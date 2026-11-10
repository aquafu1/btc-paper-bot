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
print("now", now, "ws", ws, "into", now - ws)
def m_closed(slug):
    m = get("https://gamma-api.polymarket.com/markets", {"slug": slug, "closed": "true"})
    return m[0] if isinstance(m, list) and m else m
for w, ours in [(1794245400,"Down"),(1794246300,"Up"),(1794271500,"Up"),(1794296700,"Down")]:
    m = m_closed(f"btc-updown-15m-{w}")
    print("OLD", w, "ours", ours, "|", {k: m.get(k) for k in ("closed","outcomes","outcomePrices","umaResolutionStatus","umaResolutionStatuses","closedTime","automaticallyResolved")} if isinstance(m, dict) else m)
m = m_closed(f"btc-updown-15m-{ws-3600}")
if isinstance(m, dict):
    print("KEYS", sorted(m.keys()))
    for k in ["question","endDate","closedTime","resolutionSource","feesEnabled","feeType","umaResolutionStatus","automaticallyResolved","eventStartTime","startDate"]:
        print("  ", k, "=", m.get(k))
    print("  description:", (m.get("description") or "")[:700])
ev = get("https://gamma-api.polymarket.com/events", {"slug": f"btc-updown-15m-{ws-3600}"})
print("EVENTS no-closed-param:", "found" if isinstance(ev, list) and ev else ev)
if isinstance(ev, list) and ev:
    e = ev[0]; mk = e.get("markets", [{}])[0]
    print("  event closed", e.get("closed"), "market outcomePrices", mk.get("outcomePrices"), "eventMetadata", str(e.get("eventMetadata"))[:300])
for back in (900, 1800):
    for coin in ["btc","eth","sol","xrp"]:
        m = m_closed(f"{coin}-updown-15m-{ws-back}")
        print("ENDED", back//60, "min ago", coin, {k: m.get(k) for k in ("closed","outcomePrices","umaResolutionStatus","closedTime")} if isinstance(m, dict) else m)
    m = get("https://gamma-api.polymarket.com/markets", {"slug": f"btc-updown-15m-{ws-back}"})
    print("  same btc WITHOUT closed param ->", "found" if isinstance(m, list) and m else m)
# market for a window starting in 30 min: does it exist yet?
for ahead in (1800, 3600):
    m = get("https://gamma-api.polymarket.com/markets", {"slug": f"btc-updown-15m-{ws+ahead}"})
    print("AHEAD", ahead//60, "min:", "exists" if isinstance(m, list) and m else m)
