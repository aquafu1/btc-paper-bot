# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 11, 3:50 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 51 windows, 1300 settled trades, 46 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 91 | 62.6 | 51.5 | $+172.75 | +19.0% | $1172.75 | +1.8 | Wed 6:15 PM | too few trades (91/200) |
| value_ev10 | 79 | 44.3 | 38.6 | $+56.61 | +7.2% | $1056.61 | +0.5 | Wed 10:30 PM | too few trades (79/200) |
| reversal_15m_0.10pct | 119 | 54.6 | 51.9 | $+30.64 | +2.6% | $1030.64 | +0.3 | Wed 12:00 PM | too few trades (119/200) |
| value_ev20 | 38 | 36.8 | 35.4 | $-3.85 | -1.0% | $996.15 | -0.0 | Fri 7:45 AM | too few trades (38/200) |
| momentum_5m_0.00pct | 196 | 52.0 | 50.4 | $-16.48 | -0.8% | $983.52 | -0.1 | Wed 3:45 AM | too few trades (196/200) |
| value_ev5 | 102 | 40.2 | 39.9 | $-41.65 | -4.1% | $958.35 | -0.3 | Wed 3:30 PM | too few trades (102/200) |
| momentum_15m_0.10pct | 119 | 45.4 | 48.9 | $-120.10 | -10.1% | $879.90 | -1.1 | Wed 12:00 PM | too few trades (119/200) |
| trend_filter | 73 | 41.1 | 48.5 | $-135.87 | -18.6% | $864.13 | -1.5 | Thu 1:00 AM | too few trades (73/200) |
| coinflip | 196 | 49.5 | 51.5 | $-158.26 | -8.1% | $841.74 | -1.2 | Wed 3:45 AM | too few trades (196/200) |
| momentum_60m_0.30pct | 91 | 37.4 | 49.0 | $-226.96 | -24.9% | $773.04 | -2.3 | Wed 6:15 PM | too few trades (91/200) |
| always_up | 196 | 40.8 | 49.6 | $-422.88 | -21.6% | $577.12 | -3.1 | Wed 3:45 AM | too few trades (196/200) |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 267 | 46.4 | 48.8 | $-72.72 |
| ETH | 312 | 44.2 | 47.7 | $-282.67 |
| SOL | 361 | 46.8 | 47.4 | $-284.41 |
| XRP | 360 | 49.4 | 47.7 | $-226.24 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
