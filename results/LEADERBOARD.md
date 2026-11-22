# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 22, 9:50 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1111 windows, 30748 settled trades, 38 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 586 | 34.3 | 35.1 | $-390.56 | -6.7% | $609.44 | -1.2 | done | can't tell from luck |
| reversal_15m_0.10pct | 3100 | 51.3 | 50.4 | $-767.23 | -2.5% | $232.77 | -1.4 | done | can't tell from luck |
| value_ev10 | 1432 | 37.8 | 39.1 | $-980.15 | -6.8% | $19.85 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 2610 | 49.7 | 49.4 | $-1090.46 | -4.2% | $-90.46 | -2.1 | done | losing for real |
| value_ev5 | 2171 | 39.8 | 41.0 | $-1363.96 | -6.3% | $-363.96 | -2.5 | done | losing for real |
| trend_filter | 1822 | 49.2 | 50.4 | $-1374.17 | -7.5% | $-374.17 | -3.3 | done | losing for real |
| reversal_60m_0.30pct | 2610 | 50.3 | 51.1 | $-1689.08 | -6.5% | $-689.08 | -3.4 | done | losing for real |
| coinflip | 4439 | 50.5 | 50.2 | $-1707.58 | -3.8% | $-707.58 | -2.6 | done | losing for real |
| momentum_15m_0.10pct | 3100 | 48.7 | 50.2 | $-2147.63 | -6.9% | $-1147.63 | -3.9 | done | losing for real |
| momentum_5m_0.00pct | 4439 | 50.6 | 51.4 | $-2398.88 | -5.4% | $-1398.88 | -3.7 | done | losing for real |
| always_up | 4439 | 47.5 | 49.3 | $-3578.15 | -8.1% | $-2578.15 | -5.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7039 | 48.4 | 49.0 | $-3556.72 |
| ETH | 7621 | 48.1 | 48.4 | $-4688.23 |
| SOL | 8000 | 48.0 | 48.4 | $-4533.07 |
| XRP | 8088 | 48.2 | 48.2 | $-4709.85 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
