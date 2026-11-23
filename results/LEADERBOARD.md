# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 23, 5:00 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1188 windows, 32832 settled trades, 47 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 640 | 35.0 | 35.3 | $-348.79 | -5.4% | $651.21 | -1.0 | done | can't tell from luck |
| value_ev10 | 1558 | 38.8 | 39.2 | $-729.21 | -4.7% | $270.79 | -1.5 | done | can't tell from luck |
| reversal_15m_0.10pct | 3287 | 50.8 | 50.3 | $-1067.61 | -3.2% | $-67.61 | -1.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 2763 | 49.6 | 49.4 | $-1212.74 | -4.4% | $-212.74 | -2.3 | done | losing for real |
| value_ev5 | 2360 | 40.4 | 41.1 | $-1221.94 | -5.2% | $-221.94 | -2.1 | done | losing for real |
| trend_filter | 1942 | 48.8 | 50.5 | $-1617.32 | -8.3% | $-617.32 | -3.8 | done | losing for real |
| reversal_60m_0.30pct | 2763 | 50.4 | 51.1 | $-1701.96 | -6.2% | $-701.96 | -3.3 | done | losing for real |
| momentum_15m_0.10pct | 3287 | 49.2 | 50.3 | $-2005.75 | -6.1% | $-1005.75 | -3.5 | done | losing for real |
| coinflip | 4744 | 50.1 | 50.2 | $-2127.51 | -4.5% | $-1127.51 | -3.1 | done | losing for real |
| momentum_5m_0.00pct | 4744 | 50.1 | 51.4 | $-3045.11 | -6.4% | $-2045.11 | -4.6 | done | losing for real |
| always_up | 4744 | 47.8 | 49.3 | $-3467.26 | -7.3% | $-2467.26 | -5.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7533 | 48.1 | 48.9 | $-4146.67 |
| ETH | 8139 | 48.0 | 48.4 | $-4960.10 |
| SOL | 8544 | 48.2 | 48.4 | $-4353.25 |
| XRP | 8616 | 48.1 | 48.2 | $-5085.17 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
