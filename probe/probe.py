import json, time, urllib.request, urllib.parse
def get(url, params):
    url += "?" + urllib.parse.urlencode(params)
    with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent":"probe"}), timeout=20) as r:
        return json.loads(r.read().decode())
print("now", time.strftime("%H:%M:%S", time.gmtime()))
for coin in ["btc","eth","sol","xrp"]:
    e = get("https://gamma-api.polymarket.com/events", {"slug": f"{coin}-updown-15m-1794345300"})[0]
    m = e["markets"][0]
    print("EV", coin, {k: m.get(k) for k in ("closed","umaResolutionStatus","outcomePrices","closedTime","active","acceptingOrders")}, "| event closed", e.get("closed"), "| meta", e.get("eventMetadata"))
    ms = get("https://gamma-api.polymarket.com/markets", {"slug": f"{coin}-updown-15m-1794345300", "closed": "true"})
    print("MK", coin, {k: ms[0].get(k) for k in ("closed","umaResolutionStatus","outcomePrices","closedTime")} if ms else "not in closed=true list")
