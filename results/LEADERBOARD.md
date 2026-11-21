# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 21, 4:30 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1042 windows, 28918 settled trades, 46 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 541 | 34.6 | 35.1 | $-305.47 | -5.6% | $694.53 | -1.0 | done | can't tell from luck |
| reversal_15m_0.10pct | 2934 | 51.2 | 50.5 | $-822.75 | -2.8% | $177.25 | -1.5 | done | can't tell from luck |
| value_ev10 | 1338 | 37.4 | 39.2 | $-1031.50 | -7.7% | $-31.50 | -2.3 | done | losing for real |
| momentum_60m_0.30pct | 2470 | 49.8 | 49.6 | $-1127.09 | -4.6% | $-127.09 | -2.3 | done | losing for real |
| trend_filter | 1727 | 49.3 | 50.7 | $-1356.95 | -7.9% | $-356.95 | -3.4 | done | losing for real |
| value_ev5 | 2024 | 39.3 | 41.0 | $-1473.37 | -7.3% | $-473.37 | -2.8 | done | losing for real |
| reversal_60m_0.30pct | 2470 | 50.2 | 51.0 | $-1610.82 | -6.5% | $-610.82 | -3.3 | done | losing for real |
| coinflip | 4160 | 50.5 | 50.3 | $-1684.32 | -4.0% | $-684.32 | -2.6 | done | losing for real |
| momentum_15m_0.10pct | 2934 | 48.8 | 50.3 | $-2032.31 | -6.9% | $-1032.31 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 4160 | 50.7 | 51.5 | $-2287.93 | -5.5% | $-1287.93 | -3.7 | done | losing for real |
| always_up | 4160 | 47.3 | 49.4 | $-3654.74 | -8.8% | $-2654.74 | -5.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6592 | 48.3 | 49.0 | $-3578.49 |
| ETH | 7162 | 48.1 | 48.5 | $-4475.22 |
| SOL | 7551 | 48.1 | 48.5 | $-4503.84 |
| XRP | 7613 | 48.1 | 48.3 | $-4829.70 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
