# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 21, 9:30 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1014 windows, 28228 settled trades, 60 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 519 | 34.1 | 35.0 | $-322.56 | -6.2% | $677.44 | -1.1 | done | can't tell from luck |
| reversal_15m_0.10pct | 2878 | 51.0 | 50.5 | $-911.88 | -3.2% | $88.12 | -1.7 | done | can't tell from luck |
| momentum_60m_0.30pct | 2434 | 50.1 | 49.7 | $-963.06 | -4.0% | $36.94 | -2.0 | done | can't tell from luck |
| value_ev10 | 1292 | 37.2 | 39.1 | $-1012.99 | -7.8% | $-12.99 | -2.3 | done | losing for real |
| trend_filter | 1693 | 49.9 | 50.8 | $-1147.03 | -6.8% | $-147.03 | -2.9 | done | losing for real |
| value_ev5 | 1956 | 39.4 | 41.0 | $-1384.73 | -7.1% | $-384.73 | -2.6 | done | losing for real |
| coinflip | 4048 | 50.4 | 50.4 | $-1696.86 | -4.2% | $-696.86 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 2434 | 49.9 | 51.0 | $-1728.93 | -7.1% | $-728.93 | -3.6 | done | losing for real |
| momentum_15m_0.10pct | 2878 | 49.0 | 50.3 | $-1902.83 | -6.6% | $-902.83 | -3.6 | done | losing for real |
| momentum_5m_0.00pct | 4048 | 50.8 | 51.6 | $-2144.63 | -5.3% | $-1144.63 | -3.5 | done | losing for real |
| always_up | 4048 | 47.3 | 49.5 | $-3604.18 | -8.9% | $-2604.18 | -5.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6436 | 48.3 | 49.1 | $-3531.47 |
| ETH | 7015 | 48.1 | 48.5 | $-4455.71 |
| SOL | 7375 | 48.2 | 48.6 | $-4193.81 |
| XRP | 7402 | 48.1 | 48.4 | $-4638.67 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
