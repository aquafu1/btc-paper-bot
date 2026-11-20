# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 19, 8:00 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 864 windows, 23792 settled trades, 60 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 445 | 34.6 | 34.8 | $-223.90 | -5.0% | $776.10 | -0.8 | done | can't tell from luck |
| value_ev10 | 1087 | 37.8 | 39.1 | $-721.42 | -6.6% | $278.58 | -1.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 2008 | 50.1 | 49.7 | $-816.71 | -4.1% | $183.29 | -1.8 | done | can't tell from luck |
| trend_filter | 1396 | 50.2 | 50.9 | $-882.46 | -6.3% | $117.54 | -2.4 | done | losing for real |
| reversal_15m_0.10pct | 2428 | 50.7 | 50.5 | $-928.59 | -3.8% | $71.41 | -1.9 | done | can't tell from luck |
| value_ev5 | 1648 | 39.7 | 41.0 | $-1073.81 | -6.5% | $-73.81 | -2.2 | done | losing for real |
| momentum_15m_0.10pct | 2428 | 49.3 | 50.4 | $-1437.13 | -5.9% | $-437.13 | -2.9 | done | losing for real |
| reversal_60m_0.30pct | 2008 | 49.9 | 51.0 | $-1442.50 | -7.2% | $-442.50 | -3.3 | done | losing for real |
| momentum_5m_0.00pct | 3448 | 51.3 | 51.7 | $-1547.74 | -4.5% | $-547.74 | -2.7 | done | losing for real |
| coinflip | 3448 | 50.1 | 50.3 | $-1578.75 | -4.6% | $-578.75 | -2.7 | done | losing for real |
| always_up | 3448 | 47.0 | 49.6 | $-3302.90 | -9.6% | $-2302.90 | -5.6 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5426 | 48.3 | 49.0 | $-2986.50 |
| ETH | 5918 | 48.0 | 48.5 | $-3917.01 |
| SOL | 6208 | 48.3 | 48.5 | $-3553.39 |
| XRP | 6240 | 48.3 | 48.5 | $-3499.02 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
