# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 19, 11:50 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 831 windows, 22858 settled trades, 43 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 422 | 33.2 | 34.9 | $-390.80 | -9.3% | $609.20 | -1.4 | done | can't tell from luck |
| reversal_15m_0.10pct | 2333 | 51.1 | 50.6 | $-786.25 | -3.4% | $213.75 | -1.6 | done | can't tell from luck |
| value_ev10 | 1044 | 37.4 | 39.1 | $-843.78 | -8.1% | $156.22 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 1920 | 49.8 | 49.6 | $-886.86 | -4.6% | $113.14 | -2.0 | done | losing for real |
| trend_filter | 1348 | 49.7 | 50.8 | $-977.95 | -7.3% | $22.05 | -2.7 | done | losing for real |
| value_ev5 | 1581 | 39.7 | 41.1 | $-1097.89 | -6.9% | $-97.89 | -2.3 | done | losing for real |
| reversal_60m_0.30pct | 1920 | 50.2 | 51.2 | $-1328.92 | -6.9% | $-328.92 | -3.1 | done | losing for real |
| coinflip | 3319 | 50.3 | 50.3 | $-1422.26 | -4.3% | $-422.26 | -2.5 | done | losing for real |
| momentum_15m_0.10pct | 2333 | 48.9 | 50.3 | $-1532.17 | -6.6% | $-532.17 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 3319 | 51.2 | 51.6 | $-1591.14 | -4.8% | $-591.14 | -2.9 | done | losing for real |
| always_up | 3319 | 47.3 | 49.6 | $-2989.63 | -9.0% | $-1989.63 | -5.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5195 | 48.1 | 49.1 | $-3248.46 |
| ETH | 5691 | 48.0 | 48.5 | $-3878.25 |
| SOL | 5960 | 48.2 | 48.6 | $-3456.44 |
| XRP | 6012 | 48.4 | 48.5 | $-3264.52 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
