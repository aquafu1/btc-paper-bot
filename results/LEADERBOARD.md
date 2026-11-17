# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 17, 4:00 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 608 windows, 16803 settled trades, 49 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1421 | 51.2 | 49.7 | $-213.71 | -1.5% | $786.29 | -0.6 | done | can't tell from luck |
| value_ev20 | 327 | 34.3 | 35.2 | $-244.70 | -7.5% | $755.30 | -1.0 | done | can't tell from luck |
| value_ev10 | 784 | 38.3 | 39.4 | $-538.33 | -6.9% | $461.67 | -1.6 | done | can't tell from luck |
| trend_filter | 969 | 50.3 | 51.0 | $-553.82 | -5.7% | $446.18 | -1.8 | done | can't tell from luck |
| value_ev5 | 1179 | 40.5 | 41.3 | $-692.39 | -5.9% | $307.61 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 1715 | 50.7 | 50.9 | $-788.65 | -4.6% | $211.35 | -1.9 | done | can't tell from luck |
| momentum_15m_0.10pct | 1715 | 49.3 | 50.1 | $-951.47 | -5.5% | $48.53 | -2.3 | done | losing for real |
| coinflip | 2424 | 49.9 | 50.5 | $-1235.82 | -5.1% | $-235.82 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 1421 | 48.8 | 51.3 | $-1324.62 | -9.3% | $-324.62 | -3.6 | done | losing for real |
| momentum_5m_0.00pct | 2424 | 50.3 | 51.8 | $-1564.85 | -6.5% | $-564.85 | -3.3 | done | losing for real |
| always_up | 2424 | 47.1 | 49.8 | $-2285.83 | -9.4% | $-1285.83 | -4.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3823 | 48.0 | 49.2 | $-2519.69 |
| ETH | 4193 | 47.9 | 48.6 | $-2766.51 |
| SOL | 4366 | 47.9 | 48.7 | $-2878.74 |
| XRP | 4421 | 48.5 | 48.6 | $-2229.24 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
