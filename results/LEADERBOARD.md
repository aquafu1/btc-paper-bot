# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 15, 6:05 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 424 windows, 11665 settled trades, 50 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 210 | 34.8 | 36.4 | $-166.95 | -8.0% | $833.05 | -0.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 998 | 50.5 | 50.0 | $-326.33 | -3.3% | $673.67 | -1.0 | done | can't tell from luck |
| value_ev10 | 543 | 39.2 | 40.4 | $-351.49 | -6.5% | $648.51 | -1.3 | done | can't tell from luck |
| trend_filter | 667 | 49.5 | 50.7 | $-438.88 | -6.6% | $561.12 | -1.7 | done | can't tell from luck |
| value_ev5 | 817 | 41.2 | 42.1 | $-478.73 | -5.9% | $521.27 | -1.5 | done | can't tell from luck |
| momentum_15m_0.10pct | 1181 | 49.1 | 50.0 | $-636.00 | -5.4% | $364.00 | -1.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 1181 | 50.9 | 51.8 | $-700.19 | -5.9% | $299.81 | -2.1 | done | losing for real |
| coinflip | 1690 | 50.5 | 51.0 | $-769.37 | -4.6% | $230.63 | -1.9 | done | can't tell from luck |
| reversal_60m_0.30pct | 998 | 49.5 | 51.9 | $-861.62 | -8.6% | $138.38 | -2.9 | done | losing for real |
| momentum_5m_0.00pct | 1690 | 49.5 | 51.6 | $-1293.81 | -7.7% | $-293.81 | -3.3 | done | losing for real |
| always_up | 1690 | 46.1 | 50.7 | $-2132.14 | -12.6% | $-1132.14 | -5.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2645 | 47.6 | 49.4 | $-1976.13 |
| ETH | 2926 | 47.9 | 49.0 | $-1860.13 |
| SOL | 3019 | 47.7 | 49.5 | $-2536.35 |
| XRP | 3075 | 48.7 | 49.3 | $-1782.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
