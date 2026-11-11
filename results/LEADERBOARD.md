# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 10, 6:47 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 15 windows, 350 settled trades, 40 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| coinflip | 52 | 59.6 | 52.7 | $+32.82 | +6.3% | $1032.82 | +0.5 | Wed 3:45 AM | too few trades (52/200) |
| reversal_60m_0.30pct | 24 | 50.0 | 49.0 | $-7.72 | -3.2% | $992.28 | -0.2 | Wed 6:30 PM | too few trades (24/200) |
| momentum_15m_0.10pct | 28 | 50.0 | 49.4 | $-17.18 | -6.1% | $982.82 | -0.3 | Wed 2:30 PM | too few trades (28/200) |
| reversal_15m_0.10pct | 28 | 50.0 | 49.9 | $-20.47 | -7.3% | $979.53 | -0.4 | Wed 2:30 PM | too few trades (28/200) |
| momentum_60m_0.30pct | 24 | 50.0 | 53.3 | $-24.50 | -10.2% | $975.50 | -0.5 | Wed 6:30 PM | too few trades (24/200) |
| value_ev10 | 25 | 36.0 | 38.5 | $-47.46 | -19.0% | $952.54 | -0.8 | Wed 5:15 PM | too few trades (25/200) |
| trend_filter | 20 | 40.0 | 53.7 | $-67.22 | -33.6% | $932.78 | -1.8 | Wed 11:45 PM | too few trades (20/200) |
| momentum_5m_0.00pct | 52 | 48.1 | 51.4 | $-78.47 | -15.1% | $921.53 | -1.2 | Wed 3:45 AM | too few trades (52/200) |
| value_ev20 | 13 | 15.4 | 34.9 | $-78.69 | -60.5% | $921.31 | -2.3 | Thu 5:15 PM | too few trades (13/200) |
| value_ev5 | 32 | 31.2 | 39.9 | $-98.96 | -30.9% | $901.04 | -1.7 | Wed 11:45 AM | too few trades (32/200) |
| always_up | 52 | 42.3 | 48.8 | $-114.41 | -22.0% | $885.59 | -1.7 | Wed 3:45 AM | too few trades (52/200) |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 73 | 43.8 | 47.6 | $-104.76 |
| ETH | 82 | 39.0 | 46.1 | $-231.82 |
| SOL | 97 | 48.5 | 50.0 | $-109.56 |
| XRP | 98 | 49.0 | 47.3 | $-76.13 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
