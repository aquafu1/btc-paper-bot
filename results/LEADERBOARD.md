# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 11, 2:00 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 44 windows, 1084 settled trades, 54 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 72 | 59.7 | 50.2 | $+117.27 | +16.3% | $1117.27 | +1.4 | Wed 8:30 PM | too few trades (72/200) |
| momentum_5m_0.00pct | 168 | 56.5 | 51.9 | $+101.13 | +6.0% | $1101.13 | +0.8 | Wed 3:45 AM | too few trades (168/200) |
| value_ev10 | 65 | 44.6 | 39.1 | $+43.82 | +6.7% | $1043.82 | +0.4 | Wed 11:45 PM | too few trades (65/200) |
| value_ev20 | 28 | 35.7 | 35.9 | $-14.27 | -5.1% | $985.73 | -0.2 | Fri 6:15 PM | too few trades (28/200) |
| momentum_15m_0.10pct | 102 | 50.0 | 50.9 | $-19.19 | -1.9% | $980.81 | -0.2 | Wed 12:00 PM | too few trades (102/200) |
| reversal_15m_0.10pct | 102 | 50.0 | 50.4 | $-20.29 | -2.0% | $979.71 | -0.2 | Wed 12:00 PM | too few trades (102/200) |
| value_ev5 | 85 | 41.2 | 40.3 | $-24.45 | -2.9% | $975.55 | -0.2 | Wed 4:00 PM | too few trades (85/200) |
| coinflip | 168 | 52.4 | 51.5 | $-31.03 | -1.8% | $968.97 | -0.2 | Wed 3:45 AM | too few trades (168/200) |
| trend_filter | 54 | 46.3 | 51.7 | $-67.00 | -12.4% | $933.00 | -0.9 | Thu 6:15 AM | too few trades (54/200) |
| momentum_60m_0.30pct | 72 | 40.3 | 51.2 | $-158.09 | -22.0% | $841.91 | -1.9 | Wed 8:30 PM | too few trades (72/200) |
| always_up | 168 | 39.3 | 49.5 | $-402.95 | -24.0% | $597.05 | -3.2 | Wed 3:45 AM | too few trades (168/200) |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 222 | 46.4 | 49.3 | $-135.40 |
| ETH | 258 | 45.0 | 47.9 | $-217.29 |
| SOL | 303 | 49.5 | 48.5 | $-36.60 |
| XRP | 301 | 50.8 | 48.4 | $-85.76 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
