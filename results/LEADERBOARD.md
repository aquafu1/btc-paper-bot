# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 10, 10:17 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 29 windows, 712 settled trades, 46 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 46 | 65.2 | 48.9 | $+151.65 | +33.0% | $1151.65 | +2.1 | Wed 8:45 PM | too few trades (46/200) |
| reversal_15m_0.10pct | 68 | 54.4 | 49.0 | $+75.66 | +11.1% | $1075.66 | +0.9 | Wed 11:15 AM | too few trades (68/200) |
| coinflip | 108 | 55.6 | 51.8 | $+43.03 | +4.0% | $1043.03 | +0.4 | Wed 3:45 AM | too few trades (108/200) |
| value_ev10 | 47 | 44.7 | 39.4 | $+26.62 | +5.7% | $1026.62 | +0.3 | Wed 8:00 PM | too few trades (47/200) |
| momentum_5m_0.00pct | 108 | 54.6 | 52.1 | $+15.03 | +1.4% | $1015.03 | +0.2 | Wed 3:45 AM | too few trades (108/200) |
| value_ev5 | 58 | 41.4 | 40.2 | $-18.24 | -3.1% | $981.76 | -0.2 | Wed 2:45 PM | too few trades (58/200) |
| value_ev20 | 22 | 31.8 | 35.8 | $-36.58 | -16.6% | $963.42 | -0.6 | Fri 4:45 AM | too few trades (22/200) |
| momentum_15m_0.10pct | 68 | 45.6 | 52.2 | $-87.75 | -12.9% | $912.25 | -1.1 | Wed 11:15 AM | too few trades (68/200) |
| trend_filter | 33 | 39.4 | 53.9 | $-96.78 | -29.3% | $903.22 | -1.8 | Thu 8:15 AM | too few trades (33/200) |
| momentum_60m_0.30pct | 46 | 34.8 | 53.1 | $-162.95 | -35.4% | $837.05 | -2.6 | Wed 8:45 PM | too few trades (46/200) |
| always_up | 108 | 38.9 | 48.8 | $-250.71 | -23.2% | $749.29 | -2.4 | Wed 3:45 AM | too few trades (108/200) |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 159 | 49.1 | 49.4 | $-4.37 |
| ETH | 166 | 42.8 | 47.8 | $-250.00 |
| SOL | 194 | 49.0 | 48.1 | $+7.23 |
| XRP | 193 | 49.7 | 48.2 | $-93.88 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
