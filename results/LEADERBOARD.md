# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 21, 10:00 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1016 windows, 28288 settled trades, 67 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 520 | 34.0 | 35.0 | $-332.56 | -6.4% | $667.44 | -1.1 | done | can't tell from luck |
| reversal_15m_0.10pct | 2884 | 51.1 | 50.5 | $-859.89 | -3.0% | $140.11 | -1.6 | done | can't tell from luck |
| value_ev10 | 1293 | 37.2 | 39.1 | $-1022.99 | -7.9% | $-22.99 | -2.3 | done | losing for real |
| momentum_60m_0.30pct | 2440 | 50.0 | 49.7 | $-1023.06 | -4.2% | $-23.06 | -2.1 | done | losing for real |
| trend_filter | 1699 | 49.7 | 50.8 | $-1207.03 | -7.1% | $-207.03 | -3.0 | done | losing for real |
| value_ev5 | 1960 | 39.3 | 41.0 | $-1424.73 | -7.3% | $-424.73 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 2440 | 50.0 | 51.0 | $-1678.35 | -6.9% | $-678.35 | -3.5 | done | losing for real |
| coinflip | 4056 | 50.5 | 50.4 | $-1686.35 | -4.2% | $-686.35 | -2.7 | done | losing for real |
| momentum_15m_0.10pct | 2884 | 48.9 | 50.3 | $-1962.83 | -6.8% | $-962.83 | -3.7 | done | losing for real |
| momentum_5m_0.00pct | 4056 | 50.7 | 51.5 | $-2224.63 | -5.5% | $-1224.63 | -3.6 | done | losing for real |
| always_up | 4056 | 47.3 | 49.5 | $-3603.83 | -8.9% | $-2603.83 | -5.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6448 | 48.3 | 49.1 | $-3552.29 |
| ETH | 7029 | 48.0 | 48.5 | $-4499.25 |
| SOL | 7392 | 48.2 | 48.6 | $-4270.19 |
| XRP | 7419 | 48.1 | 48.4 | $-4704.52 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
