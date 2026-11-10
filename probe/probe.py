import json, time, urllib.request, urllib.parse
UA={"User-Agent":"btc-paper-bot/1.0 probe"}
def get(url, params=None):
    if params: url += "?" + urllib.parse.urlencode(params)
    with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=20) as r:
        return json.loads(r.read().decode())
ws = int(time.time()) // 900 * 900
for coin in ["btc","eth","sol","xrp"]:
    e = get("https://gamma-api.polymarket.com/events", {"slug": f"{coin}-updown-15m-{ws+900}"})[0]
    m = e["markets"][0]
    print("FEE", coin, "feeSchedule=", m.get("feeSchedule"), "| feeType=", m.get("feeType"), "| takerBaseFee=", m.get("takerBaseFee"), "| makerBaseFee=", m.get("makerBaseFee"))
    print("CFG", coin, str(m.get("cryptoMarketConfig"))[:300], "| eventMetadata", e.get("eventMetadata"), "| resolutionSource", m.get("resolutionSource"))
