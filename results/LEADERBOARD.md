# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 10, 5:00 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 8 windows, 158 settled trades, 59 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| coinflip | 24 | 62.5 | 51.7 | $+41.00 | +17.1% | $1041.00 | +0.9 | Wed 3:45 AM | too few trades (24/200) |
| value_ev10 | 11 | 54.5 | 39.5 | $+30.74 | +27.9% | $1030.74 | +0.7 | Wed 6:45 PM | too few trades (11/200) |
| value_ev20 | 4 | 50.0 | 35.1 | $+11.31 | +28.3% | $1011.31 | +0.4 | Fri 6:15 PM | too few trades (4/200) |
| momentum_15m_0.10pct | 14 | 50.0 | 49.6 | $-1.04 | -0.7% | $998.96 | -0.0 | Wed 12:45 PM | too few trades (14/200) |
| momentum_60m_0.30pct | 9 | 55.6 | 55.7 | $-1.76 | -2.0% | $998.24 | -0.1 | Thu 12:45 AM | too few trades (9/200) |
| reversal_60m_0.30pct | 9 | 44.4 | 46.6 | $-7.15 | -7.9% | $992.85 | -0.2 | Thu 12:45 AM | too few trades (9/200) |
| reversal_15m_0.10pct | 14 | 50.0 | 51.2 | $-7.37 | -5.3% | $992.63 | -0.2 | Wed 12:45 PM | too few trades (14/200) |
| value_ev5 | 15 | 40.0 | 41.0 | $-9.26 | -6.2% | $990.74 | -0.2 | Wed 11:15 AM | too few trades (15/200) |
| momentum_5m_0.00pct | 24 | 45.8 | 55.0 | $-48.92 | -20.4% | $951.08 | -1.1 | Wed 3:45 AM | too few trades (24/200) |
| trend_filter | 10 | 30.0 | 58.0 | $-52.39 | -52.4% | $947.61 | -2.1 | Wed 9:15 PM | too few trades (10/200) |
| always_up | 24 | 37.5 | 52.2 | $-78.08 | -32.5% | $921.92 | -1.8 | Wed 3:45 AM | too few trades (24/200) |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 36 | 50.0 | 49.7 | $+16.89 |
| ETH | 39 | 38.5 | 49.1 | $-112.55 |
| SOL | 40 | 47.5 | 49.2 | $-41.85 |
| XRP | 43 | 53.5 | 49.4 | $+14.60 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
