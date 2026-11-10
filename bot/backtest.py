"""Backtest every strategy on recent real BTC data, assuming a fixed entry price and
Polymarket's real fee formula.

Usage: python -m bot.backtest [days]      (default 21)
Writes results/backtest_report.md
"""
import os
import random
import sys
import time
from datetime import datetime, timezone

from . import config, data, scoring, strategies

LOOKBACK_MIN = 61


def run(candles, days_test, rng_seed=7):
    """candles: oldest-first 1-min candles. Returns {name: {"all","train","test"}} summaries."""
    idx = {c["t"]: i for i, c in enumerate(candles)}
    first_t, last_t = candles[0]["t"], candles[-1]["t"]
    W = config.WINDOW_SECONDS
    start = ((first_t + LOOKBACK_MIN * 60) // W + 1) * W
    test_from = last_t - days_test * 86400
    strats = {k: v for k, v in strategies.all_strategies().items()
              if not getattr(v, "needs_market", False)}  # no historical Polymarket prices
    rng = random.Random(rng_seed)
    results = {name: [] for name in strats}

    ws = start
    while ws + W <= last_t + 60:
        i = idx.get(ws)
        prev = idx.get(ws - 60)
        if i is not None and prev is not None and prev >= LOOKBACK_MIN - 1:
            hist = candles[prev - LOOKBACK_MIN + 1: prev + 1]
            outcome, _, _ = data.window_outcome(candles[i: i + 16], ws)
            if outcome:
                for name, fn in strats.items():
                    pick = fn(hist, rng) if name == "coinflip" else fn(hist)
                    if pick is None:
                        continue
                    won = pick == outcome
                    shares, _ = scoring.buy_at(config.SIM_ENTRY_PRICE)
                    results[name].append({"t": ws, "won": won, "payout": shares,
                                          "pnl": scoring.pnl(won, shares), "test": ws >= test_from})
        ws += W

    out = {}
    for name, trades in results.items():
        out[name] = {
            "all": scoring.summarize(trades),
            "train": scoring.summarize([t for t in trades if not t["test"]]),
            "test": scoring.summarize([t for t in trades if t["test"]]),
        }
    return out


def report(results, days, days_test, first_t, last_t):
    def d(ts):
        return datetime.fromtimestamp(ts, tz=timezone.utc).strftime("%b %d %H:%M UTC")

    lines = [
        "# Backtest report (FAKE money)",
        "",
        f"Data: Coinbase BTC-USD 1-min candles, {d(first_t)} to {d(last_t)} ({days} days).",
        f"Assumed entry price {config.SIM_ENTRY_PRICE:.2f}, Polymarket's crypto taker fee "
        f"({config.FEE_RATE} x p x (1-p) per share), ${config.STAKE:.0f} per trade. Break-even win rate = "
        f"{scoring.breakeven_at(config.SIM_ENTRY_PRICE)*100:.1f}%.",
        "",
        f"**Train** = first {days - days_test} days (where you'd pick a strategy). "
        f"**Test** = last {days_test} days (did it still work on data it wasn't picked on?).",
        "",
        "| Strategy | Trades | Win % | P&L (all) | Train P&L | Test P&L | Test win % | Verdict |",
        "|---|---|---|---|---|---|---|---|",
    ]
    rows = sorted(results.items(), key=lambda kv: kv[1]["train"].get("pnl", -1e9), reverse=True)
    for name, r in rows:
        a, tr, te = r["all"], r["train"], r["test"]
        if a["trades"] == 0:
            continue
        lines.append(
            f"| {name} | {a['trades']} | {a['win_rate']*100:.1f} | ${a['pnl']:+.0f} | "
            f"${tr.get('pnl', 0):+.0f} | ${te.get('pnl', 0):+.0f} | "
            f"{te.get('win_rate', 0)*100:.1f} | {scoring.verdict(a, 100)} |"
        )
    lines += [
        "",
        "Sorted by Train P&L. A strategy is only interesting if it is ALSO positive in Test "
        "and beats coinflip. With ~18 strategies, one or two will look good by pure luck.",
        "",
        "Big caveat: real Polymarket prices move with BTC, so the 51c assumption is generous "
        "when a move is obvious. The live paper bot uses real Polymarket prices -- trust it over this.",
    ]
    return "\n".join(lines) + "\n"


def main():
    days = int(sys.argv[1]) if len(sys.argv) > 1 else 21
    days_test = max(2, days // 3)
    end = int(time.time()) // 60 * 60
    start = end - days * 86400 - LOOKBACK_MIN * 60
    print(f"Fetching {days} days of candles...", flush=True)
    candles = data.coinbase_candles(start, end)
    print(f"Got {len(candles)} candles", flush=True)
    res = run(candles, days_test)
    os.makedirs("results", exist_ok=True)
    with open("results/backtest_report.md", "w") as f:
        f.write(report(res, days, days_test, candles[0]["t"], candles[-1]["t"]))
    print(open("results/backtest_report.md").read())


if __name__ == "__main__":
    main()
