# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 16, 12:50 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 547 windows, 15188 settled trades, 45 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1301 | 51.6 | 49.7 | $-168.15 | -1.3% | $831.85 | -0.5 | done | can't tell from luck |
| value_ev20 | 298 | 32.9 | 35.2 | $-362.88 | -12.2% | $637.12 | -1.6 | done | can't tell from luck |
| trend_filter | 886 | 50.8 | 50.9 | $-439.63 | -5.0% | $560.37 | -1.5 | done | can't tell from luck |
| momentum_15m_0.10pct | 1536 | 49.7 | 49.8 | $-707.25 | -4.6% | $292.75 | -1.8 | done | can't tell from luck |
| value_ev10 | 717 | 36.7 | 39.4 | $-820.87 | -11.4% | $179.13 | -2.6 | done | losing for real |
| value_ev5 | 1067 | 39.1 | 41.2 | $-1022.51 | -9.6% | $-22.51 | -2.7 | done | losing for real |
| reversal_15m_0.10pct | 1536 | 50.3 | 51.2 | $-1059.01 | -6.9% | $-59.01 | -2.8 | done | losing for real |
| coinflip | 2182 | 49.9 | 50.5 | $-1288.15 | -5.9% | $-288.15 | -2.8 | done | losing for real |
| reversal_60m_0.30pct | 1301 | 48.4 | 51.2 | $-1376.07 | -10.6% | $-376.07 | -3.9 | done | losing for real |
| momentum_5m_0.00pct | 2182 | 50.1 | 51.8 | $-1596.28 | -7.3% | $-596.28 | -3.6 | done | losing for real |
| always_up | 2182 | 46.7 | 50.0 | $-2484.45 | -11.4% | $-1484.45 | -5.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3435 | 47.4 | 49.2 | $-2870.45 |
| ETH | 3792 | 47.8 | 48.6 | $-2782.49 |
| SOL | 3967 | 47.6 | 48.7 | $-3123.76 |
| XRP | 3994 | 48.4 | 48.7 | $-2548.56 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
