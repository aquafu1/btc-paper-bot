"""Live PAPER trader. Run every ~15 min (GitHub Actions does this).

Each run:
  1. settles finished trades using real BTC prices
  2. opens new fake trades for the current 15-min window, at real Polymarket prices if available
  3. rewrites results/trades.csv and results/LEADERBOARD.md
"""
import csv
import os
import random
import time
from datetime import datetime, timezone

from . import config, data, scoring, strategies

TRADES = "results/trades.csv"
BOARD = "results/LEADERBOARD.md"
LOG = "results/run_log.csv"
FIELDS = ["window_start", "window_start_utc", "strategy", "pick", "price", "price_source",
          "entered_at", "status", "outcome", "won", "pnl", "btc_open", "btc_close"]


def load():
    if not os.path.exists(TRADES):
        return []
    with open(TRADES) as f:
        return list(csv.DictReader(f))


def save(rows):
    os.makedirs("results", exist_ok=True)
    with open(TRADES, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        w.writeheader()
        w.writerows(rows)


def log_run(msg, now):
    new = not os.path.exists(LOG)
    with open(LOG, "a", newline="") as f:
        w = csv.writer(f)
        if new:
            w.writerow(["run_at_utc", "note"])
        w.writerow([datetime.fromtimestamp(now, tz=timezone.utc).isoformat(timespec="seconds"), msg])


def settle(rows, now):
    open_rows = [r for r in rows if r["status"] == "open"
                 and int(r["window_start"]) + config.WINDOW_SECONDS + 60 <= now]
    if not open_rows:
        return 0
    starts = sorted({int(r["window_start"]) for r in open_rows})
    candles = data.coinbase_candles(starts[0], starts[-1] + config.WINDOW_SECONDS)
    n = 0
    for r in open_rows:
        ws = int(r["window_start"])
        outcome, o, c = data.window_outcome(candles, ws)
        if outcome is None:
            if now - ws > 6 * 3600:  # give up on windows with missing data
                r["status"] = "void"
            continue
        won = r["pick"] == outcome
        r.update(status="settled", outcome=outcome, won=str(won),
                 pnl=f"{scoring.trade_pnl(won, float(r['price'])):.4f}",
                 btc_open=f"{o:.2f}", btc_close=f"{c:.2f}")
        n += 1
    return n


def enter(rows, now):
    ws = now // config.WINDOW_SECONDS * config.WINDOW_SECONDS
    if any(int(r["window_start"]) == ws for r in rows):
        return "already entered this window"
    delay = now - ws
    if delay > config.MAX_ENTRY_DELAY_REAL_PRICE:
        return f"skipped: run was {delay//60} min late into window"

    poly = data.polymarket_prices(ws)
    if poly is None and delay > config.MAX_ENTRY_DELAY_SIM_PRICE:
        return f"skipped: no Polymarket price and {delay//60} min into window"

    hist = data.coinbase_candles(ws - 61 * 60, ws)
    if len(hist) < 55:
        return "skipped: not enough candle history"

    strats = strategies.all_strategies()
    rng = random.Random(ws)
    made = 0
    for name in strategies.LIVE:
        fn = strats[name]
        pick = fn(hist, rng) if name == "coinflip" else fn(hist)
        if pick is None:
            continue
        if poly and poly.get(pick):
            price, src = poly[pick], "polymarket_ask"
        else:
            price, src = config.SIM_ENTRY_PRICE, "simulated"
        if not (0.01 <= price <= 0.99):
            continue
        rows.append({
            "window_start": ws,
            "window_start_utc": datetime.fromtimestamp(ws, tz=timezone.utc).strftime("%Y-%m-%d %H:%M"),
            "strategy": name, "pick": pick, "price": f"{price:.3f}", "price_source": src,
            "entered_at": f"+{delay}s", "status": "open", "outcome": "", "won": "", "pnl": "",
            "btc_open": "", "btc_close": "",
        })
        made += 1
    src = "real Polymarket odds" if poly else "simulated 51c"
    return f"entered {made} trades ({src}, {delay}s into window)"


def leaderboard(rows, now):
    settled = [r for r in rows if r["status"] == "settled"]
    by = {}
    for r in settled:
        by.setdefault(r["strategy"], []).append(
            {"won": r["won"] == "True", "price": float(r["price"]), "pnl": float(r["pnl"])})
    stats = {k: scoring.summarize(v) for k, v in by.items()}
    real = sum(1 for r in settled if r["price_source"] == "polymarket_ask")
    first = min((r["window_start_utc"] for r in settled), default="-")
    lines = [
        "# Paper trading leaderboard (FAKE money)",
        "",
        f"Updated {datetime.fromtimestamp(now, tz=timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}. "
        f"Running since {first}. Each strategy starts with ${config.STARTING_BANKROLL:.0f}, "
        f"bets ${config.STAKE:.0f}/trade. {len(settled)} settled trades "
        f"({real} at real Polymarket prices).",
        "",
        "| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | Worst drawdown | Verdict |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    for name, s in sorted(stats.items(), key=lambda kv: kv[1]["pnl"], reverse=True):
        lines.append(
            f"| {name} | {s['trades']} | {s['win_rate']*100:.1f} | {s['breakeven']*100:.1f} | "
            f"${s['pnl']:+.2f} | {s['roi']*100:+.1f}% | ${s['bankroll']:.2f} | "
            f"${s['max_drawdown']:.2f} | {scoring.verdict(s)} |"
        )
    lines += [
        "",
        "**How to read this:** a strategy makes money only if Win % beats Break-even %. "
        "Ignore anything under ~300 trades. It should also clearly beat `coinflip`. "
        "\"real edge?\" means the win rate is 2+ standard errors above break-even -- "
        "still check it holds for another week before trusting it.",
    ]
    with open(BOARD, "w") as f:
        f.write("\n".join(lines) + "\n")


def main():
    now = int(time.time())
    rows = load()
    notes = []
    try:
        notes.append(f"settled {settle(rows, now)}")
    except Exception as e:  # noqa: BLE001
        notes.append(f"settle error: {e}")
    try:
        notes.append(enter(rows, now))
    except Exception as e:  # noqa: BLE001
        notes.append(f"enter error: {e}")
    save(rows)
    leaderboard(rows, now)
    msg = "; ".join(notes)
    log_run(msg, now)
    print(msg)


if __name__ == "__main__":
    main()
