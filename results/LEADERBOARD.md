# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 19, 2:05 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 840 windows, 23102 settled trades, 45 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 424 | 33.0 | 34.9 | $-410.80 | -9.7% | $589.20 | -1.5 | done | can't tell from luck |
| reversal_15m_0.10pct | 2360 | 50.9 | 50.6 | $-885.54 | -3.8% | $114.46 | -1.8 | done | can't tell from luck |
| value_ev10 | 1053 | 37.2 | 39.2 | $-890.49 | -8.5% | $109.51 | -2.2 | done | losing for real |
| momentum_60m_0.30pct | 1945 | 49.9 | 49.7 | $-896.57 | -4.6% | $103.43 | -2.0 | done | losing for real |
| trend_filter | 1357 | 49.7 | 50.8 | $-980.66 | -7.2% | $19.34 | -2.7 | done | losing for real |
| value_ev5 | 1596 | 39.6 | 41.1 | $-1163.03 | -7.3% | $-163.03 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 1945 | 50.1 | 51.1 | $-1383.75 | -7.1% | $-383.75 | -3.2 | done | losing for real |
| momentum_15m_0.10pct | 2360 | 49.1 | 50.3 | $-1487.51 | -6.3% | $-487.51 | -3.1 | done | losing for real |
| coinflip | 3354 | 50.2 | 50.3 | $-1504.73 | -4.5% | $-504.73 | -2.6 | done | losing for real |
| momentum_5m_0.00pct | 3354 | 51.2 | 51.7 | $-1625.28 | -4.8% | $-625.28 | -2.9 | done | losing for real |
| always_up | 3354 | 47.1 | 49.6 | $-3155.61 | -9.4% | $-2155.61 | -5.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5256 | 48.0 | 49.1 | $-3418.97 |
| ETH | 5756 | 48.0 | 48.5 | $-3991.16 |
| SOL | 6022 | 48.2 | 48.6 | $-3578.49 |
| XRP | 6068 | 48.4 | 48.5 | $-3395.35 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
