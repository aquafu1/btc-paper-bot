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


def model_prob_up(hist, window, secs_left):
    """Chance BTC finishes the window at/above its open, from current move + recent volatility.
    hist: candles before the window. window: candles inside the window so far."""
    import math
    closes = [c["close"] for c in hist[-61:]]
    rets = [math.log(b / a) for a, b in zip(closes, closes[1:]) if a > 0]
    if len(rets) < 30 or secs_left <= 0:
        return None
    mean = sum(rets) / len(rets)
    sigma = math.sqrt(sum((r - mean) ** 2 for r in rets) / (len(rets) - 1))
    if sigma <= 0:
        return None
    if window:
        w_open, cur = window[0]["open"], window[-1]["close"]
    else:
        w_open = cur = hist[-1]["close"]
    z = math.log(cur / w_open) / (sigma * math.sqrt(secs_left / 60))
    return 0.5 * (1 + math.erf(z / math.sqrt(2)))


def make_value(min_ev, fee_rate):
    """Only bet when Polymarket's price looks wrong vs. the model.
    Expected return per $1 staked = p/price - 1 - fee. Bet the side with the best one if > min_ev."""
    def strat(hist, window, prices, secs_left):
        p_up = model_prob_up(hist, window, secs_left)
        if p_up is None or not prices:
            return None
        best, best_ev = None, min_ev
        for side, p in (("Up", p_up), ("Down", 1 - p_up)):
            price = prices.get(side)
            if not price or not (0.03 <= price <= 0.97):
                continue
            ev = p / price - 1 - fee_rate
            if ev > best_ev:
                best, best_ev = side, ev
        return best
    strat.__name__ = f"value_ev{int(min_ev*100)}"
    strat.needs_market = True
    return strat


def all_strategies():
    strats = {"coinflip": coinflip, "always_up": always_up, "trend_filter": trend_filter}
    for m in (5, 15, 60):
        for th in (0.0, 0.001, 0.003):
            for s in (make_momentum(m, th), make_reversal(m, th)):
                strats[s.__name__] = s
    from .config import FEE_RATE
    for ev in (0.05, 0.10, 0.20):
        s = make_value(ev, FEE_RATE)
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
    # "Odds look wrong" bets: need live Polymarket prices, so they can't be backtested.
    "value_ev5",
    "value_ev10",
    "value_ev20",
]
