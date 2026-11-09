"""Trading rules. Each strategy looks ONLY at 1-minute candles that closed before
the window starts and returns "Up", "Down" or None (skip this window).

candles: list of dicts {t, open, high, low, close, volume}, oldest first,
         ending with the last full minute before the window opens.
"""
import random


def _ret(candles, minutes):
    if len(candles) < minutes + 1:
        return None
    start = candles[-(minutes + 1)]["close"]
    end = candles[-1]["close"]
    return (end - start) / start


def coinflip(candles, rng=random):
    """Control group. A real strategy has to beat this."""
    return rng.choice(["Up", "Down"])


def always_up(candles):
    return "Up"


def make_momentum(minutes, threshold):
    def strat(candles):
        r = _ret(candles, minutes)
        if r is None or abs(r) < threshold:
            return None
        return "Up" if r > 0 else "Down"
    strat.__name__ = f"momentum_{minutes}m_{threshold*100:.2f}pct"
    return strat


def make_reversal(minutes, threshold):
    def strat(candles):
        r = _ret(candles, minutes)
        if r is None or abs(r) < threshold:
            return None
        return "Down" if r > 0 else "Up"
    strat.__name__ = f"reversal_{minutes}m_{threshold*100:.2f}pct"
    return strat


def trend_filter(candles):
    """Bet with the 60-min trend only when the last 5 min agree with it."""
    r60, r5 = _ret(candles, 60), _ret(candles, 5)
    if r60 is None or r5 is None:
        return None
    if r60 > 0.002 and r5 > 0:
        return "Up"
    if r60 < -0.002 and r5 < 0:
        return "Down"
    return None


def all_strategies():
    strats = {"coinflip": coinflip, "always_up": always_up, "trend_filter": trend_filter}
    for m in (5, 15, 60):
        for th in (0.0, 0.001, 0.003):
            for s in (make_momentum(m, th), make_reversal(m, th)):
                strats[s.__name__] = s
    return strats


# Strategies the live bot paper-trades. Update this list after backtests.
LIVE = [
    "coinflip",
    "always_up",
    "trend_filter",
    "momentum_15m_0.10pct",
    "reversal_15m_0.10pct",
    "momentum_60m_0.30pct",
    "reversal_60m_0.30pct",
    "momentum_5m_0.00pct",
]
