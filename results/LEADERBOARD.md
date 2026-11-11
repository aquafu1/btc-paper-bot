# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 11, 2:45 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 47 windows, 1164 settled trades, 61 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 80 | 61.3 | 50.9 | $+142.13 | +17.8% | $1142.13 | +1.6 | Wed 7:30 PM | too few trades (80/200) |
| momentum_5m_0.00pct | 180 | 54.4 | 51.7 | $+43.58 | +2.4% | $1043.58 | +0.3 | Wed 3:45 AM | too few trades (180/200) |
| value_ev10 | 68 | 44.1 | 39.3 | $+36.12 | +5.3% | $1036.12 | +0.4 | Thu 12:30 AM | too few trades (68/200) |
| reversal_15m_0.10pct | 109 | 51.4 | 50.8 | $-2.52 | -0.2% | $997.48 | -0.0 | Wed 12:00 PM | too few trades (109/200) |
| value_ev20 | 28 | 35.7 | 35.9 | $-14.27 | -5.1% | $985.73 | -0.2 | Fri 11:45 PM | too few trades (28/200) |
| value_ev5 | 89 | 40.4 | 40.5 | $-42.15 | -4.7% | $957.85 | -0.4 | Wed 4:45 PM | too few trades (89/200) |
| momentum_15m_0.10pct | 109 | 48.6 | 50.5 | $-44.05 | -4.0% | $955.95 | -0.4 | Wed 12:00 PM | too few trades (109/200) |
| trend_filter | 61 | 44.3 | 50.9 | $-91.85 | -15.1% | $908.15 | -1.2 | Thu 4:15 AM | too few trades (61/200) |
| coinflip | 180 | 50.0 | 51.3 | $-108.24 | -6.0% | $891.76 | -0.8 | Wed 3:45 AM | too few trades (180/200) |
| momentum_60m_0.30pct | 80 | 38.8 | 50.6 | $-192.94 | -24.1% | $807.06 | -2.2 | Wed 7:30 PM | too few trades (80/200) |
| always_up | 180 | 40.0 | 49.4 | $-403.42 | -22.4% | $596.58 | -3.1 | Wed 3:45 AM | too few trades (180/200) |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 241 | 45.6 | 49.1 | $-177.37 |
| ETH | 279 | 43.7 | 48.0 | $-324.43 |
| SOL | 322 | 48.1 | 48.5 | $-139.09 |
| XRP | 322 | 51.2 | 48.5 | $-36.72 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
