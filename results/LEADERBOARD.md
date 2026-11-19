# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 19, 8:45 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 819 windows, 22463 settled trades, 56 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 413 | 33.4 | 35.0 | $-341.28 | -8.3% | $658.72 | -1.3 | done | can't tell from luck |
| value_ev10 | 1025 | 37.8 | 39.2 | $-717.11 | -7.0% | $282.89 | -1.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 1878 | 50.0 | 49.6 | $-765.45 | -4.1% | $234.55 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 2298 | 50.8 | 50.6 | $-871.34 | -3.8% | $128.66 | -1.8 | done | can't tell from luck |
| trend_filter | 1318 | 49.9 | 50.9 | $-872.84 | -6.6% | $127.16 | -2.5 | done | losing for real |
| value_ev5 | 1551 | 40.0 | 41.1 | $-941.29 | -6.1% | $58.71 | -2.0 | done | losing for real |
| reversal_60m_0.30pct | 1878 | 50.0 | 51.2 | $-1322.99 | -7.0% | $-322.99 | -3.1 | done | losing for real |
| momentum_15m_0.10pct | 2298 | 49.2 | 50.2 | $-1362.67 | -5.9% | $-362.67 | -2.9 | done | losing for real |
| coinflip | 3268 | 50.1 | 50.3 | $-1480.24 | -4.5% | $-480.24 | -2.6 | done | losing for real |
| momentum_5m_0.00pct | 3268 | 51.2 | 51.7 | $-1480.90 | -4.5% | $-480.90 | -2.7 | done | losing for real |
| always_up | 3268 | 47.5 | 49.6 | $-2832.39 | -8.7% | $-1832.39 | -5.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5096 | 48.2 | 49.1 | $-3046.10 |
| ETH | 5591 | 48.1 | 48.6 | $-3611.41 |
| SOL | 5859 | 48.3 | 48.6 | $-3234.68 |
| XRP | 5917 | 48.4 | 48.5 | $-3096.31 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
