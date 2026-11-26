# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 25, 10:30 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1450 windows, 36779 settled trades, 390 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 743 | 34.3 | 35.3 | $-563.47 | -7.6% | $436.53 | -1.6 | done | can't tell from luck |
| value_ev10 | 1792 | 38.7 | 39.2 | $-866.32 | -4.8% | $133.68 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 3668 | 50.9 | 50.0 | $-970.09 | -2.6% | $29.91 | -1.6 | done | can't tell from luck |
| value_ev5 | 2698 | 40.5 | 41.1 | $-1351.66 | -5.0% | $-351.66 | -2.2 | done | losing for real |
| momentum_60m_0.30pct | 3080 | 49.2 | 49.3 | $-1531.81 | -5.0% | $-531.81 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 3080 | 50.8 | 51.0 | $-1577.44 | -5.1% | $-577.44 | -2.9 | done | losing for real |
| trend_filter | 2180 | 48.6 | 50.3 | $-1889.45 | -8.7% | $-889.45 | -4.1 | done | losing for real |
| coinflip | 5290 | 50.0 | 50.0 | $-2284.32 | -4.3% | $-1284.32 | -3.2 | done | losing for real |
| momentum_15m_0.10pct | 3668 | 49.1 | 50.2 | $-2300.84 | -6.3% | $-1300.84 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 5290 | 50.1 | 51.3 | $-3343.97 | -6.3% | $-2343.97 | -4.7 | done | losing for real |
| always_up | 5290 | 48.0 | 49.2 | $-3568.73 | -6.7% | $-2568.73 | -4.9 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 9385 | 48.1 | 48.7 | $-5016.84 |
| ETH | 10084 | 47.9 | 48.0 | $-5647.02 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
