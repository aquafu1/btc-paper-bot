# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 19, 1:05 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 836 windows, 22986 settled trades, 45 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 423 | 33.1 | 34.9 | $-400.80 | -9.5% | $599.20 | -1.5 | done | can't tell from luck |
| reversal_15m_0.10pct | 2346 | 51.0 | 50.6 | $-823.98 | -3.5% | $176.02 | -1.7 | done | can't tell from luck |
| momentum_60m_0.30pct | 1934 | 49.9 | 49.7 | $-883.55 | -4.6% | $116.45 | -2.0 | done | losing for real |
| value_ev10 | 1048 | 37.2 | 39.1 | $-883.78 | -8.4% | $116.22 | -2.2 | done | losing for real |
| trend_filter | 1356 | 49.7 | 50.8 | $-991.58 | -7.3% | $8.42 | -2.8 | done | losing for real |
| value_ev5 | 1588 | 39.5 | 41.1 | $-1167.89 | -7.4% | $-167.89 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 1934 | 50.1 | 51.2 | $-1361.78 | -7.0% | $-361.78 | -3.2 | done | losing for real |
| coinflip | 3337 | 50.4 | 50.3 | $-1403.30 | -4.2% | $-403.30 | -2.5 | done | losing for real |
| momentum_15m_0.10pct | 2346 | 49.0 | 50.3 | $-1524.81 | -6.5% | $-524.81 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 3337 | 51.2 | 51.7 | $-1617.24 | -4.8% | $-617.24 | -2.9 | done | losing for real |
| always_up | 3337 | 47.3 | 49.6 | $-3055.12 | -9.2% | $-2055.12 | -5.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5223 | 48.1 | 49.1 | $-3317.47 |
| ETH | 5720 | 48.0 | 48.5 | $-3950.05 |
| SOL | 5993 | 48.2 | 48.6 | $-3507.28 |
| XRP | 6050 | 48.4 | 48.5 | $-3339.05 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
