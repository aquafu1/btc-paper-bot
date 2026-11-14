# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 13, 10:15 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 297 windows, 7900 settled trades, 67 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 147 | 35.4 | 36.4 | $-124.69 | -8.5% | $875.31 | -0.8 | Sun 2:30 AM | too few trades (147/200) |
| reversal_15m_0.10pct | 784 | 53.3 | 51.9 | $-128.54 | -1.6% | $871.46 | -0.5 | done | can't tell from luck |
| reversal_60m_0.30pct | 638 | 51.9 | 51.9 | $-283.99 | -4.5% | $716.01 | -1.2 | done | can't tell from luck |
| value_ev10 | 381 | 38.3 | 40.4 | $-361.07 | -9.5% | $638.93 | -1.6 | done | can't tell from luck |
| trend_filter | 428 | 47.0 | 50.2 | $-480.60 | -11.2% | $519.40 | -2.4 | done | losing for real |
| momentum_60m_0.30pct | 638 | 48.1 | 49.8 | $-531.58 | -8.3% | $468.42 | -2.1 | done | losing for real |
| value_ev5 | 560 | 40.0 | 42.1 | $-532.32 | -9.5% | $467.68 | -2.0 | done | can't tell from luck |
| coinflip | 1180 | 50.3 | 50.9 | $-634.90 | -5.4% | $365.10 | -1.9 | done | can't tell from luck |
| momentum_15m_0.10pct | 784 | 46.7 | 49.9 | $-825.92 | -10.5% | $174.08 | -3.0 | done | losing for real |
| momentum_5m_0.00pct | 1180 | 49.4 | 51.3 | $-933.87 | -7.9% | $66.13 | -2.8 | done | losing for real |
| always_up | 1180 | 46.9 | 50.3 | $-1277.78 | -10.8% | $-277.78 | -3.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1763 | 46.7 | 49.3 | $-1650.11 |
| ETH | 1977 | 47.3 | 48.7 | $-1756.91 |
| SOL | 2053 | 48.3 | 49.3 | $-1558.47 |
| XRP | 2107 | 48.6 | 49.0 | $-1149.77 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
