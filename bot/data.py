"""Market data: BTC candles from Coinbase, odds from Polymarket. Public endpoints, no keys."""
import json
import time
import urllib.parse
import urllib.request
from datetime import datetime, timezone

from . import config

UA = {"User-Agent": "btc-paper-bot/1.0 (paper trading research)"}


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


def coinbase_candles(start_ts, end_ts):
    """1-minute candles in [start_ts, end_ts), oldest first. Coinbase caps 300 per call."""
    out = {}
    cur = start_ts
    while cur < end_ts:
        chunk_end = min(cur + 300 * 60, end_ts)
        rows = _get(
            f"https://api.exchange.coinbase.com/products/{config.COINBASE_PRODUCT}/candles",
            {"granularity": 60, "start": _iso(cur), "end": _iso(chunk_end)},
        )
        for t, low, high, op, close, vol in rows:
            if start_ts <= t < end_ts:
                out[int(t)] = {"t": int(t), "open": float(op), "high": float(high),
                               "low": float(low), "close": float(close), "volume": float(vol)}
        cur = chunk_end
        time.sleep(0.25)  # stay well under Coinbase's public rate limit
    return [out[k] for k in sorted(out)]


def window_outcome(candles, start_ts):
    """'Up' if BTC closed the 15-min window at or above where it opened, else 'Down'.
    Returns None if candles are missing."""
    end_ts = start_ts + config.WINDOW_SECONDS
    w = [c for c in candles if start_ts <= c["t"] < end_ts]
    if len(w) < 13:  # tolerate a couple of missing minutes
        return None, None, None
    first = min(w, key=lambda c: c["t"])
    last = max(w, key=lambda c: c["t"])
    o, c = first["open"], last["close"]
    return ("Up" if c >= o else "Down"), o, c


def polymarket_prices(start_ts):
    """Best ask (cost to buy) for Up and Down in the 15-min market starting at start_ts.
    Returns dict like {"Up": 0.53, "Down": 0.49, "slug": ...} or None if not found."""
    slug = config.POLY_SLUG_TEMPLATE.format(start=start_ts)
    market = None
    try:
        events = _get("https://gamma-api.polymarket.com/events", {"slug": slug}, retries=2)
        if events and events[0].get("markets"):
            market = events[0]["markets"][0]
    except Exception:  # noqa: BLE001
        pass
    if market is None:
        try:
            ms = _get("https://gamma-api.polymarket.com/markets", {"slug": slug}, retries=2)
            market = ms[0] if ms else None
        except Exception:  # noqa: BLE001
            return None
    if market is None:
        return None

    def _list(v):
        return json.loads(v) if isinstance(v, str) else (v or [])

    outcomes = _list(market.get("outcomes"))
    tokens = _list(market.get("clobTokenIds"))
    if len(outcomes) != 2 or len(tokens) != 2:
        return None
    prices = {"slug": slug}
    for name, tok in zip(outcomes, tokens):
        try:
            book = _get("https://clob.polymarket.com/book", {"token_id": tok}, retries=2)
            asks = [float(a["price"]) for a in book.get("asks", []) if float(a.get("size", 0)) > 0]
            prices[name.capitalize()] = min(asks) if asks else None
        except Exception:  # noqa: BLE001
            prices[name.capitalize()] = None
    if prices.get("Up") is None and prices.get("Down") is None:
        return None
    return prices
