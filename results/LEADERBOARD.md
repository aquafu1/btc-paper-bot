# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 10, 6:30 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 14 windows, 328 settled trades, 44 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| coinflip | 48 | 60.4 | 52.5 | $+37.69 | +7.9% | $1037.69 | +0.6 | Wed 3:45 AM | too few trades (48/200) |
| reversal_60m_0.30pct | 22 | 50.0 | 48.5 | $-3.91 | -1.8% | $996.09 | -0.1 | Wed 6:45 PM | too few trades (22/200) |
| reversal_15m_0.10pct | 27 | 51.9 | 49.6 | $-10.47 | -3.9% | $989.53 | -0.2 | Wed 1:30 PM | too few trades (27/200) |
| momentum_60m_0.30pct | 22 | 50.0 | 53.8 | $-23.01 | -10.5% | $976.99 | -0.5 | Wed 6:45 PM | too few trades (22/200) |
| momentum_15m_0.10pct | 27 | 48.1 | 49.6 | $-28.55 | -10.6% | $971.45 | -0.6 | Wed 1:30 PM | too few trades (27/200) |
| value_ev10 | 24 | 37.5 | 38.3 | $-37.46 | -15.6% | $962.54 | -0.7 | Wed 4:15 PM | too few trades (24/200) |
| trend_filter | 20 | 40.0 | 53.7 | $-67.22 | -33.6% | $932.78 | -1.8 | Wed 9:15 PM | too few trades (20/200) |
| value_ev20 | 12 | 16.7 | 34.3 | $-68.69 | -57.2% | $931.31 | -2.0 | Thu 5:15 PM | too few trades (12/200) |
| momentum_5m_0.00pct | 48 | 47.9 | 51.3 | $-76.03 | -15.8% | $923.97 | -1.2 | Wed 3:45 AM | too few trades (48/200) |
| value_ev5 | 30 | 30.0 | 39.4 | $-97.46 | -32.5% | $902.54 | -1.7 | Wed 11:15 AM | too few trades (30/200) |
| always_up | 48 | 41.7 | 48.5 | $-111.85 | -23.3% | $888.15 | -1.7 | Wed 3:45 AM | too few trades (48/200) |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 68 | 44.1 | 47.2 | $-97.49 |
| ETH | 79 | 38.0 | 45.8 | $-239.69 |
| SOL | 91 | 48.4 | 49.8 | $-105.06 |
| XRP | 90 | 50.0 | 47.1 | $-44.71 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
