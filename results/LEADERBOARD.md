# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 17, 3:20 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 653 windows, 18074 settled trades, 27 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 343 | 34.1 | 35.4 | $-267.49 | -7.8% | $732.51 | -1.1 | done | can't tell from luck |
| momentum_60m_0.30pct | 1527 | 50.6 | 49.6 | $-387.66 | -2.5% | $612.34 | -1.0 | done | can't tell from luck |
| reversal_15m_0.10pct | 1853 | 51.6 | 51.0 | $-554.17 | -3.0% | $445.83 | -1.3 | done | can't tell from luck |
| trend_filter | 1045 | 50.2 | 50.9 | $-591.70 | -5.7% | $408.30 | -1.9 | done | can't tell from luck |
| value_ev10 | 837 | 38.1 | 39.5 | $-630.22 | -7.5% | $369.78 | -1.8 | done | can't tell from luck |
| value_ev5 | 1265 | 40.7 | 41.4 | $-705.58 | -5.6% | $294.42 | -1.7 | done | can't tell from luck |
| coinflip | 2608 | 50.0 | 50.5 | $-1236.31 | -4.7% | $-236.31 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 1527 | 49.4 | 51.4 | $-1250.50 | -8.2% | $-250.50 | -3.3 | done | losing for real |
| momentum_15m_0.10pct | 1853 | 48.4 | 50.0 | $-1288.80 | -7.0% | $-288.80 | -3.0 | done | losing for real |
| momentum_5m_0.00pct | 2608 | 50.7 | 51.8 | $-1451.29 | -5.6% | $-451.29 | -2.9 | done | losing for real |
| always_up | 2608 | 47.5 | 49.7 | $-2213.72 | -8.5% | $-1213.72 | -4.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4098 | 48.3 | 49.3 | $-2521.50 |
| ETH | 4512 | 48.2 | 48.7 | $-2780.96 |
| SOL | 4702 | 48.0 | 48.8 | $-2931.71 |
| XRP | 4762 | 48.5 | 48.6 | $-2343.27 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
