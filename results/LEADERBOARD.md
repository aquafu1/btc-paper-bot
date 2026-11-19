# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 19, 4:50 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 851 windows, 23494 settled trades, 37 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 441 | 34.2 | 34.8 | $-260.78 | -5.9% | $739.22 | -0.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 1987 | 50.3 | 49.7 | $-736.24 | -3.7% | $263.76 | -1.7 | done | can't tell from luck |
| value_ev10 | 1076 | 37.7 | 39.0 | $-737.17 | -6.9% | $262.83 | -1.8 | done | can't tell from luck |
| trend_filter | 1383 | 50.2 | 50.9 | $-887.68 | -6.4% | $112.32 | -2.5 | done | losing for real |
| reversal_15m_0.10pct | 2400 | 50.7 | 50.5 | $-948.52 | -4.0% | $51.48 | -1.9 | done | can't tell from luck |
| value_ev5 | 1623 | 39.8 | 41.0 | $-1049.71 | -6.5% | $-49.71 | -2.2 | done | losing for real |
| momentum_15m_0.10pct | 2400 | 49.3 | 50.4 | $-1414.89 | -5.9% | $-414.89 | -2.9 | done | losing for real |
| reversal_60m_0.30pct | 1987 | 49.7 | 51.1 | $-1515.54 | -7.6% | $-515.54 | -3.5 | done | losing for real |
| coinflip | 3399 | 50.2 | 50.3 | $-1519.03 | -4.5% | $-519.03 | -2.6 | done | losing for real |
| momentum_5m_0.00pct | 3399 | 51.3 | 51.7 | $-1575.27 | -4.6% | $-575.27 | -2.8 | done | losing for real |
| always_up | 3399 | 47.0 | 49.5 | $-3263.17 | -9.6% | $-2263.17 | -5.6 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5354 | 48.3 | 49.0 | $-2995.60 |
| ETH | 5853 | 48.0 | 48.5 | $-3862.17 |
| SOL | 6117 | 48.2 | 48.5 | $-3667.33 |
| XRP | 6170 | 48.4 | 48.5 | $-3382.91 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
