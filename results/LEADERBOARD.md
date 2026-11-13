# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 12, 11:20 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 205 windows, 5314 settled trades, 62 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 522 | 57.7 | 52.8 | $+309.19 | +5.9% | $1309.19 | +1.4 | done | can't tell from luck |
| reversal_60m_0.30pct | 404 | 56.2 | 53.0 | $+104.38 | +2.6% | $1104.38 | +0.6 | done | can't tell from luck |
| value_ev20 | 100 | 31.0 | 37.1 | $-224.01 | -22.4% | $775.99 | -1.9 | Sun 6:45 AM | too few trades (100/200) |
| momentum_5m_0.00pct | 812 | 50.9 | 51.3 | $-421.82 | -5.2% | $578.18 | -1.5 | done | can't tell from luck |
| trend_filter | 273 | 43.6 | 49.6 | $-427.28 | -15.7% | $572.72 | -2.6 | done | losing for real |
| coinflip | 812 | 50.5 | 51.0 | $-458.04 | -5.6% | $541.96 | -1.7 | done | can't tell from luck |
| value_ev10 | 265 | 35.5 | 41.0 | $-479.46 | -18.1% | $520.54 | -2.6 | done | losing for real |
| value_ev5 | 388 | 37.9 | 42.7 | $-610.98 | -15.7% | $389.02 | -2.8 | done | losing for real |
| momentum_60m_0.30pct | 404 | 43.8 | 49.3 | $-617.57 | -15.3% | $382.43 | -3.1 | done | losing for real |
| momentum_15m_0.10pct | 522 | 42.3 | 49.5 | $-948.95 | -18.2% | $51.05 | -4.2 | done | losing for real |
| always_up | 812 | 45.2 | 50.4 | $-1204.03 | -14.8% | $-204.03 | -4.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1178 | 45.9 | 49.7 | $-1308.51 |
| ETH | 1325 | 46.2 | 48.9 | $-1457.29 |
| SOL | 1374 | 47.4 | 49.3 | $-1338.52 |
| XRP | 1437 | 48.9 | 49.3 | $-874.25 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
