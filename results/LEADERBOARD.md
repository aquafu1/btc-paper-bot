# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 22, 6:20 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1097 windows, 30357 settled trades, 45 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 576 | 34.5 | 35.0 | $-338.75 | -5.9% | $661.25 | -1.1 | done | can't tell from luck |
| value_ev10 | 1409 | 38.1 | 39.1 | $-842.06 | -6.0% | $157.94 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 3064 | 51.0 | 50.5 | $-946.01 | -3.1% | $53.99 | -1.7 | done | can't tell from luck |
| momentum_60m_0.30pct | 2581 | 49.7 | 49.4 | $-1090.95 | -4.2% | $-90.95 | -2.1 | done | losing for real |
| value_ev5 | 2140 | 40.0 | 41.0 | $-1211.68 | -5.7% | $-211.68 | -2.2 | done | losing for real |
| trend_filter | 1799 | 49.4 | 50.5 | $-1317.14 | -7.3% | $-317.14 | -3.2 | done | losing for real |
| reversal_60m_0.30pct | 2581 | 50.3 | 51.1 | $-1662.59 | -6.4% | $-662.59 | -3.4 | done | losing for real |
| coinflip | 4381 | 50.5 | 50.2 | $-1680.72 | -3.8% | $-680.72 | -2.6 | done | losing for real |
| momentum_15m_0.10pct | 3064 | 49.0 | 50.2 | $-1948.77 | -6.4% | $-948.77 | -3.6 | done | losing for real |
| momentum_5m_0.00pct | 4381 | 50.8 | 51.4 | $-2241.03 | -5.1% | $-1241.03 | -3.5 | done | losing for real |
| always_up | 4381 | 47.5 | 49.3 | $-3509.99 | -8.0% | $-2509.99 | -5.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6951 | 48.5 | 49.0 | $-3362.75 |
| ETH | 7519 | 48.2 | 48.4 | $-4427.21 |
| SOL | 7903 | 48.1 | 48.4 | $-4420.59 |
| XRP | 7984 | 48.2 | 48.2 | $-4579.16 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
