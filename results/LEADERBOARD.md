# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 21, 6:30 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1050 windows, 29114 settled trades, 38 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 544 | 34.6 | 35.1 | $-308.54 | -5.7% | $691.46 | -1.0 | done | can't tell from luck |
| reversal_15m_0.10pct | 2951 | 51.3 | 50.4 | $-759.91 | -2.6% | $240.09 | -1.4 | done | can't tell from luck |
| value_ev10 | 1349 | 37.6 | 39.2 | $-963.69 | -7.1% | $36.31 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 2483 | 49.7 | 49.6 | $-1172.66 | -4.7% | $-172.66 | -2.4 | done | losing for real |
| trend_filter | 1737 | 49.3 | 50.7 | $-1358.44 | -7.8% | $-358.44 | -3.3 | done | losing for real |
| value_ev5 | 2040 | 39.5 | 41.0 | $-1409.42 | -6.9% | $-409.42 | -2.6 | done | losing for real |
| reversal_60m_0.30pct | 2483 | 50.3 | 51.0 | $-1552.68 | -6.3% | $-552.68 | -3.2 | done | losing for real |
| coinflip | 4192 | 50.5 | 50.3 | $-1691.72 | -4.0% | $-691.72 | -2.6 | done | losing for real |
| momentum_15m_0.10pct | 2951 | 48.7 | 50.3 | $-2086.68 | -7.1% | $-1086.68 | -3.9 | done | losing for real |
| momentum_5m_0.00pct | 4192 | 50.8 | 51.5 | $-2246.48 | -5.4% | $-1246.48 | -3.6 | done | losing for real |
| always_up | 4192 | 47.4 | 49.4 | $-3635.96 | -8.7% | $-2635.96 | -5.6 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6634 | 48.3 | 49.0 | $-3526.73 |
| ETH | 7209 | 48.1 | 48.5 | $-4577.58 |
| SOL | 7602 | 48.1 | 48.5 | $-4423.50 |
| XRP | 7669 | 48.2 | 48.3 | $-4658.37 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
