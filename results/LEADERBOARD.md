# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 21, 8:50 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1059 windows, 29310 settled trades, 41 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 547 | 34.6 | 35.1 | $-310.90 | -5.7% | $689.10 | -1.0 | done | can't tell from luck |
| reversal_15m_0.10pct | 2967 | 51.2 | 50.4 | $-779.81 | -2.6% | $220.19 | -1.4 | done | can't tell from luck |
| value_ev10 | 1357 | 37.7 | 39.2 | $-953.77 | -7.0% | $46.23 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 2488 | 49.6 | 49.6 | $-1192.80 | -4.8% | $-192.80 | -2.4 | done | losing for real |
| trend_filter | 1744 | 49.4 | 50.7 | $-1343.80 | -7.7% | $-343.80 | -3.3 | done | losing for real |
| value_ev5 | 2059 | 39.6 | 41.0 | $-1359.36 | -6.6% | $-359.36 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 2488 | 50.4 | 51.0 | $-1548.08 | -6.2% | $-548.08 | -3.2 | done | losing for real |
| coinflip | 4231 | 50.5 | 50.3 | $-1702.39 | -4.0% | $-702.39 | -2.6 | done | losing for real |
| momentum_15m_0.10pct | 2967 | 48.8 | 50.3 | $-2080.19 | -7.0% | $-1080.19 | -3.9 | done | losing for real |
| momentum_5m_0.00pct | 4231 | 50.8 | 51.5 | $-2220.72 | -5.2% | $-1220.72 | -3.5 | done | losing for real |
| always_up | 4231 | 47.3 | 49.4 | $-3701.17 | -8.7% | $-2701.17 | -5.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6680 | 48.4 | 49.0 | $-3443.28 |
| ETH | 7253 | 48.1 | 48.5 | $-4579.29 |
| SOL | 7651 | 48.0 | 48.5 | $-4505.38 |
| XRP | 7726 | 48.2 | 48.3 | $-4665.04 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
