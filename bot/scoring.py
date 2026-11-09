"""Profit math and stats. A $1 share bought at price p pays $1 if right, $0 if wrong."""
import math

from . import config


def trade_pnl(won, price, stake=config.STAKE, fee_rate=config.FEE_RATE):
    fee = stake * fee_rate
    if won:
        return stake / price - stake - fee
    return -stake - fee


def breakeven_win_rate(avg_price, fee_rate=config.FEE_RATE):
    return avg_price * (1 + fee_rate)


def summarize(trades):
    """trades: list of dicts with keys won (bool), price (float), pnl (float)."""
    n = len(trades)
    if n == 0:
        return {"trades": 0}
    wins = sum(1 for t in trades if t["won"])
    pnl = sum(t["pnl"] for t in trades)
    avg_price = sum(t["price"] for t in trades) / n
    be = breakeven_win_rate(avg_price)
    wr = wins / n
    # z-score: how many standard errors the win rate is above break-even.
    se = math.sqrt(be * (1 - be) / n) if 0 < be < 1 else float("nan")
    z = (wr - be) / se if se else float("nan")
    # max drawdown on the running fake bankroll
    bank = peak = config.STARTING_BANKROLL
    mdd = 0.0
    for t in trades:
        bank += t["pnl"]
        peak = max(peak, bank)
        mdd = max(mdd, peak - bank)
    return {
        "trades": n, "wins": wins, "win_rate": wr, "breakeven": be, "z": z,
        "pnl": pnl, "roi": pnl / (n * config.STAKE), "max_drawdown": mdd,
        "bankroll": config.STARTING_BANKROLL + pnl,
    }


def verdict(s):
    if s["trades"] < 100:
        return "too few trades"
    if s["z"] >= 2:
        return "real edge? (z>=2)"
    if s["z"] <= -2:
        return "losing for real"
    return "can't tell from luck"
