# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 10, 4:45 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 7 windows, 122 settled trades, 62 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev10 | 8 | 62.5 | 38.8 | $+42.79 | +53.5% | $1042.79 | +1.2 | Wed 10:30 PM | too few trades (8/200) |
| coinflip | 20 | 65.0 | 53.9 | $+41.69 | +20.8% | $1041.69 | +1.0 | Wed 3:45 AM | too few trades (20/200) |
| value_ev20 | 3 | 66.7 | 35.7 | $+21.31 | +71.0% | $1021.31 | +0.8 | Sat 2:45 AM | too few trades (3/200) |
| reversal_15m_0.10pct | 10 | 60.0 | 56.1 | $+11.26 | +11.3% | $1011.26 | +0.4 | Wed 4:15 PM | too few trades (10/200) |
| value_ev5 | 12 | 41.7 | 40.8 | $+2.79 | +2.3% | $1002.79 | +0.1 | Wed 12:15 PM | too few trades (12/200) |
| reversal_60m_0.30pct | 6 | 50.0 | 51.1 | $+1.49 | +2.5% | $1001.49 | +0.1 | Thu 9:00 AM | too few trades (6/200) |
| momentum_60m_0.30pct | 6 | 50.0 | 52.4 | $-1.56 | -2.6% | $998.44 | -0.1 | Thu 9:00 AM | too few trades (6/200) |
| momentum_15m_0.10pct | 10 | 40.0 | 46.0 | $-8.79 | -8.8% | $991.21 | -0.2 | Wed 4:15 PM | too few trades (10/200) |
| trend_filter | 7 | 14.3 | 55.9 | $-52.19 | -74.6% | $947.81 | -2.9 | Thu 3:00 AM | too few trades (7/200) |
| momentum_5m_0.00pct | 20 | 40.0 | 53.9 | $-56.67 | -28.3% | $943.33 | -1.4 | Wed 3:45 AM | too few trades (20/200) |
| always_up | 20 | 40.0 | 54.8 | $-59.45 | -29.7% | $940.55 | -1.5 | Wed 3:45 AM | too few trades (20/200) |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 28 | 50.0 | 49.2 | $+11.42 |
| ETH | 29 | 37.9 | 49.7 | $-75.28 |
| SOL | 29 | 51.7 | 52.8 | $+11.68 |
| XRP | 36 | 50.0 | 48.6 | $-5.14 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
