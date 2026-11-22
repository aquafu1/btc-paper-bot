# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 21, 9:45 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1063 windows, 29411 settled trades, 72 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 547 | 34.6 | 35.1 | $-310.90 | -5.7% | $689.10 | -1.0 | done | can't tell from luck |
| reversal_15m_0.10pct | 2977 | 51.2 | 50.4 | $-793.77 | -2.7% | $206.23 | -1.5 | done | can't tell from luck |
| value_ev10 | 1359 | 37.7 | 39.2 | $-927.80 | -6.8% | $72.20 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 2501 | 49.7 | 49.6 | $-1140.74 | -4.6% | $-140.74 | -2.3 | done | losing for real |
| trend_filter | 1752 | 49.5 | 50.7 | $-1304.54 | -7.4% | $-304.54 | -3.2 | done | losing for real |
| value_ev5 | 2065 | 39.8 | 41.0 | $-1309.38 | -6.3% | $-309.38 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 2501 | 50.3 | 51.0 | $-1592.04 | -6.4% | $-592.04 | -3.3 | done | losing for real |
| coinflip | 4244 | 50.5 | 50.3 | $-1711.73 | -4.0% | $-711.73 | -2.7 | done | losing for real |
| momentum_15m_0.10pct | 2977 | 48.8 | 50.3 | $-2066.21 | -6.9% | $-1066.21 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 4244 | 50.9 | 51.5 | $-2188.20 | -5.2% | $-1188.20 | -3.5 | done | losing for real |
| always_up | 4244 | 47.2 | 49.4 | $-3745.13 | -8.8% | $-2745.13 | -5.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6712 | 48.4 | 49.0 | $-3454.46 |
| ETH | 7276 | 48.1 | 48.5 | $-4610.02 |
| SOL | 7674 | 48.1 | 48.5 | $-4436.23 |
| XRP | 7749 | 48.2 | 48.3 | $-4589.72 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
