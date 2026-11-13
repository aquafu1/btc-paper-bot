# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 13, 5:30 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 230 windows, 6026 settled trades, 39 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 592 | 56.1 | 52.6 | $+189.71 | +3.2% | $1189.71 | +0.8 | done | can't tell from luck |
| reversal_60m_0.30pct | 474 | 53.8 | 52.4 | $-40.50 | -0.9% | $959.50 | -0.2 | done | can't tell from luck |
| value_ev20 | 112 | 33.9 | 36.6 | $-124.82 | -11.1% | $875.18 | -0.9 | Sun 6:00 AM | too few trades (112/200) |
| value_ev10 | 297 | 37.4 | 40.7 | $-350.78 | -11.8% | $649.22 | -1.7 | done | can't tell from luck |
| trend_filter | 317 | 45.4 | 50.1 | $-420.76 | -13.3% | $579.24 | -2.4 | done | losing for real |
| value_ev5 | 432 | 39.4 | 42.5 | $-478.33 | -11.1% | $521.67 | -2.0 | done | losing for real |
| momentum_60m_0.30pct | 474 | 46.2 | 49.8 | $-532.63 | -11.2% | $467.37 | -2.5 | done | losing for real |
| momentum_5m_0.00pct | 912 | 50.2 | 51.5 | $-578.44 | -6.3% | $421.56 | -2.0 | done | can't tell from luck |
| coinflip | 912 | 49.6 | 51.0 | $-614.91 | -6.7% | $385.09 | -2.1 | done | losing for real |
| momentum_15m_0.10pct | 592 | 43.9 | 49.6 | $-889.39 | -15.0% | $110.61 | -3.7 | done | losing for real |
| always_up | 912 | 47.3 | 50.3 | $-925.81 | -10.2% | $74.19 | -3.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1355 | 46.4 | 49.6 | $-1374.47 |
| ETH | 1499 | 46.8 | 49.0 | $-1416.25 |
| SOL | 1557 | 48.0 | 49.3 | $-1261.15 |
| XRP | 1615 | 49.0 | 49.1 | $-714.79 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
