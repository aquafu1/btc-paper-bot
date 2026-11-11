"""Live PAPER trader (fake money).

On GitHub Actions this runs as a loop:  python -m bot.live --loop
Every 15-min window it wakes twice:
  +20s   buys fake $10 positions for each strategy's pick, on BTC/ETH/SOL/XRP, at the price
         the real Polymarket order book would fill (fees included)
  +300s  settles the window that just ended, using Polymarket's official result
After ~5.5 hours the loop exits and the workflow starts a fresh one (GitHub's 6h job limit).
Results are committed to results/ after every wake.

python -m bot.live      runs one wake and exits (handy for testing).
"""
import argparse
import csv
import math
import os
import random
import subprocess
import time
from datetime import datetime, timezone

from . import config, data, scoring, strategies

TRADES = "results/trades.csv"
ARCHIVE = "results/archive_v1_trades.csv"
BOARD = "results/LEADERBOARD.md"
LOG = "results/run_log.csv"
W = config.WINDOW_SECONDS
FIELDS = ["window_start", "window_start_utc", "coin", "strategy", "pick", "best_ask", "avg_price",
          "shares", "fee", "entered_at", "status", "outcome", "won", "pnl", "settled_by",
          "price_to_beat", "final_price"]

try:
    from zoneinfo import ZoneInfo
    CT = ZoneInfo("America/Chicago")
except Exception:  # noqa: BLE001
    CT = timezone.utc


def ct(ts, fmt="%a %b %d, %-I:%M %p CT"):
    s = datetime.fromtimestamp(ts, tz=CT).strftime(fmt)
    return s if CT is not timezone.utc else s.replace("CT", "UTC")


# ---------- storage ----------

def migrate_v1():
    """Version 1 trades were entered 6-10 min late with a guessed fee; keep them, but out of
    the stats."""
    if not os.path.exists(TRADES):
        return
    with open(TRADES) as f:
        header = f.readline()
    if "coin" not in header.split(","):
        os.replace(TRADES, ARCHIVE)


def load():
    if not os.path.exists(TRADES):
        return []
    with open(TRADES) as f:
        return list(csv.DictReader(f))


