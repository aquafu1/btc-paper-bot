# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 14, 5:45 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 375 windows, 10189 settled trades, 56 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 195 | 37.4 | 36.5 | $-16.95 | -0.9% | $983.05 | -0.1 | Sat 8:15 PM | too few trades (195/200) |
| value_ev10 | 497 | 40.2 | 40.4 | $-179.12 | -3.6% | $820.88 | -0.7 | done | can't tell from luck |
| value_ev5 | 733 | 41.9 | 42.1 | $-292.45 | -4.0% | $707.55 | -0.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 847 | 49.8 | 49.7 | $-360.16 | -4.3% | $639.84 | -1.2 | done | can't tell from luck |
| trend_filter | 562 | 48.9 | 50.4 | $-420.47 | -7.5% | $579.53 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 1016 | 51.7 | 52.2 | $-505.24 | -5.0% | $494.76 | -1.7 | done | can't tell from luck |
| momentum_15m_0.10pct | 1016 | 48.3 | 49.6 | $-622.12 | -6.1% | $377.88 | -1.9 | done | can't tell from luck |
| reversal_60m_0.30pct | 847 | 50.2 | 52.0 | $-635.93 | -7.5% | $364.07 | -2.3 | done | losing for real |
| coinflip | 1492 | 49.8 | 50.8 | $-839.78 | -5.6% | $160.22 | -2.2 | done | losing for real |
| momentum_5m_0.00pct | 1492 | 49.5 | 51.5 | $-1094.98 | -7.3% | $-94.98 | -2.9 | done | losing for real |
| always_up | 1492 | 45.6 | 50.7 | $-2029.36 | -13.6% | $-1029.36 | -5.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2294 | 47.3 | 49.3 | $-1807.31 |
| ETH | 2562 | 47.7 | 48.8 | $-1802.32 |
| SOL | 2639 | 47.9 | 49.4 | $-1984.11 |
| XRP | 2694 | 48.7 | 49.1 | $-1402.83 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
