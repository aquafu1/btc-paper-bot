# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 24, 2:45 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1323 windows, 35022 settled trades, 419 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 689 | 34.4 | 35.3 | $-497.07 | -7.2% | $502.93 | -1.4 | done | can't tell from luck |
| value_ev10 | 1689 | 38.8 | 39.2 | $-769.05 | -4.6% | $230.95 | -1.5 | done | can't tell from luck |
| reversal_15m_0.10pct | 3509 | 50.8 | 50.2 | $-1038.42 | -3.0% | $-38.42 | -1.7 | done | can't tell from luck |
| value_ev5 | 2547 | 40.5 | 41.1 | $-1246.98 | -4.9% | $-246.98 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 2943 | 49.4 | 49.4 | $-1398.70 | -4.8% | $-398.70 | -2.6 | done | losing for real |
| reversal_60m_0.30pct | 2943 | 50.6 | 50.9 | $-1574.71 | -5.4% | $-574.71 | -3.0 | done | losing for real |
| trend_filter | 2085 | 48.7 | 50.5 | $-1773.38 | -8.5% | $-773.38 | -4.0 | done | losing for real |
| momentum_15m_0.10pct | 3509 | 49.2 | 50.2 | $-2181.57 | -6.2% | $-1181.57 | -3.7 | done | losing for real |
| coinflip | 5036 | 49.9 | 50.0 | $-2347.82 | -4.7% | $-1347.82 | -3.3 | done | losing for real |
| momentum_5m_0.00pct | 5036 | 50.3 | 51.4 | $-3013.33 | -6.0% | $-2013.33 | -4.4 | done | losing for real |
| always_up | 5036 | 47.8 | 49.3 | $-3717.54 | -7.4% | $-2717.54 | -5.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 8524 | 47.9 | 48.8 | $-5135.92 |
| ETH | 9188 | 48.2 | 48.2 | $-4838.41 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
