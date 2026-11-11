# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 11, 2:20 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 45 windows, 1102 settled trades, 62 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 72 | 59.7 | 50.2 | $+117.27 | +16.3% | $1117.27 | +1.4 | Wed 9:15 PM | too few trades (72/200) |
| momentum_5m_0.00pct | 172 | 55.2 | 51.9 | $+61.13 | +3.6% | $1061.13 | +0.5 | Wed 3:45 AM | too few trades (172/200) |
| value_ev10 | 65 | 44.6 | 39.1 | $+43.82 | +6.7% | $1043.82 | +0.4 | Thu 12:30 AM | too few trades (65/200) |
| reversal_15m_0.10pct | 105 | 51.4 | 50.5 | $+6.49 | +0.6% | $1006.49 | +0.1 | Wed 11:45 AM | too few trades (105/200) |
| value_ev20 | 28 | 35.7 | 35.9 | $-14.27 | -5.1% | $985.73 | -0.2 | Fri 8:15 PM | too few trades (28/200) |
| value_ev5 | 85 | 41.2 | 40.3 | $-24.45 | -2.9% | $975.55 | -0.2 | Wed 4:45 PM | too few trades (85/200) |
| momentum_15m_0.10pct | 105 | 48.6 | 50.9 | $-49.19 | -4.7% | $950.81 | -0.5 | Wed 11:45 AM | too few trades (105/200) |
| trend_filter | 54 | 46.3 | 51.7 | $-67.00 | -12.4% | $933.00 | -0.9 | Thu 7:15 AM | too few trades (54/200) |
| coinflip | 172 | 51.2 | 51.5 | $-71.03 | -4.1% | $928.97 | -0.6 | Wed 3:45 AM | too few trades (172/200) |
| momentum_60m_0.30pct | 72 | 40.3 | 51.2 | $-158.09 | -22.0% | $841.91 | -1.9 | Wed 9:15 PM | too few trades (72/200) |
| always_up | 172 | 40.7 | 49.6 | $-368.56 | -21.4% | $631.44 | -2.9 | Wed 3:45 AM | too few trades (172/200) |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 225 | 46.2 | 49.3 | $-147.79 |
| ETH | 263 | 44.9 | 47.9 | $-231.44 |
| SOL | 308 | 49.4 | 48.6 | $-48.54 |
| XRP | 306 | 50.7 | 48.5 | $-96.11 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
