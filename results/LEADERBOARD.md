# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 15, 5:35 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 422 windows, 11619 settled trades, 35 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 210 | 34.8 | 36.4 | $-166.95 | -8.0% | $833.05 | -0.9 | done | can't tell from luck |
| value_ev10 | 540 | 39.4 | 40.4 | $-321.49 | -6.0% | $678.51 | -1.2 | done | can't tell from luck |
| momentum_60m_0.30pct | 996 | 50.5 | 50.0 | $-324.34 | -3.3% | $675.66 | -1.0 | done | can't tell from luck |
| value_ev5 | 813 | 41.5 | 42.1 | $-438.73 | -5.4% | $561.27 | -1.3 | done | can't tell from luck |
| trend_filter | 665 | 49.3 | 50.7 | $-452.59 | -6.8% | $547.41 | -1.8 | done | can't tell from luck |
| momentum_15m_0.10pct | 1175 | 49.0 | 50.0 | $-646.62 | -5.5% | $353.38 | -1.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 1175 | 51.0 | 51.8 | $-672.87 | -5.7% | $327.13 | -2.1 | done | losing for real |
| coinflip | 1683 | 50.5 | 51.0 | $-769.36 | -4.6% | $230.64 | -1.9 | done | can't tell from luck |
| reversal_60m_0.30pct | 996 | 49.5 | 51.9 | $-857.56 | -8.6% | $142.44 | -2.9 | done | losing for real |
| momentum_5m_0.00pct | 1683 | 49.4 | 51.6 | $-1307.81 | -7.8% | $-307.81 | -3.3 | done | losing for real |
| always_up | 1683 | 46.0 | 50.7 | $-2149.49 | -12.8% | $-1149.49 | -5.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2635 | 47.7 | 49.4 | $-1928.96 |
| ETH | 2914 | 47.9 | 49.0 | $-1864.97 |
| SOL | 3011 | 47.6 | 49.5 | $-2564.40 |
| XRP | 3059 | 48.7 | 49.3 | $-1749.49 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
