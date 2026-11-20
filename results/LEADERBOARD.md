# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 19, 10:05 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 872 windows, 24088 settled trades, 30 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 453 | 35.5 | 34.9 | $-116.41 | -2.6% | $883.59 | -0.4 | done | can't tell from luck |
| value_ev10 | 1105 | 38.4 | 39.1 | $-585.75 | -5.3% | $414.25 | -1.4 | done | can't tell from luck |
| momentum_60m_0.30pct | 2037 | 50.0 | 49.8 | $-852.98 | -4.2% | $147.02 | -1.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 2460 | 50.7 | 50.5 | $-915.89 | -3.7% | $84.11 | -1.8 | done | can't tell from luck |
| value_ev5 | 1668 | 40.0 | 41.0 | $-958.15 | -5.7% | $41.85 | -2.0 | done | can't tell from luck |
| trend_filter | 1419 | 50.0 | 51.0 | $-979.43 | -6.9% | $20.57 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 2037 | 50.0 | 51.0 | $-1386.13 | -6.8% | $-386.13 | -3.1 | done | losing for real |
| momentum_15m_0.10pct | 2460 | 49.3 | 50.4 | $-1443.82 | -5.9% | $-443.82 | -2.9 | done | losing for real |
| coinflip | 3483 | 50.1 | 50.3 | $-1550.61 | -4.5% | $-550.61 | -2.6 | done | losing for real |
| momentum_5m_0.00pct | 3483 | 51.2 | 51.7 | $-1653.60 | -4.7% | $-653.60 | -2.9 | done | losing for real |
| always_up | 3483 | 47.0 | 49.6 | $-3354.48 | -9.6% | $-2354.48 | -5.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5499 | 48.3 | 49.1 | $-2950.69 |
| ETH | 5992 | 48.1 | 48.5 | $-3834.82 |
| SOL | 6290 | 48.3 | 48.6 | $-3564.48 |
| XRP | 6307 | 48.4 | 48.5 | $-3447.27 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
