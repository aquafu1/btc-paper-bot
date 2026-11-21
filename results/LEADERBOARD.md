# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 21, 10:15 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1017 windows, 28320 settled trades, 64 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 524 | 34.5 | 35.1 | $-292.61 | -5.6% | $707.39 | -1.0 | done | can't tell from luck |
| reversal_15m_0.10pct | 2888 | 51.2 | 50.5 | $-819.94 | -2.8% | $180.06 | -1.5 | done | can't tell from luck |
| value_ev10 | 1297 | 37.4 | 39.2 | $-983.05 | -7.6% | $16.95 | -2.2 | done | losing for real |
| momentum_60m_0.30pct | 2440 | 50.0 | 49.7 | $-1023.06 | -4.2% | $-23.06 | -2.1 | done | losing for real |
| trend_filter | 1699 | 49.7 | 50.8 | $-1207.03 | -7.1% | $-207.03 | -3.0 | done | losing for real |
| value_ev5 | 1964 | 39.4 | 41.0 | $-1384.78 | -7.1% | $-384.78 | -2.6 | done | losing for real |
| coinflip | 4060 | 50.5 | 50.4 | $-1668.01 | -4.1% | $-668.01 | -2.6 | done | losing for real |
| reversal_60m_0.30pct | 2440 | 50.0 | 51.0 | $-1678.35 | -6.9% | $-678.35 | -3.5 | done | losing for real |
| momentum_15m_0.10pct | 2888 | 48.8 | 50.3 | $-2002.83 | -6.9% | $-1002.83 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 4060 | 50.7 | 51.5 | $-2264.63 | -5.6% | $-1264.63 | -3.7 | done | losing for real |
| always_up | 4060 | 47.3 | 49.5 | $-3643.83 | -9.0% | $-2643.83 | -5.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6456 | 48.3 | 49.1 | $-3545.85 |
| ETH | 7037 | 48.1 | 48.5 | $-4480.96 |
| SOL | 7400 | 48.2 | 48.6 | $-4253.49 |
| XRP | 7427 | 48.1 | 48.4 | $-4687.82 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
