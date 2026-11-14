# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 14, 9:15 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 341 windows, 9131 settled trades, 61 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 184 | 37.5 | 36.6 | $-38.35 | -2.1% | $961.65 | -0.2 | Sat 5:00 PM | too few trades (184/200) |
| reversal_60m_0.30pct | 733 | 52.4 | 52.0 | $-226.69 | -3.1% | $773.31 | -0.9 | done | can't tell from luck |
| value_ev10 | 446 | 39.5 | 40.2 | $-252.22 | -5.7% | $747.78 | -1.0 | done | can't tell from luck |
| reversal_15m_0.10pct | 905 | 52.0 | 51.9 | $-360.13 | -4.0% | $639.87 | -1.3 | done | can't tell from luck |
| value_ev5 | 661 | 41.0 | 41.9 | $-403.83 | -6.1% | $596.17 | -1.4 | done | can't tell from luck |
| trend_filter | 496 | 46.2 | 50.2 | $-607.84 | -12.3% | $392.16 | -2.8 | done | losing for real |
| momentum_60m_0.30pct | 733 | 47.6 | 49.6 | $-616.25 | -8.4% | $383.75 | -2.3 | done | losing for real |
| coinflip | 1356 | 50.2 | 50.8 | $-682.33 | -5.0% | $317.67 | -1.9 | done | can't tell from luck |
| momentum_15m_0.10pct | 905 | 48.0 | 49.8 | $-692.40 | -7.7% | $307.60 | -2.3 | done | losing for real |
| momentum_5m_0.00pct | 1356 | 48.8 | 51.3 | $-1164.82 | -8.6% | $-164.82 | -3.3 | done | losing for real |
| always_up | 1356 | 47.1 | 50.5 | $-1441.84 | -10.6% | $-441.84 | -4.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2044 | 47.0 | 49.2 | $-1703.87 |
| ETH | 2297 | 47.4 | 48.6 | $-1717.83 |
| SOL | 2374 | 47.9 | 49.3 | $-1812.86 |
| XRP | 2416 | 48.7 | 49.1 | $-1252.15 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
