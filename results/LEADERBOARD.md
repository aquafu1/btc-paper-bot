# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 18, 3:30 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 702 windows, 19403 settled trades, 34 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 372 | 34.1 | 34.9 | $-244.03 | -6.6% | $755.97 | -0.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 1633 | 50.2 | 49.4 | $-511.28 | -3.1% | $488.72 | -1.3 | done | can't tell from luck |
| value_ev10 | 899 | 38.4 | 39.1 | $-513.27 | -5.7% | $486.73 | -1.4 | done | can't tell from luck |
| reversal_15m_0.10pct | 1992 | 51.6 | 50.8 | $-539.96 | -2.7% | $460.04 | -1.2 | done | can't tell from luck |
| value_ev5 | 1351 | 40.8 | 41.1 | $-618.49 | -4.6% | $381.51 | -1.4 | done | can't tell from luck |
| trend_filter | 1131 | 50.2 | 50.9 | $-634.55 | -5.6% | $365.45 | -1.9 | done | can't tell from luck |
| coinflip | 2800 | 50.2 | 50.3 | $-1196.58 | -4.3% | $-196.58 | -2.3 | done | losing for real |
| reversal_60m_0.30pct | 1633 | 49.8 | 51.4 | $-1230.27 | -7.5% | $-230.27 | -3.1 | done | losing for real |
| momentum_15m_0.10pct | 1992 | 48.4 | 50.0 | $-1405.24 | -7.1% | $-405.24 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 2800 | 50.9 | 51.8 | $-1493.31 | -5.3% | $-493.31 | -2.9 | done | losing for real |
| always_up | 2800 | 47.4 | 49.5 | $-2389.11 | -8.5% | $-1389.11 | -4.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4400 | 48.2 | 49.1 | $-2557.82 |
| ETH | 4828 | 48.3 | 48.5 | $-2763.34 |
| SOL | 5062 | 48.2 | 48.7 | $-2915.84 |
| XRP | 5113 | 48.5 | 48.4 | $-2539.10 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
