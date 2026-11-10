# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 10, 4:15 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 5 windows, 78 settled trades, 44 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev10 | 4 | 100.0 | 38.8 | $+63.02 | +157.6% | $1063.02 | +51.7 | Thu 4:45 AM | too few trades (4/200) |
| coinflip | 12 | 66.7 | 51.8 | $+44.57 | +37.1% | $1044.57 | +1.2 | Wed 3:45 AM | too few trades (12/200) |
| value_ev5 | 6 | 66.7 | 42.1 | $+43.02 | +71.7% | $1043.02 | +1.3 | Wed 4:15 PM | too few trades (6/200) |
| value_ev20 | 2 | 100.0 | 39.0 | $+31.31 | +156.6% | $1031.31 | +56.8 | Fri 6:15 PM | too few trades (2/200) |
| momentum_15m_0.10pct | 6 | 66.7 | 48.0 | $+31.21 | +52.0% | $1031.21 | +1.1 | Wed 4:15 PM | too few trades (6/200) |
| reversal_60m_0.30pct | 6 | 50.0 | 51.1 | $+1.49 | +2.5% | $1001.49 | +0.1 | Wed 4:15 PM | too few trades (6/200) |
| momentum_60m_0.30pct | 6 | 50.0 | 52.4 | $-1.56 | -2.6% | $998.44 | -0.1 | Wed 4:15 PM | too few trades (6/200) |
| reversal_15m_0.10pct | 6 | 33.3 | 54.2 | $-16.26 | -27.1% | $983.74 | -0.6 | Wed 4:15 PM | too few trades (6/200) |
| trend_filter | 6 | 16.7 | 57.6 | $-42.19 | -70.3% | $957.81 | -2.4 | Wed 4:15 PM | too few trades (6/200) |
| always_up | 12 | 33.3 | 55.5 | $-42.21 | -35.2% | $957.79 | -1.3 | Wed 3:45 AM | too few trades (12/200) |
| momentum_5m_0.00pct | 12 | 25.0 | 53.5 | $-56.30 | -46.9% | $943.70 | -1.7 | Wed 3:45 AM | too few trades (12/200) |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 21 | 47.6 | 48.1 | $+20.03 |
| ETH | 19 | 42.1 | 52.1 | $-21.18 |
| SOL | 17 | 47.1 | 52.6 | $+0.16 |
| XRP | 21 | 57.1 | 50.4 | $+57.09 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
