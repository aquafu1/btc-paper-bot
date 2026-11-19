# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 19, 2:00 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 840 windows, 23085 settled trades, 62 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 424 | 33.0 | 34.9 | $-410.80 | -9.7% | $589.20 | -1.5 | done | can't tell from luck |
| reversal_15m_0.10pct | 2358 | 50.9 | 50.6 | $-865.54 | -3.7% | $134.46 | -1.8 | done | can't tell from luck |
| value_ev10 | 1052 | 37.2 | 39.1 | $-899.14 | -8.5% | $100.86 | -2.3 | done | losing for real |
| momentum_60m_0.30pct | 1943 | 49.9 | 49.7 | $-912.83 | -4.7% | $87.17 | -2.1 | done | losing for real |
| trend_filter | 1357 | 49.7 | 50.8 | $-980.66 | -7.2% | $19.34 | -2.7 | done | losing for real |
| value_ev5 | 1594 | 39.5 | 41.1 | $-1179.29 | -7.4% | $-179.29 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 1943 | 50.1 | 51.1 | $-1363.75 | -7.0% | $-363.75 | -3.2 | done | losing for real |
| coinflip | 3352 | 50.3 | 50.3 | $-1484.73 | -4.4% | $-484.73 | -2.6 | done | losing for real |
| momentum_15m_0.10pct | 2358 | 49.1 | 50.3 | $-1503.77 | -6.4% | $-503.77 | -3.1 | done | losing for real |
| momentum_5m_0.00pct | 3352 | 51.2 | 51.7 | $-1605.28 | -4.8% | $-605.28 | -2.9 | done | losing for real |
| always_up | 3352 | 47.1 | 49.6 | $-3135.61 | -9.4% | $-2135.61 | -5.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5248 | 48.1 | 49.1 | $-3391.79 |
| ETH | 5747 | 48.0 | 48.5 | $-3975.77 |
| SOL | 6022 | 48.2 | 48.6 | $-3578.49 |
| XRP | 6068 | 48.4 | 48.5 | $-3395.35 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
