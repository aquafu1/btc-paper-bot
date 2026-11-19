# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 19, 12:05 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 832 windows, 22880 settled trades, 43 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 422 | 33.2 | 34.9 | $-390.80 | -9.3% | $609.20 | -1.4 | done | can't tell from luck |
| reversal_15m_0.10pct | 2335 | 51.0 | 50.6 | $-806.25 | -3.5% | $193.75 | -1.7 | done | can't tell from luck |
| value_ev10 | 1045 | 37.3 | 39.1 | $-853.78 | -8.2% | $146.22 | -2.2 | done | losing for real |
| momentum_60m_0.30pct | 1922 | 49.9 | 49.6 | $-872.82 | -4.5% | $127.18 | -2.0 | done | losing for real |
| trend_filter | 1350 | 49.8 | 50.8 | $-963.91 | -7.1% | $36.09 | -2.7 | done | losing for real |
| value_ev5 | 1583 | 39.7 | 41.1 | $-1117.89 | -7.1% | $-117.89 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 1922 | 50.1 | 51.1 | $-1348.92 | -7.0% | $-348.92 | -3.2 | done | losing for real |
| coinflip | 3322 | 50.3 | 50.3 | $-1418.98 | -4.3% | $-418.98 | -2.5 | done | losing for real |
| momentum_15m_0.10pct | 2335 | 49.0 | 50.3 | $-1518.13 | -6.5% | $-518.13 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 3322 | 51.2 | 51.7 | $-1570.56 | -4.7% | $-570.56 | -2.8 | done | losing for real |
| always_up | 3322 | 47.3 | 49.6 | $-3002.33 | -9.0% | $-2002.33 | -5.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5205 | 48.1 | 49.1 | $-3264.79 |
| ETH | 5691 | 48.0 | 48.5 | $-3878.25 |
| SOL | 5972 | 48.3 | 48.6 | $-3456.82 |
| XRP | 6012 | 48.4 | 48.5 | $-3264.52 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
