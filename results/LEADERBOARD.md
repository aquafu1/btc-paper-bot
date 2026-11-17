# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 17, 2:30 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 650 windows, 17955 settled trades, 63 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 338 | 34.6 | 35.3 | $-217.49 | -6.4% | $782.51 | -0.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 1514 | 50.6 | 49.6 | $-353.18 | -2.3% | $646.82 | -0.9 | done | can't tell from luck |
| value_ev10 | 828 | 38.5 | 39.5 | $-540.22 | -6.5% | $459.78 | -1.5 | done | can't tell from luck |
| reversal_15m_0.10pct | 1846 | 51.5 | 51.0 | $-564.73 | -3.1% | $435.27 | -1.3 | done | can't tell from luck |
| value_ev5 | 1254 | 41.1 | 41.4 | $-595.58 | -4.7% | $404.42 | -1.4 | done | can't tell from luck |
| trend_filter | 1039 | 50.0 | 50.9 | $-628.38 | -6.0% | $371.62 | -2.0 | done | can't tell from luck |
| coinflip | 2592 | 50.1 | 50.5 | $-1180.08 | -4.6% | $-180.08 | -2.3 | done | losing for real |
| reversal_60m_0.30pct | 1514 | 49.4 | 51.4 | $-1241.98 | -8.2% | $-241.98 | -3.3 | done | losing for real |
| momentum_15m_0.10pct | 1846 | 48.5 | 50.0 | $-1255.75 | -6.8% | $-255.75 | -2.9 | done | losing for real |
| momentum_5m_0.00pct | 2592 | 50.4 | 51.7 | $-1541.87 | -5.9% | $-541.87 | -3.1 | done | losing for real |
| always_up | 2592 | 47.4 | 49.7 | $-2198.04 | -8.5% | $-1198.04 | -4.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4070 | 48.3 | 49.3 | $-2438.91 |
| ETH | 4483 | 48.2 | 48.7 | $-2681.99 |
| SOL | 4673 | 48.0 | 48.8 | $-2864.92 |
| XRP | 4729 | 48.5 | 48.6 | $-2331.48 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
