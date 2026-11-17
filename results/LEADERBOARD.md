# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 17, 12:50 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 595 windows, 16471 settled trades, 40 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1394 | 51.3 | 49.6 | $-174.37 | -1.3% | $825.63 | -0.5 | done | can't tell from luck |
| value_ev20 | 323 | 34.4 | 35.2 | $-232.82 | -7.2% | $767.18 | -1.0 | done | can't tell from luck |
| trend_filter | 955 | 50.3 | 50.9 | $-536.54 | -5.6% | $463.46 | -1.8 | done | can't tell from luck |
| value_ev10 | 774 | 38.1 | 39.4 | $-561.90 | -7.3% | $438.10 | -1.7 | done | can't tell from luck |
| value_ev5 | 1158 | 40.6 | 41.2 | $-646.37 | -5.6% | $353.63 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 1674 | 50.8 | 51.0 | $-811.37 | -4.8% | $188.63 | -2.0 | done | losing for real |
| momentum_15m_0.10pct | 1674 | 49.2 | 49.9 | $-928.65 | -5.5% | $71.35 | -2.3 | done | losing for real |
| coinflip | 2375 | 50.0 | 50.5 | $-1177.59 | -5.0% | $-177.59 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 1394 | 48.7 | 51.4 | $-1374.80 | -9.9% | $-374.80 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 2375 | 50.2 | 51.8 | $-1565.28 | -6.6% | $-565.28 | -3.3 | done | losing for real |
| always_up | 2375 | 47.1 | 49.8 | $-2249.79 | -9.5% | $-1249.79 | -4.6 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3744 | 48.0 | 49.2 | $-2467.93 |
| ETH | 4109 | 48.0 | 48.6 | $-2654.20 |
| SOL | 4285 | 47.9 | 48.7 | $-2881.40 |
| XRP | 4333 | 48.5 | 48.6 | $-2255.95 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
