# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 17, 4:30 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 610 windows, 16852 settled trades, 49 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1424 | 51.2 | 49.7 | $-205.78 | -1.4% | $794.22 | -0.5 | done | can't tell from luck |
| value_ev20 | 327 | 34.3 | 35.2 | $-244.70 | -7.5% | $755.30 | -1.0 | done | can't tell from luck |
| value_ev10 | 784 | 38.3 | 39.4 | $-538.33 | -6.9% | $461.67 | -1.6 | done | can't tell from luck |
| trend_filter | 972 | 50.3 | 51.0 | $-545.89 | -5.6% | $454.11 | -1.8 | done | can't tell from luck |
| value_ev5 | 1181 | 40.5 | 41.3 | $-692.71 | -5.9% | $307.29 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 1722 | 50.7 | 50.9 | $-806.98 | -4.7% | $193.02 | -2.0 | done | can't tell from luck |
| momentum_15m_0.10pct | 1722 | 49.3 | 50.1 | $-952.66 | -5.5% | $47.34 | -2.3 | done | losing for real |
| coinflip | 2432 | 50.0 | 50.5 | $-1208.56 | -5.0% | $-208.56 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 1424 | 48.8 | 51.3 | $-1339.09 | -9.4% | $-339.09 | -3.6 | done | losing for real |
| momentum_5m_0.00pct | 2432 | 50.3 | 51.8 | $-1556.14 | -6.4% | $-556.14 | -3.3 | done | losing for real |
| always_up | 2432 | 47.0 | 49.8 | $-2332.27 | -9.6% | $-1332.27 | -4.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3831 | 48.0 | 49.2 | $-2512.14 |
| ETH | 4210 | 48.0 | 48.6 | $-2727.20 |
| SOL | 4378 | 47.9 | 48.8 | $-2899.35 |
| XRP | 4433 | 48.5 | 48.6 | $-2284.42 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
