# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 19, 4:30 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 802 windows, 22050 settled trades, 45 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 409 | 33.7 | 34.9 | $-301.28 | -7.4% | $698.72 | -1.1 | done | can't tell from luck |
| value_ev10 | 1008 | 38.1 | 39.2 | $-614.51 | -6.1% | $385.49 | -1.6 | done | can't tell from luck |
| momentum_60m_0.30pct | 1855 | 50.1 | 49.6 | $-718.05 | -3.9% | $281.95 | -1.7 | done | can't tell from luck |
| trend_filter | 1293 | 50.1 | 50.8 | $-787.79 | -6.1% | $212.21 | -2.2 | done | losing for real |
| reversal_15m_0.10pct | 2255 | 51.0 | 50.6 | $-798.47 | -3.5% | $201.53 | -1.7 | done | can't tell from luck |
| value_ev5 | 1520 | 40.2 | 41.1 | $-840.23 | -5.5% | $159.77 | -1.8 | done | can't tell from luck |
| reversal_60m_0.30pct | 1855 | 49.9 | 51.2 | $-1323.97 | -7.1% | $-323.97 | -3.1 | done | losing for real |
| momentum_5m_0.00pct | 3200 | 51.3 | 51.6 | $-1346.61 | -4.2% | $-346.61 | -2.5 | done | losing for real |
| coinflip | 3200 | 50.2 | 50.3 | $-1359.79 | -4.2% | $-359.79 | -2.4 | done | losing for real |
| momentum_15m_0.10pct | 2255 | 49.0 | 50.2 | $-1374.85 | -6.1% | $-374.85 | -2.9 | done | losing for real |
| always_up | 3200 | 47.4 | 49.6 | $-2746.13 | -8.6% | $-1746.13 | -4.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5009 | 48.3 | 49.1 | $-2809.99 |
| ETH | 5497 | 48.2 | 48.5 | $-3421.38 |
| SOL | 5743 | 48.3 | 48.6 | $-3153.85 |
| XRP | 5801 | 48.5 | 48.5 | $-2826.46 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
