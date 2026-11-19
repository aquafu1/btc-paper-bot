# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 19, 12:00 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 832 windows, 22866 settled trades, 57 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 422 | 33.2 | 34.9 | $-390.80 | -9.3% | $609.20 | -1.4 | done | can't tell from luck |
| reversal_15m_0.10pct | 2334 | 51.1 | 50.6 | $-796.25 | -3.4% | $203.75 | -1.7 | done | can't tell from luck |
| value_ev10 | 1044 | 37.4 | 39.1 | $-843.78 | -8.1% | $156.22 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 1921 | 49.9 | 49.6 | $-879.55 | -4.6% | $120.45 | -2.0 | done | losing for real |
| trend_filter | 1349 | 49.7 | 50.8 | $-970.64 | -7.2% | $29.36 | -2.7 | done | losing for real |
| value_ev5 | 1581 | 39.7 | 41.1 | $-1097.89 | -6.9% | $-97.89 | -2.3 | done | losing for real |
| reversal_60m_0.30pct | 1921 | 50.1 | 51.1 | $-1338.92 | -7.0% | $-338.92 | -3.1 | done | losing for real |
| coinflip | 3320 | 50.3 | 50.3 | $-1432.26 | -4.3% | $-432.26 | -2.5 | done | losing for real |
| momentum_15m_0.10pct | 2334 | 48.9 | 50.3 | $-1524.87 | -6.5% | $-524.87 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 3320 | 51.2 | 51.6 | $-1583.84 | -4.8% | $-583.84 | -2.8 | done | losing for real |
| always_up | 3320 | 47.3 | 49.6 | $-2982.33 | -9.0% | $-1982.33 | -5.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5195 | 48.1 | 49.1 | $-3248.46 |
| ETH | 5691 | 48.0 | 48.5 | $-3878.25 |
| SOL | 5968 | 48.3 | 48.6 | $-3449.90 |
| XRP | 6012 | 48.4 | 48.5 | $-3264.52 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
