# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 15, 5:50 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 423 windows, 11649 settled trades, 28 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 210 | 34.8 | 36.4 | $-166.95 | -8.0% | $833.05 | -0.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 997 | 50.6 | 50.0 | $-316.33 | -3.2% | $683.67 | -1.0 | done | can't tell from luck |
| value_ev10 | 543 | 39.2 | 40.4 | $-351.49 | -6.5% | $648.51 | -1.3 | done | can't tell from luck |
| trend_filter | 667 | 49.5 | 50.7 | $-438.88 | -6.6% | $561.12 | -1.7 | done | can't tell from luck |
| value_ev5 | 816 | 41.3 | 42.1 | $-468.73 | -5.7% | $531.27 | -1.4 | done | can't tell from luck |
| momentum_15m_0.10pct | 1179 | 49.1 | 50.0 | $-635.30 | -5.4% | $364.70 | -1.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 1179 | 50.9 | 51.8 | $-696.13 | -5.9% | $303.87 | -2.1 | done | losing for real |
| coinflip | 1687 | 50.5 | 51.0 | $-774.61 | -4.6% | $225.39 | -1.9 | done | can't tell from luck |
| reversal_60m_0.30pct | 997 | 49.4 | 51.9 | $-867.56 | -8.7% | $132.44 | -2.9 | done | losing for real |
| momentum_5m_0.00pct | 1687 | 49.5 | 51.6 | $-1279.76 | -7.6% | $-279.76 | -3.2 | done | losing for real |
| always_up | 1687 | 46.1 | 50.7 | $-2121.44 | -12.6% | $-1121.44 | -5.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2642 | 47.7 | 49.4 | $-1946.13 |
| ETH | 2921 | 47.9 | 49.0 | $-1868.03 |
| SOL | 3019 | 47.7 | 49.5 | $-2536.35 |
| XRP | 3067 | 48.7 | 49.3 | $-1766.69 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
