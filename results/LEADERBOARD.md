# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 10, 11:30 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 34 windows, 842 settled trades, 38 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 55 | 61.8 | 47.8 | $+132.19 | +24.0% | $1132.19 | +1.7 | Wed 8:30 PM | too few trades (55/200) |
| momentum_5m_0.00pct | 128 | 57.0 | 52.2 | $+71.04 | +5.5% | $1071.04 | +0.7 | Wed 3:45 AM | too few trades (128/200) |
| reversal_15m_0.10pct | 79 | 54.4 | 48.9 | $+69.40 | +8.8% | $1069.40 | +0.7 | Wed 11:45 AM | too few trades (79/200) |
| value_ev10 | 56 | 41.1 | 38.9 | $-11.81 | -2.1% | $988.19 | -0.1 | Wed 8:00 PM | too few trades (56/200) |
| coinflip | 128 | 53.1 | 51.6 | $-13.78 | -1.1% | $986.22 | -0.1 | Wed 3:45 AM | too few trades (128/200) |
| value_ev5 | 69 | 40.6 | 39.8 | $-33.46 | -4.8% | $966.54 | -0.3 | Wed 2:30 PM | too few trades (69/200) |
| value_ev20 | 25 | 32.0 | 35.8 | $-36.85 | -14.7% | $963.15 | -0.6 | Fri 7:15 AM | too few trades (25/200) |
| trend_filter | 40 | 45.0 | 54.5 | $-89.48 | -22.4% | $910.52 | -1.6 | Thu 7:15 AM | too few trades (40/200) |
| momentum_15m_0.10pct | 79 | 45.6 | 52.0 | $-108.29 | -13.7% | $891.71 | -1.2 | Wed 11:45 AM | too few trades (79/200) |
| momentum_60m_0.30pct | 55 | 38.2 | 53.6 | $-175.65 | -31.9% | $824.35 | -2.7 | Wed 8:30 PM | too few trades (55/200) |
| always_up | 128 | 39.1 | 48.2 | $-289.08 | -22.6% | $710.92 | -2.5 | Wed 3:45 AM | too few trades (128/200) |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 178 | 47.2 | 49.1 | $-82.83 |
| ETH | 196 | 44.4 | 47.5 | $-189.40 |
| SOL | 234 | 49.6 | 48.0 | $-16.12 |
| XRP | 234 | 49.1 | 48.0 | $-197.43 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
