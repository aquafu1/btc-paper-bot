# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 10, 5:47 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 11 windows, 242 settled trades, 59 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| coinflip | 36 | 58.3 | 52.7 | $+26.61 | +7.4% | $1026.61 | +0.5 | Wed 3:45 AM | too few trades (36/200) |
| value_ev10 | 14 | 50.0 | 39.5 | $+23.07 | +16.5% | $1023.07 | +0.5 | Wed 11:30 PM | too few trades (14/200) |
| reversal_15m_0.10pct | 20 | 55.0 | 50.3 | $+13.89 | +6.9% | $1013.89 | +0.3 | Wed 1:45 PM | too few trades (20/200) |
| reversal_60m_0.30pct | 19 | 47.4 | 47.1 | $-7.03 | -3.7% | $992.97 | -0.2 | Wed 3:00 PM | too few trades (19/200) |
| value_ev20 | 6 | 33.3 | 35.7 | $-8.69 | -14.5% | $991.31 | -0.3 | Fri 6:15 PM | too few trades (6/200) |
| momentum_5m_0.00pct | 36 | 55.6 | 55.7 | $-9.35 | -2.6% | $990.65 | -0.2 | Wed 3:45 AM | too few trades (36/200) |
| momentum_60m_0.30pct | 19 | 52.6 | 55.5 | $-13.54 | -7.1% | $986.46 | -0.3 | Wed 3:00 PM | too few trades (19/200) |
| momentum_15m_0.10pct | 20 | 45.0 | 51.4 | $-26.65 | -13.3% | $973.35 | -0.6 | Wed 1:45 PM | too few trades (20/200) |
| value_ev5 | 19 | 36.8 | 40.9 | $-26.93 | -14.2% | $973.07 | -0.5 | Wed 3:00 PM | too few trades (19/200) |
| trend_filter | 17 | 47.1 | 58.6 | $-37.22 | -21.9% | $962.78 | -1.0 | Wed 5:45 PM | too few trades (17/200) |
| always_up | 36 | 38.9 | 50.7 | $-97.96 | -27.2% | $902.04 | -1.7 | Wed 3:45 AM | too few trades (36/200) |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 51 | 49.0 | 50.5 | $-0.53 |
| ETH | 58 | 44.8 | 50.3 | $-86.44 |
| SOL | 66 | 48.5 | 49.8 | $-76.25 |
| XRP | 67 | 52.2 | 49.3 | $-0.59 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
