# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 21, 10:20 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1017 windows, 28330 settled trades, 54 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 524 | 34.5 | 35.1 | $-292.61 | -5.6% | $707.39 | -1.0 | done | can't tell from luck |
| reversal_15m_0.10pct | 2889 | 51.2 | 50.5 | $-829.94 | -2.9% | $170.06 | -1.5 | done | can't tell from luck |
| value_ev10 | 1298 | 37.4 | 39.2 | $-970.95 | -7.5% | $29.05 | -2.2 | done | losing for real |
| momentum_60m_0.30pct | 2441 | 50.0 | 49.6 | $-1010.96 | -4.1% | $-10.96 | -2.0 | done | losing for real |
| trend_filter | 1700 | 49.7 | 50.8 | $-1194.94 | -7.0% | $-194.94 | -3.0 | done | losing for real |
| value_ev5 | 1965 | 39.4 | 41.0 | $-1372.69 | -7.0% | $-372.69 | -2.6 | done | losing for real |
| coinflip | 4061 | 50.5 | 50.4 | $-1678.01 | -4.1% | $-678.01 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 2441 | 50.0 | 51.0 | $-1688.35 | -6.9% | $-688.35 | -3.5 | done | losing for real |
| momentum_15m_0.10pct | 2889 | 48.8 | 50.3 | $-1990.74 | -6.9% | $-990.74 | -3.7 | done | losing for real |
| momentum_5m_0.00pct | 4061 | 50.7 | 51.5 | $-2252.54 | -5.5% | $-1252.54 | -3.7 | done | losing for real |
| always_up | 4061 | 47.3 | 49.5 | $-3653.83 | -9.0% | $-2653.83 | -5.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6466 | 48.3 | 49.1 | $-3513.30 |
| ETH | 7037 | 48.1 | 48.5 | $-4480.96 |
| SOL | 7400 | 48.2 | 48.6 | $-4253.49 |
| XRP | 7427 | 48.1 | 48.4 | $-4687.82 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
