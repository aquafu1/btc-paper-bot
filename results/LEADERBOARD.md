# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 15, 7:00 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 476 windows, 13050 settled trades, 73 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 238 | 35.3 | 35.9 | $-125.26 | -5.3% | $874.74 | -0.6 | done | can't tell from luck |
| momentum_60m_0.30pct | 1103 | 50.9 | 50.0 | $-264.32 | -2.4% | $735.68 | -0.8 | done | can't tell from luck |
| value_ev10 | 614 | 39.3 | 40.2 | $-344.93 | -5.6% | $655.07 | -1.2 | done | can't tell from luck |
| momentum_15m_0.10pct | 1318 | 50.3 | 50.1 | $-394.47 | -3.0% | $605.53 | -1.1 | done | can't tell from luck |
| trend_filter | 758 | 49.6 | 50.8 | $-468.46 | -6.2% | $531.54 | -1.7 | done | can't tell from luck |
| value_ev5 | 910 | 41.1 | 41.9 | $-497.62 | -5.5% | $502.38 | -1.4 | done | can't tell from luck |
| reversal_60m_0.30pct | 1103 | 49.1 | 51.5 | $-954.14 | -8.7% | $45.86 | -2.9 | done | losing for real |
| reversal_15m_0.10pct | 1318 | 49.7 | 51.4 | $-955.74 | -7.3% | $44.26 | -2.7 | done | losing for real |
| coinflip | 1896 | 49.9 | 50.8 | $-1029.45 | -5.4% | $-29.45 | -2.4 | done | losing for real |
| momentum_5m_0.00pct | 1896 | 49.7 | 51.7 | $-1359.79 | -7.2% | $-359.79 | -3.2 | done | losing for real |
| always_up | 1896 | 46.5 | 50.4 | $-2168.70 | -11.4% | $-1168.70 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2946 | 47.5 | 49.3 | $-2257.93 |
| ETH | 3271 | 48.1 | 48.9 | $-2123.47 |
| SOL | 3398 | 47.7 | 49.3 | $-2493.67 |
| XRP | 3435 | 48.7 | 49.1 | $-1687.81 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
