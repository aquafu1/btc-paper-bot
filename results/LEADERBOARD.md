# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 19, 4:05 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 800 windows, 22033 settled trades, 17 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 409 | 33.7 | 34.9 | $-301.28 | -7.4% | $698.72 | -1.1 | done | can't tell from luck |
| value_ev10 | 1007 | 38.0 | 39.1 | $-623.44 | -6.2% | $376.56 | -1.6 | done | can't tell from luck |
| momentum_60m_0.30pct | 1855 | 50.1 | 49.6 | $-718.05 | -3.9% | $281.95 | -1.7 | done | can't tell from luck |
| trend_filter | 1293 | 50.1 | 50.8 | $-787.79 | -6.1% | $212.21 | -2.2 | done | losing for real |
| reversal_15m_0.10pct | 2254 | 51.0 | 50.6 | $-788.47 | -3.5% | $211.53 | -1.7 | done | can't tell from luck |
| value_ev5 | 1518 | 40.2 | 41.1 | $-839.17 | -5.5% | $160.83 | -1.8 | done | can't tell from luck |
| reversal_60m_0.30pct | 1855 | 49.9 | 51.2 | $-1323.97 | -7.1% | $-323.97 | -3.1 | done | losing for real |
| coinflip | 3196 | 50.3 | 50.3 | $-1335.49 | -4.2% | $-335.49 | -2.4 | done | losing for real |
| momentum_5m_0.00pct | 3196 | 51.3 | 51.6 | $-1378.25 | -4.3% | $-378.25 | -2.5 | done | losing for real |
| momentum_15m_0.10pct | 2254 | 49.0 | 50.2 | $-1380.55 | -6.1% | $-380.55 | -2.9 | done | losing for real |
| always_up | 3196 | 47.5 | 49.6 | $-2725.07 | -8.5% | $-1725.07 | -4.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5005 | 48.4 | 49.1 | $-2787.01 |
| ETH | 5492 | 48.2 | 48.5 | $-3447.12 |
| SOL | 5740 | 48.3 | 48.6 | $-3143.84 |
| XRP | 5796 | 48.5 | 48.5 | $-2823.56 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
