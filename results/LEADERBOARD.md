# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 21, 3:35 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 990 windows, 27531 settled trades, 48 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 505 | 34.3 | 34.9 | $-285.26 | -5.6% | $714.74 | -0.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 2811 | 51.0 | 50.4 | $-868.21 | -3.1% | $131.79 | -1.6 | done | can't tell from luck |
| value_ev10 | 1257 | 37.5 | 39.1 | $-881.38 | -7.0% | $118.62 | -2.0 | done | losing for real |
| momentum_60m_0.30pct | 2367 | 49.9 | 49.7 | $-1073.60 | -4.5% | $-73.60 | -2.2 | done | losing for real |
| trend_filter | 1648 | 49.6 | 50.9 | $-1212.65 | -7.4% | $-212.65 | -3.1 | done | losing for real |
| value_ev5 | 1903 | 39.6 | 41.0 | $-1246.17 | -6.5% | $-246.17 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 2367 | 50.1 | 50.9 | $-1551.79 | -6.6% | $-551.79 | -3.3 | done | losing for real |
| coinflip | 3954 | 50.2 | 50.3 | $-1815.60 | -4.6% | $-815.60 | -2.9 | done | losing for real |
| momentum_15m_0.10pct | 2811 | 49.0 | 50.4 | $-1900.10 | -6.8% | $-900.10 | -3.6 | done | losing for real |
| momentum_5m_0.00pct | 3954 | 50.8 | 51.5 | $-2097.06 | -5.3% | $-1097.06 | -3.4 | done | losing for real |
| always_up | 3954 | 46.8 | 49.6 | $-3932.92 | -9.9% | $-2932.92 | -6.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6275 | 48.2 | 49.1 | $-3572.52 |
| ETH | 6843 | 48.0 | 48.5 | $-4482.89 |
| SOL | 7196 | 48.1 | 48.6 | $-4250.38 |
| XRP | 7217 | 48.1 | 48.5 | $-4558.96 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
