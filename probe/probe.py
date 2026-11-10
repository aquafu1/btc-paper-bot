import json, time, urllib.request, urllib.parse
UA={"User-Agent":"btc-paper-bot/1.0 probe"}
def get(url, params=None):
    if params: url += "?" + urllib.parse.urlencode(params)
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=20) as r:
            return json.loads(r.read().decode())
    except Exception as e:
        return {"ERROR": str(e)}
now = int(time.time()); ws = now // 900 * 900
print("now", now, "ws", ws, "secs into window", now - ws)
def market(slug):
    m = get("https://gamma-api.polymarket.com/markets", {"slug": slug})
    return m[0] if isinstance(m, list) and m else m
# 1) old BTC windows: official result vs our Coinbase settlement
for w, ours in [(1794245400,"Down"),(1794246300,"Up"),(1794271500,"Up"),(1794296700,"Down")]:
    m = market(f"btc-updown-15m-{w}")
    if isinstance(m, dict) and "slug" in m:
        print("OLD", w, "ours", ours, "| closed", m.get("closed"), "outcomes", m.get("outcomes"), "outcomePrices", m.get("outcomePrices"), "uma", m.get("umaResolutionStatus"), "umaStatuses", m.get("umaResolutionStatuses"))
    else:
        print("OLD", w, m)
# 2) full field dump for one resolved market
m = market(f"btc-updown-15m-{ws-1800}")
print("KEYS", sorted(m.keys()) if isinstance(m, dict) else m)
if isinstance(m, dict):
    for k in ["question","closed","active","acceptingOrders","endDate","outcomes","outcomePrices","umaResolutionStatus","resolutionSource","feesEnabled","feeType","takerBaseFee","makerBaseFee","orderMinSize","orderPriceMinTickSize","negRisk"]:
        print("  ", k, "=", m.get(k))
    print("  description:", (m.get("description") or "")[:600])
    ev = get("https://gamma-api.polymarket.com/events", {"slug": f"btc-updown-15m-{ws-1800}"})
    if isinstance(ev, list) and ev:
        e = ev[0]; print("EVENT keys", sorted(e.keys()))
        for k in ["eventMetadata","resolutionSource","seriesSlug","tags"]:
            print("  ev", k, "=", str(e.get(k))[:400])
# 3) just-ended window: how fast does it resolve?
m = market(f"btc-updown-15m-{ws-900}")
if isinstance(m, dict): print("JUST ENDED", ws-900, "closed", m.get("closed"), "outcomePrices", m.get("outcomePrices"), "uma", m.get("umaResolutionStatus"), "endDate", m.get("endDate"))
# 4) current window for each coin: exists? book depth? fee rate?
for coin in ["btc","eth","sol","xrp"]:
    for w in (ws, ws+900):
        m = market(f"{coin}-updown-15m-{w}")
        if not (isinstance(m, dict) and "slug" in m):
            print("CUR", coin, w, "NOT FOUND", str(m)[:200]); continue
        toks = json.loads(m["clobTokenIds"]) if isinstance(m["clobTokenIds"], str) else m["clobTokenIds"]
        outs = json.loads(m["outcomes"]) if isinstance(m["outcomes"], str) else m["outcomes"]
        line = f"CUR {coin} {w} accepting={m.get('acceptingOrders')} min={m.get('orderMinSize')} tick={m.get('orderPriceMinTickSize')}"
        for o, t in zip(outs, toks):
            b = get("https://clob.polymarket.com/book", {"token_id": t})
            asks = sorted(((float(a["price"]), float(a["size"])) for a in b.get("asks", [])))[:4] if isinstance(b, dict) and "asks" in b else b
            line += f" | {o} asks {asks}"
        print(line)
        if coin == "btc" and w == ws:
            print("  fee-rate", get("https://clob.polymarket.com/fee-rate", {"token_id": toks[0]}))
            print("  fee-rate alt", get(f"https://clob.polymarket.com/fee-rate/{toks[0]}"))
            b = get("https://clob.polymarket.com/book", {"token_id": toks[0]})
            if isinstance(b, dict): print("  book keys", sorted(b.keys()), {k: b.get(k) for k in ("min_order_size","tick_size","neg_risk","last_trade_price")})
# 5) Coinbase candle latency per product
for p in ["BTC-USD","ETH-USD","SOL-USD","XRP-USD"]:
    end = int(time.time()); start = end - 600
    iso = lambda t: time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(t))
    c = get(f"https://api.exchange.coinbase.com/products/{p}/candles", {"granularity":60,"start":iso(start),"end":iso(end)})
    if isinstance(c, list) and c:
        print("CB", p, "rows", len(c), "newest candle t", c[0][0], "age s", end - c[0][0], "newest", c[0])
    else:
        print("CB", p, str(c)[:200])
