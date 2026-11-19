# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 19, 4:00 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 848 windows, 23364 settled trades, 66 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 434 | 33.4 | 34.8 | $-357.48 | -8.2% | $642.52 | -1.3 | done | can't tell from luck |
| momentum_60m_0.30pct | 1973 | 50.3 | 49.7 | $-762.95 | -3.9% | $237.05 | -1.7 | done | can't tell from luck |
| value_ev10 | 1067 | 37.5 | 39.1 | $-813.87 | -7.6% | $186.13 | -2.0 | done | losing for real |
| trend_filter | 1378 | 50.2 | 50.9 | $-889.35 | -6.5% | $110.65 | -2.5 | done | losing for real |
| reversal_15m_0.10pct | 2387 | 50.7 | 50.5 | $-940.61 | -3.9% | $59.39 | -1.9 | done | can't tell from luck |
| value_ev5 | 1613 | 39.7 | 41.0 | $-1116.42 | -6.9% | $-116.42 | -2.4 | done | losing for real |
| momentum_15m_0.10pct | 2387 | 49.3 | 50.4 | $-1426.10 | -6.0% | $-426.10 | -2.9 | done | losing for real |
| reversal_60m_0.30pct | 1973 | 49.7 | 51.0 | $-1516.96 | -7.7% | $-516.96 | -3.5 | done | losing for real |
| coinflip | 3384 | 50.2 | 50.3 | $-1527.73 | -4.5% | $-527.73 | -2.6 | done | losing for real |
| momentum_5m_0.00pct | 3384 | 51.3 | 51.7 | $-1583.75 | -4.7% | $-583.75 | -2.8 | done | losing for real |
| always_up | 3384 | 46.9 | 49.5 | $-3308.82 | -9.8% | $-2308.82 | -5.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5319 | 48.1 | 49.1 | $-3190.57 |
| ETH | 5817 | 48.0 | 48.5 | $-3993.75 |
| SOL | 6092 | 48.2 | 48.5 | $-3683.60 |
| XRP | 6136 | 48.4 | 48.5 | $-3376.11 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
