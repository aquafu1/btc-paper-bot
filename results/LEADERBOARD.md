# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 15, 9:00 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 484 windows, 13302 settled trades, 63 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 245 | 34.7 | 35.8 | $-152.29 | -6.2% | $847.71 | -0.7 | done | can't tell from luck |
| momentum_60m_0.30pct | 1129 | 50.8 | 49.7 | $-213.09 | -1.9% | $786.91 | -0.6 | done | can't tell from luck |
| value_ev10 | 626 | 39.0 | 40.1 | $-363.65 | -5.8% | $636.35 | -1.2 | done | can't tell from luck |
| momentum_15m_0.10pct | 1343 | 50.1 | 49.9 | $-426.29 | -3.2% | $573.71 | -1.2 | done | can't tell from luck |
| value_ev5 | 924 | 41.0 | 41.8 | $-479.82 | -5.2% | $520.18 | -1.3 | done | can't tell from luck |
| trend_filter | 779 | 49.3 | 50.6 | $-533.93 | -6.9% | $466.07 | -2.0 | done | can't tell from luck |
| reversal_15m_0.10pct | 1343 | 49.9 | 51.5 | $-965.52 | -7.2% | $34.48 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 1129 | 49.2 | 51.6 | $-1001.05 | -8.9% | $-1.05 | -3.1 | done | losing for real |
| coinflip | 1928 | 49.9 | 50.8 | $-1022.08 | -5.3% | $-22.08 | -2.4 | done | losing for real |
| momentum_5m_0.00pct | 1928 | 49.5 | 51.7 | $-1457.24 | -7.6% | $-457.24 | -3.4 | done | losing for real |
| always_up | 1928 | 46.4 | 50.4 | $-2253.30 | -11.7% | $-1253.30 | -5.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3002 | 47.4 | 49.3 | $-2392.74 |
| ETH | 3334 | 48.1 | 48.8 | $-2142.93 |
| SOL | 3463 | 47.7 | 49.3 | $-2503.68 |
| XRP | 3503 | 48.5 | 49.0 | $-1828.93 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
