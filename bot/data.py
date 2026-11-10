"""Market data: candles from Coinbase, markets/order books/results from Polymarket.
Public endpoints, no keys."""
import json
import time
import urllib.parse
import urllib.request
from datetime import datetime, timezone

from . import config, scoring

UA = {"User-Agent": "btc-paper-bot/2.0 (paper trading research)"}


def _get(url, params=None, retries=3):
    if params:
        url += "?" + urllib.parse.urlencode(params)
    last = None
    for i in range(retries):
        try:
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=20) as r:
                return json.loads(r.read().decode())
        except Exception as e:  # noqa: BLE001
            last = e
            time.sleep(1.5 * (i + 1))
    raise RuntimeError(f"GET failed {url}: {last}")


def _iso(ts):
    return datetime.fromtimestamp(ts, tz=timezone.utc).isoformat()


def coinbase_candles(start_ts, end_ts, product="BTC-USD"):
    """1-minute candles in [start_ts, end_ts), oldest first. Coinbase caps 300 per call.
    Coinbase skips minutes with no trades; those are filled with the previous close so
    that "N candles back" always means N minutes back. The newest candle may still be
    in progress (Coinbase returns the current minute)."""
    out = {}
    cur = start_ts
    while cur < end_ts:
        chunk_end = min(cur + 300 * 60, end_ts)
        rows = _get(
            f"https://api.exchange.coinbase.com/products/{product}/candles",
            {"granularity": 60, "start": _iso(cur), "end": _iso(chunk_end)},
        )
        for t, low, high, op, close, vol in rows:
            if start_ts <= t < end_ts:
                out[int(t)] = {"t": int(t), "open": float(op), "high": float(high),
                               "low": float(low), "close": float(close), "volume": float(vol)}
        cur = chunk_end
        time.sleep(0.25)  # stay well under Coinbase's public rate limit
    return fill_gaps([out[k] for k in sorted(out)])


def fill_gaps(candles):
    if not candles:
        return candles
    filled = [candles[0]]
    for c in candles[1:]:
        prev = filled[-1]
        t = prev["t"] + 60
        while t < c["t"]:
            p = prev["close"]
            filled.append({"t": t, "open": p, "high": p, "low": p, "close": p, "volume": 0.0})
            t += 60
        filled.append(c)
    return filled


def window_outcome(candles, start_ts):
    """Backtest only: 'Up' if the coin closed the window at/above where it opened.
    (Live trades are settled with Polymarket's official result instead.)"""
    end_ts = start_ts + config.WINDOW_SECONDS
    w = [c for c in candles if start_ts <= c["t"] < end_ts]
    if len(w) < 13:
        return None, None, None
    first = min(w, key=lambda c: c["t"])
    last = max(w, key=lambda c: c["t"])
    o, c = first["open"], last["close"]
    return ("Up" if c >= o else "Down"), o, c


def _list(v):
    return json.loads(v) if isinstance(v, str) else (v or [])


def slug(coin, start_ts):
    return config.POLY_SLUG_TEMPLATE.format(coin=coin.lower(), start=int(start_ts))


def polymarket_event(coin, start_ts):
    """The Gamma 'event' for a coin's 15-min window. The events endpoint returns both open
    and finished windows (the markets endpoint hides finished ones). None if not found."""
    ev = _get("https://gamma-api.polymarket.com/events", {"slug": slug(coin, start_ts)}, retries=2)
    if not ev or not ev[0].get("markets"):
        return None
    return ev[0]


def market_info(coin, start_ts):
    """Token ids and fee settings for a window's market, or None."""
    ev = polymarket_event(coin, start_ts)
    if ev is None:
        return None
    m = ev["markets"][0]
    outcomes, tokens = _list(m.get("outcomes")), _list(m.get("clobTokenIds"))
    if len(outcomes) != 2 or len(tokens) != 2:
        return None
    fs = m.get("feeSchedule") or {}
    return {
        "slug": slug(coin, start_ts),
        "tokens": {o.capitalize(): t for o, t in zip(outcomes, tokens)},
        "accepting": bool(m.get("acceptingOrders")),
        "fee_rate": float(fs.get("rate", config.FEE_RATE)) if m.get("feesEnabled", True) else 0.0,
        "fee_exp": float(fs.get("exponent", config.FEE_EXPONENT)),
    }


def book_asks(token_id):
    """Sell orders you could buy from, cheapest first: [(price, shares), ...]."""
    book = _get("https://clob.polymarket.com/book", {"token_id": token_id}, retries=2)
    asks = [(float(a["price"]), float(a["size"])) for a in book.get("asks", [])
            if float(a.get("size", 0)) > 0]
    return sorted(asks)


def simulate_buy(asks, stake, rate, exponent):
    """Fill a `stake`-dollar market buy against the order book, level by level.
    Returns dict(best_ask, avg_price, shares (after fee), fee) or None if the book is too thin."""
    if not asks:
        return None
    left, gross, fee, fee_shares = stake, 0.0, 0.0, 0.0
    for price, size in asks:
        if left <= 1e-9:
            break
        if not (0 < price < 1):
            continue
        spend = min(left, price * size)
        sh = spend / price
        f = scoring.fee_dollars(sh, price, rate, exponent)
        gross += sh
        fee += f
        fee_shares += f / price   # fee is collected in shares on buys, at the fill price
        left -= spend
    if left > 1e-6 or gross < config.MIN_SHARES:
        return None
    return {"best_ask": asks[0][0], "avg_price": stake / gross,
            "shares": gross - fee_shares, "fee": fee}


def official_result(coin, start_ts):
    """Polymarket's own resolution (Chainlink price). Returns dict(outcome, price_to_beat,
    final_price) once resolved, else None."""
    ev = polymarket_event(coin, start_ts)
    if ev is None:
        return None
    m = ev["markets"][0]
    if not m.get("closed") or m.get("umaResolutionStatus") != "resolved":
        return None
    outcomes, prices = _list(m.get("outcomes")), [float(p) for p in _list(m.get("outcomePrices"))]
    if len(outcomes) != 2 or len(prices) != 2 or sorted(prices) != [0.0, 1.0]:
        return None
    meta = ev.get("eventMetadata") or {}
    return {"outcome": outcomes[prices.index(1.0)].capitalize(),
            "price_to_beat": meta.get("priceToBeat"), "final_price": meta.get("finalPrice")}
