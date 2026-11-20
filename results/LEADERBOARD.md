# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 20, 8:35 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 914 windows, 25240 settled trades, 47 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 472 | 35.0 | 34.8 | $-181.30 | -3.8% | $818.70 | -0.6 | done | can't tell from luck |
| value_ev10 | 1156 | 38.1 | 39.1 | $-668.14 | -5.8% | $331.86 | -1.6 | done | can't tell from luck |
| momentum_60m_0.30pct | 2139 | 50.1 | 49.9 | $-925.23 | -4.3% | $74.77 | -2.0 | done | losing for real |
| trend_filter | 1499 | 50.0 | 51.0 | $-998.52 | -6.7% | $1.48 | -2.7 | done | losing for real |
| reversal_15m_0.10pct | 2568 | 50.5 | 50.5 | $-1088.38 | -4.2% | $-88.38 | -2.2 | done | losing for real |
| value_ev5 | 1749 | 39.7 | 41.0 | $-1112.52 | -6.4% | $-112.52 | -2.2 | done | losing for real |
| momentum_15m_0.10pct | 2568 | 49.5 | 50.3 | $-1370.53 | -5.3% | $-370.53 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 2139 | 49.9 | 50.8 | $-1444.99 | -6.8% | $-444.99 | -3.2 | done | losing for real |
| coinflip | 3650 | 50.3 | 50.3 | $-1544.05 | -4.2% | $-544.05 | -2.6 | done | losing for real |
| momentum_5m_0.00pct | 3650 | 51.1 | 51.6 | $-1718.69 | -4.7% | $-718.69 | -2.9 | done | losing for real |
| always_up | 3650 | 46.8 | 49.7 | $-3639.68 | -10.0% | $-2639.68 | -6.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5751 | 48.2 | 49.1 | $-3257.58 |
| ETH | 6279 | 48.2 | 48.5 | $-3868.97 |
| SOL | 6583 | 48.1 | 48.6 | $-3846.02 |
| XRP | 6627 | 48.3 | 48.5 | $-3719.45 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
