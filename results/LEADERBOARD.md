# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 19, 3:20 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 845 windows, 23289 settled trades, 31 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 430 | 33.7 | 34.9 | $-317.48 | -7.4% | $682.52 | -1.2 | done | can't tell from luck |
| value_ev10 | 1063 | 37.6 | 39.1 | $-773.87 | -7.3% | $226.13 | -1.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 1966 | 50.2 | 49.7 | $-803.77 | -4.1% | $196.23 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 2379 | 50.9 | 50.6 | $-860.61 | -3.6% | $139.39 | -1.8 | done | can't tell from luck |
| trend_filter | 1372 | 50.0 | 50.9 | $-923.15 | -6.7% | $76.85 | -2.6 | done | losing for real |
| value_ev5 | 1609 | 39.8 | 41.1 | $-1076.42 | -6.7% | $-76.42 | -2.3 | done | losing for real |
| reversal_60m_0.30pct | 1966 | 49.8 | 51.1 | $-1446.96 | -7.4% | $-446.96 | -3.3 | done | losing for real |
| coinflip | 3375 | 50.3 | 50.3 | $-1469.33 | -4.4% | $-469.33 | -2.5 | done | losing for real |
| momentum_15m_0.10pct | 2379 | 49.1 | 50.3 | $-1474.52 | -6.2% | $-474.52 | -3.0 | done | losing for real |
| momentum_5m_0.00pct | 3375 | 51.2 | 51.7 | $-1606.86 | -4.8% | $-606.86 | -2.9 | done | losing for real |
| always_up | 3375 | 47.0 | 49.5 | $-3218.82 | -9.5% | $-2218.82 | -5.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5295 | 48.2 | 49.1 | $-3138.62 |
| ETH | 5801 | 48.0 | 48.5 | $-3927.54 |
| SOL | 6073 | 48.2 | 48.6 | $-3619.34 |
| XRP | 6120 | 48.4 | 48.5 | $-3286.28 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