def save(rows):
    os.makedirs("results", exist_ok=True)
    tmp = TRADES + ".tmp"
    with open(tmp, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        w.writeheader()
        w.writerows(rows)
    os.replace(tmp, TRADES)


def log_run(msg, now):
    new = not os.path.exists(LOG)
    with open(LOG, "a", newline="") as f:
        w = csv.writer(f)
        if new:
            w.writerow(["run_at_utc", "note"])
        w.writerow([datetime.fromtimestamp(now, tz=timezone.utc).isoformat(timespec="seconds"), msg])


# ---------- trading ----------

def settle(rows, now):
    pending = {}
    for r in rows:
        if r["status"] == "open" and int(r["window_start"]) + W <= now:
            pending.setdefault((r["coin"].lower(), int(r["window_start"])), []).append(r)
    done = waiting = 0
    errors = []
    for (coin, ws), group in sorted(pending.items(), key=lambda kv: kv[0][1]):
        try:
            res = data.official_result(coin, ws)
        except Exception as e:  # noqa: BLE001
            errors.append(f"{coin} {ws}: {e}")
            res = None
        if res is None:
            if now - (ws + W) > 6 * 3600:   # never resolved: don't count it either way
                for r in group:
                    r["status"] = "void"
            else:
                waiting += len(group)
            continue
        for r in group:
            won = r["pick"] == res["outcome"]
            r.update(status="settled", outcome=res["outcome"], won=str(won),
                     pnl=f"{scoring.pnl(won, float(r['shares'])):.4f}", settled_by="polymarket",
                     price_to_beat=res["price_to_beat"] or "", final_price=res["final_price"] or "")
            done += 1
    msg = f"settled {done}, waiting {waiting}"
    if errors:
        msg += " | settle errors: " + "; ".join(errors[:3])
    return msg


def enter(rows, now):
    ws = now // W * W
    delay = now - ws
    if any(int(r["window_start"]) == ws for r in rows):
        return None
    if delay < config.ENTRY_DELAY:
        return None
    if delay > config.MAX_ENTRY_DELAY:
        return f"skipped {ct(ws, '%-I:%M %p')} window: {delay}s late"

    strats = strategies.all_strategies()
    notes = []
    for coin in config.COINS:
        try:
            info = data.market_info(coin, ws)
            if info is None or not info["accepting"]:
                notes.append(f"{coin} no market")
                continue
            product = config.COINBASE_PRODUCT[coin]
            hist = window = None
            for _ in range(3):   # the last pre-window minute can take a few seconds to appear
                allc = data.coinbase_candles(ws - 62 * 60, int(time.time()) + 60, product)
                hist = [c for c in allc if c["t"] < ws]
                window = [c for c in allc if c["t"] >= ws]
                if hist and hist[-1]["t"] == ws - 60 and len(hist) >= 61:
                    break
                time.sleep(5)
            if not hist or hist[-1]["t"] != ws - 60 or len(hist) < 61:
                notes.append(f"{coin} candles not ready")
                continue
            asks = {side: data.book_asks(tok) for side, tok in info["tokens"].items()}
            prices = {side: (a[0][0] if a else None) for side, a in asks.items()}
            prices.update(fee_rate=info["fee_rate"], fee_exp=info["fee_exp"])
            secs_left = ws + W - int(time.time())
            rng = random.Random(f"{coin}-{ws}")
            made = thin = 0
            for name in strategies.LIVE:
                fn = strats[name]
                if getattr(fn, "needs_market", False):
                    pick = fn(hist, window, prices, secs_left)
                elif name == "coinflip":
                    pick = fn(hist, rng)
                else:
                    pick = fn(hist)
                if pick is None:
                    continue
                fill = data.simulate_buy(asks.get(pick, []), config.STAKE,
                                         info["fee_rate"], info["fee_exp"])
                if fill is None:
                    thin += 1
                    continue
                rows.append({
                    "window_start": ws,
                    "window_start_utc": datetime.fromtimestamp(ws, tz=timezone.utc).strftime("%Y-%m-%d %H:%M"),
                    "coin": coin.upper(), "strategy": name, "pick": pick,
                    "best_ask": f"{fill['best_ask']:.3f}", "avg_price": f"{fill['avg_price']:.4f}",
                    "shares": f"{fill['shares']:.4f}", "fee": f"{fill['fee']:.4f}",
                    "entered_at": f"+{int(time.time()) - ws}s", "status": "open", "outcome": "",
                    "won": "", "pnl": "", "settled_by": "", "price_to_beat": "", "final_price": "",
                })
                made += 1
            notes.append(f"{coin} {made}" + (f" ({thin} skipped: thin book)" if thin else ""))
        except Exception as e:  # noqa: BLE001
            notes.append(f"{coin} error: {e}")
    return f"entered {ct(ws, '%-I:%M %p')} window ({delay}s in): " + ", ".join(notes)


# ---------- leaderboard ----------

def leaderboard(rows, now):
    settled = [r for r in rows if r["status"] == "settled"]
    open_n = sum(1 for r in rows if r["status"] == "open")
    windows = sorted({int(r["window_start"]) for r in rows})

    def summ(rs):
        return scoring.summarize([{"won": r["won"] == "True", "pnl": float(r["pnl"]),
                                   "payout": float(r["shares"])} for r in rs])

    by = {}
    for r in settled:
        by.setdefault(r["strategy"], []).append(r)
    stats = {k: summ(v) for k, v in by.items()}
    for name in strategies.LIVE:
        stats.setdefault(name, {"trades": 0})

    # pace: settled trades per window, from the first window to the last settled one
    settled_windows = sorted({int(r["window_start"]) for r in settled})
    n_win = (settled_windows[-1] - settled_windows[0]) // W + 1 if settled_windows else 0

    def eta(n):
        if n >= config.MIN_TRADES:
            return "done"
        if n == 0 or n_win == 0:
            return "-"
        more = math.ceil((config.MIN_TRADES - n) / (n / n_win))
        return ct(settled_windows[-1] + (more + 1) * W, "%a %-I:%M %p")

    start = ct(windows[0]) if windows else "-"
    lines = [
        "# Paper trading leaderboard (FAKE money)",
        "",
        f"**Updated {ct(now)}.** Running since {start}: {len(windows)} windows, "
        f"{len(settled)} settled trades, {open_n} waiting for results. Coins: "
        + ", ".join(c.upper() for c in config.COINS) + ".",
        "",
        f"Each strategy: ${config.STARTING_BANKROLL:.0f} fake bankroll, ${config.STAKE:.0f} per trade, "
        "bought ~20s after each 15-min window opens at the real Polymarket order-book price, "
        "with Polymarket's real fee, settled by Polymarket's official result.",
        "",
        f"| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits {config.MIN_TRADES} | Verdict |",
        "|---|---|---|---|---|---|---|---|---|---|",
    ]
    order = sorted(stats.items(), key=lambda kv: kv[1].get("pnl", -1e9), reverse=True)
    for name, s in order:
        if s["trades"] == 0:
            lines.append(f"| {name} | 0 | - | - | - | - | - | - | - | no trades yet |")
            continue
        z = f"{s['z']:+.1f}" if not math.isnan(s["z"]) else "-"
        lines.append(
            f"| {name} | {s['trades']} | {s['win_rate']*100:.1f} | {s['breakeven']*100:.1f} | "
            f"${s['pnl']:+.2f} | {s['roi']*100:+.1f}% | ${s['bankroll']:.2f} | {z} | "
            f"{eta(s['trades'])} | {scoring.verdict(s)} |")

    lines += ["", "## By coin (all strategies)", "",
              "| Coin | Trades | Win % | Break-even % | P&L |", "|---|---|---|---|---|"]
    for coin in config.COINS:
        rs = [r for r in settled if r["coin"] == coin.upper()]
        if not rs:
            lines.append(f"| {coin.upper()} | 0 | - | - | - |")
            continue
        s = summ(rs)
        lines.append(f"| {coin.upper()} | {s['trades']} | {s['win_rate']*100:.1f} | "
                     f"{s['breakeven']*100:.1f} | ${s['pnl']:+.2f} |")

    lines += [
        "",
        "**How to read this:** a strategy makes money only if **Win % beats Break-even %**. "
        f"Ignore anything under {config.MIN_TRADES} trades. It should also clearly beat `coinflip` "
        "(random picks). **z** = how many standard errors the average profit is above zero; "
        "\"real edge?\" needs z of 2 or more, and even then let it keep running before trusting it. "
        "The 4 coins usually move together, so a strategy's trades in the same window aren't "
        "fully independent.",
        "",
        "Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in "
        "`archive_v1_trades.csv` and left out of these stats.",
    ]
    with open(BOARD, "w") as f:
        f.write("\n".join(lines) + "\n")


# ---------- running ----------

def run_once():
    now = int(time.time())
    rows = load()
    notes = []
    try:
        notes.append(settle(rows, now))
    except Exception as e:  # noqa: BLE001
        notes.append(f"settle error: {e}")
    try:
        msg = enter(rows, now)
        if msg:
            notes.append(msg)
    except Exception as e:  # noqa: BLE001
        notes.append(f"enter error: {e}")
    save(rows)
    leaderboard(rows, int(time.time()))
    msg = "; ".join(notes)
    log_run(msg, now)
    print(datetime.now(timezone.utc).strftime("%H:%M:%S"), msg, flush=True)


def git(*args):
    return subprocess.run(["git", *args], capture_output=True, text=True)


def git_save():
    """Commit and push results (only on GitHub Actions)."""
    if not os.environ.get("GITHUB_ACTIONS"):
        return
    git("add", "results")
    if git("diff", "--cached", "--quiet").returncode == 0:
        return
    git("commit", "-q", "-m", f"paper trades {datetime.now(timezone.utc):%Y-%m-%dT%H:%MZ}")
    for i in range(4):
        pull = git("pull", "-q", "--rebase")
        if pull.returncode != 0:
            git("rebase", "--abort")
        if pull.returncode == 0 and git("push", "-q").returncode == 0:
            return
        time.sleep(5 * (i + 1))
    print("WARNING: push failed, will retry next wake", flush=True)


def next_wake(now):
    ws = now // W * W
    for t in (ws + config.ENTRY_DELAY, ws + config.SETTLE_DELAY, ws + W + config.ENTRY_DELAY):
        if t > now:
            return t
    return ws + W + config.ENTRY_DELAY


def loop():
    deadline = time.time() + config.LOOP_SECONDS
    migrate_v1()
    while True:
        try:
            run_once()
            git_save()
        except Exception as e:  # noqa: BLE001  never let one bad wake kill the loop
            print("wake error:", e, flush=True)
        wake = next_wake(int(time.time()))
        if wake > deadline:
            print("loop time used up; the workflow starts a fresh loop", flush=True)
            return
        time.sleep(max(1, wake - time.time()))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--loop", action="store_true")
    if ap.parse_args().loop:
        loop()
    else:
        migrate_v1()
        run_once()


if __name__ == "__main__":
    main()
