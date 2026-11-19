# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 19, 3:45 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 847 windows, 23320 settled trades, 80 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 430 | 33.7 | 34.9 | $-317.48 | -7.4% | $682.52 | -1.2 | done | can't tell from luck |
| value_ev10 | 1063 | 37.6 | 39.1 | $-773.87 | -7.3% | $226.13 | -1.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 1969 | 50.2 | 49.7 | $-775.99 | -3.9% | $224.01 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 2383 | 50.8 | 50.6 | $-900.61 | -3.8% | $99.39 | -1.9 | done | can't tell from luck |
| trend_filter | 1374 | 50.1 | 50.9 | $-902.39 | -6.6% | $97.61 | -2.5 | done | losing for real |
| value_ev5 | 1609 | 39.8 | 41.1 | $-1076.42 | -6.7% | $-76.42 | -2.3 | done | losing for real |
| momentum_15m_0.10pct | 2383 | 49.2 | 50.3 | $-1439.14 | -6.0% | $-439.14 | -3.0 | done | losing for real |
| reversal_60m_0.30pct | 1969 | 49.8 | 51.1 | $-1476.96 | -7.5% | $-476.96 | -3.4 | done | losing for real |
| coinflip | 3380 | 50.2 | 50.3 | $-1502.31 | -4.4% | $-502.31 | -2.6 | done | losing for real |
| momentum_5m_0.00pct | 3380 | 51.2 | 51.7 | $-1596.80 | -4.7% | $-596.80 | -2.8 | done | losing for real |
| always_up | 3380 | 46.9 | 49.6 | $-3268.82 | -9.7% | $-2268.82 | -5.6 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5308 | 48.2 | 49.1 | $-3153.47 |
| ETH | 5806 | 48.0 | 48.5 | $-3938.94 |
| SOL | 6081 | 48.2 | 48.6 | $-3621.77 |
| XRP | 6125 | 48.4 | 48.5 | $-3316.61 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
