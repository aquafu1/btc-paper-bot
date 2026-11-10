"""Profit math and stats.

A share bought at price p pays $1 if right, $0 if wrong. Polymarket charges takers
fee = shares * rate * (p*(1-p))**exponent dollars, taken out of the shares you receive.
"""
import math

from . import config


def fee_dollars(shares, price, rate=config.FEE_RATE, exponent=config.FEE_EXPONENT):
    return round(shares * rate * (price * (1 - price)) ** exponent, 5)


def buy_at(price, stake=config.STAKE, rate=config.FEE_RATE, exponent=config.FEE_EXPONENT):
    """Spend `stake` at a single price. Returns (shares kept after fee, fee in $)."""
    gross = stake / price
    fee = fee_dollars(gross, price, rate, exponent)
    return gross - fee / price, fee


def pnl(won, net_shares, stake=config.STAKE):
    return net_shares - stake if won else -stake


def trade_pnl(won, price, stake=config.STAKE):
    """Backtest helper: single fixed price."""
    shares, _ = buy_at(price, stake)
    return pnl(won, shares, stake)


def breakeven_at(price):
    """Win rate needed to break even buying at one price (fees included)."""
    shares, _ = buy_at(price, 1.0)
    return 1.0 / shares


def summarize(trades):
    """trades: list of dicts with won (bool), pnl (float), payout (float: $ received if won)."""
    n = len(trades)
    if n == 0:
        return {"trades": 0}
    wins = sum(1 for t in trades if t["won"])
    pnls = [t["pnl"] for t in trades]
    total = sum(pnls)
    staked = n * config.STAKE
    # Break-even win rate across trades bought at different prices:
    # total staked / total you'd collect if every trade won.
    be = staked / sum(t["payout"] for t in trades)
    # t-stat of the average profit per trade: how many standard errors above zero.
    if n >= 2:
        mean = total / n
        sd = math.sqrt(sum((p - mean) ** 2 for p in pnls) / (n - 1))
        z = mean / (sd / math.sqrt(n)) if sd > 0 else float("nan")
    else:
        z = float("nan")
    bank = peak = config.STARTING_BANKROLL
    mdd = 0.0
    for p in pnls:
        bank += p
        peak = max(peak, bank)
        mdd = max(mdd, peak - bank)
    return {
        "trades": n, "wins": wins, "win_rate": wins / n, "breakeven": be, "z": z,
        "pnl": total, "roi": total / staked, "max_drawdown": mdd,
        "bankroll": config.STARTING_BANKROLL + total,
    }


def verdict(s, min_trades=config.MIN_TRADES):
    if s["trades"] < min_trades:
        return f"too few trades ({s['trades']}/{min_trades})"
    if s["z"] >= 2:
        return "real edge? (z>=2)"
    if s["z"] <= -2:
        return "losing for real"
    return "can't tell from luck"
