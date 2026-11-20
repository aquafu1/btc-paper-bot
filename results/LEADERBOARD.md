# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 19, 11:35 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 878 windows, 24252 settled trades, 45 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 457 | 35.9 | 34.9 | $-59.37 | -1.3% | $940.63 | -0.2 | done | can't tell from luck |
| value_ev10 | 1111 | 38.5 | 39.1 | $-524.76 | -4.7% | $475.24 | -1.3 | done | can't tell from luck |
| momentum_60m_0.30pct | 2052 | 50.1 | 49.8 | $-829.16 | -4.0% | $170.84 | -1.8 | done | can't tell from luck |
| trend_filter | 1429 | 50.2 | 51.0 | $-920.43 | -6.4% | $79.57 | -2.5 | done | losing for real |
| value_ev5 | 1679 | 40.1 | 41.0 | $-921.98 | -5.5% | $78.02 | -1.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 2477 | 50.5 | 50.4 | $-984.09 | -4.0% | $15.91 | -2.0 | done | can't tell from luck |
| momentum_15m_0.10pct | 2477 | 49.5 | 50.4 | $-1378.53 | -5.6% | $-378.53 | -2.8 | done | losing for real |
| reversal_60m_0.30pct | 2052 | 49.9 | 50.9 | $-1407.77 | -6.9% | $-407.77 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 3506 | 51.3 | 51.7 | $-1562.41 | -4.5% | $-562.41 | -2.7 | done | losing for real |
| coinflip | 3506 | 50.1 | 50.3 | $-1578.70 | -4.5% | $-578.70 | -2.7 | done | losing for real |
| always_up | 3506 | 46.9 | 49.6 | $-3427.72 | -9.8% | $-2427.72 | -5.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5538 | 48.3 | 49.1 | $-2977.61 |
| ETH | 6037 | 48.2 | 48.5 | $-3702.36 |
| SOL | 6326 | 48.3 | 48.5 | $-3538.73 |
| XRP | 6351 | 48.4 | 48.5 | $-3376.22 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
