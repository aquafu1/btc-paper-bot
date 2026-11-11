# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 10, 11:45 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 35 windows, 860 settled trades, 43 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 56 | 62.5 | 48.0 | $+137.20 | +24.5% | $1137.20 | +1.8 | Wed 8:45 PM | too few trades (56/200) |
| momentum_5m_0.00pct | 132 | 57.6 | 52.4 | $+74.82 | +5.7% | $1074.82 | +0.7 | Wed 3:45 AM | too few trades (132/200) |
| reversal_15m_0.10pct | 79 | 54.4 | 48.9 | $+69.40 | +8.8% | $1069.40 | +0.7 | Wed 12:15 PM | too few trades (79/200) |
| value_ev10 | 57 | 40.4 | 38.7 | $-21.81 | -3.8% | $978.19 | -0.2 | Wed 8:15 PM | too few trades (57/200) |
| coinflip | 132 | 53.0 | 51.5 | $-24.80 | -1.9% | $975.20 | -0.2 | Wed 3:45 AM | too few trades (132/200) |
| value_ev20 | 26 | 30.8 | 35.7 | $-46.85 | -18.0% | $953.15 | -0.7 | Fri 6:45 AM | too few trades (26/200) |
| value_ev5 | 71 | 39.4 | 39.7 | $-53.46 | -7.5% | $946.54 | -0.5 | Wed 2:30 PM | too few trades (71/200) |
| trend_filter | 40 | 45.0 | 54.5 | $-89.48 | -22.4% | $910.52 | -1.6 | Thu 8:30 AM | too few trades (40/200) |
| momentum_15m_0.10pct | 79 | 45.6 | 52.0 | $-108.29 | -13.7% | $891.71 | -1.2 | Wed 12:15 PM | too few trades (79/200) |
| momentum_60m_0.30pct | 56 | 37.5 | 53.2 | $-185.65 | -33.2% | $814.35 | -2.8 | Wed 8:45 PM | too few trades (56/200) |
| always_up | 132 | 40.9 | 48.6 | $-270.86 | -20.5% | $729.14 | -2.4 | Wed 3:45 AM | too few trades (132/200) |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 181 | 47.5 | 49.1 | $-83.25 |
| ETH | 202 | 44.6 | 47.4 | $-207.44 |
| SOL | 240 | 50.0 | 48.1 | $-16.11 |
| XRP | 237 | 48.9 | 47.9 | $-212.99 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
