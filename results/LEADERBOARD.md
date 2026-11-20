# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 19, 7:30 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 862 windows, 23746 settled trades, 46 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 445 | 34.6 | 34.8 | $-223.90 | -5.0% | $776.10 | -0.8 | done | can't tell from luck |
| value_ev10 | 1086 | 37.8 | 39.1 | $-732.23 | -6.7% | $267.77 | -1.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 2004 | 50.1 | 49.7 | $-797.52 | -4.0% | $202.48 | -1.8 | done | can't tell from luck |
| trend_filter | 1396 | 50.2 | 50.9 | $-882.46 | -6.3% | $117.54 | -2.4 | done | losing for real |
| reversal_15m_0.10pct | 2423 | 50.7 | 50.5 | $-931.78 | -3.8% | $68.22 | -1.9 | done | can't tell from luck |
| value_ev5 | 1645 | 39.8 | 41.0 | $-1064.63 | -6.5% | $-64.63 | -2.2 | done | losing for real |
| momentum_15m_0.10pct | 2423 | 49.3 | 50.4 | $-1434.15 | -5.9% | $-434.15 | -2.9 | done | losing for real |
| reversal_60m_0.30pct | 2004 | 49.9 | 51.0 | $-1470.01 | -7.3% | $-470.01 | -3.4 | done | losing for real |
| coinflip | 3440 | 50.1 | 50.3 | $-1594.72 | -4.6% | $-594.72 | -2.7 | done | losing for real |
| momentum_5m_0.00pct | 3440 | 51.2 | 51.7 | $-1623.19 | -4.7% | $-623.19 | -2.9 | done | losing for real |
| always_up | 3440 | 47.0 | 49.5 | $-3243.71 | -9.4% | $-2243.71 | -5.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5413 | 48.3 | 49.0 | $-2978.58 |
| ETH | 5909 | 48.0 | 48.5 | $-3916.43 |
| SOL | 6198 | 48.3 | 48.5 | $-3566.06 |
| XRP | 6226 | 48.3 | 48.5 | $-3537.23 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
