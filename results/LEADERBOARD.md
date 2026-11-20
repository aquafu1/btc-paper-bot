# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 19, 10:00 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 872 windows, 24059 settled trades, 59 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 452 | 35.6 | 34.9 | $-106.41 | -2.4% | $893.59 | -0.4 | done | can't tell from luck |
| value_ev10 | 1102 | 38.4 | 39.1 | $-575.43 | -5.2% | $424.57 | -1.4 | done | can't tell from luck |
| momentum_60m_0.30pct | 2034 | 50.0 | 49.7 | $-853.10 | -4.2% | $146.90 | -1.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 2458 | 50.7 | 50.5 | $-915.57 | -3.7% | $84.43 | -1.8 | done | can't tell from luck |
| value_ev5 | 1665 | 40.1 | 41.0 | $-947.83 | -5.7% | $52.17 | -2.0 | done | can't tell from luck |
| trend_filter | 1416 | 49.9 | 51.0 | $-979.56 | -6.9% | $20.44 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 2034 | 50.0 | 51.0 | $-1375.81 | -6.8% | $-375.81 | -3.1 | done | losing for real |
| momentum_15m_0.10pct | 2458 | 49.3 | 50.4 | $-1438.00 | -5.9% | $-438.00 | -2.9 | done | losing for real |
| coinflip | 3480 | 50.1 | 50.3 | $-1536.55 | -4.4% | $-536.55 | -2.6 | done | losing for real |
| momentum_5m_0.00pct | 3480 | 51.2 | 51.7 | $-1653.73 | -4.8% | $-653.73 | -2.9 | done | losing for real |
| always_up | 3480 | 47.0 | 49.6 | $-3354.61 | -9.6% | $-2354.61 | -5.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5491 | 48.3 | 49.1 | $-2950.42 |
| ETH | 5982 | 48.1 | 48.5 | $-3813.53 |
| SOL | 6279 | 48.3 | 48.6 | $-3525.37 |
| XRP | 6307 | 48.4 | 48.5 | $-3447.27 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
