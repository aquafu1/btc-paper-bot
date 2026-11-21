# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 20, 9:50 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 967 windows, 26807 settled trades, 55 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 496 | 34.7 | 34.8 | $-219.50 | -4.4% | $780.50 | -0.7 | done | can't tell from luck |
| value_ev10 | 1224 | 38.0 | 39.1 | $-719.05 | -5.9% | $280.95 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 2736 | 51.3 | 50.5 | $-727.56 | -2.7% | $272.44 | -1.4 | done | can't tell from luck |
| momentum_60m_0.30pct | 2286 | 50.2 | 49.8 | $-875.08 | -3.8% | $124.92 | -1.8 | done | can't tell from luck |
| trend_filter | 1602 | 50.0 | 50.9 | $-1059.18 | -6.6% | $-59.18 | -2.7 | done | losing for real |
| value_ev5 | 1855 | 39.8 | 41.0 | $-1092.06 | -5.9% | $-92.06 | -2.1 | done | losing for real |
| reversal_60m_0.30pct | 2286 | 49.8 | 50.9 | $-1639.74 | -7.2% | $-639.74 | -3.5 | done | losing for real |
| coinflip | 3862 | 50.2 | 50.3 | $-1757.17 | -4.5% | $-757.17 | -2.9 | done | losing for real |
| momentum_15m_0.10pct | 2736 | 48.7 | 50.3 | $-1941.31 | -7.1% | $-941.31 | -3.7 | done | losing for real |
| momentum_5m_0.00pct | 3862 | 50.9 | 51.6 | $-2002.15 | -5.2% | $-1002.15 | -3.3 | done | losing for real |
| always_up | 3862 | 46.8 | 49.6 | $-3829.88 | -9.9% | $-2829.88 | -6.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6102 | 48.2 | 49.1 | $-3489.91 |
| ETH | 6665 | 48.1 | 48.5 | $-4187.09 |
| SOL | 6996 | 48.2 | 48.6 | $-3827.68 |
| XRP | 7044 | 48.2 | 48.4 | $-4358.01 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
