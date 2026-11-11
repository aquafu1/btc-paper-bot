# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 11, 12:45 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 39 windows, 948 settled trades, 54 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 61 | 63.9 | 48.6 | $+159.14 | +26.1% | $1159.14 | +2.0 | Wed 9:45 PM | too few trades (61/200) |
| momentum_5m_0.00pct | 148 | 58.1 | 52.3 | $+105.55 | +7.1% | $1105.55 | +0.9 | Wed 3:45 AM | too few trades (148/200) |
| coinflip | 148 | 54.1 | 51.4 | $+5.52 | +0.4% | $1005.52 | +0.0 | Wed 3:45 AM | too few trades (148/200) |
| reversal_15m_0.10pct | 90 | 50.0 | 49.3 | $-3.00 | -0.3% | $997.00 | -0.0 | Wed 12:00 PM | too few trades (90/200) |
| value_ev10 | 57 | 40.4 | 38.7 | $-21.81 | -3.8% | $978.19 | -0.2 | Wed 11:45 PM | too few trades (57/200) |
| momentum_15m_0.10pct | 90 | 50.0 | 52.0 | $-45.39 | -5.0% | $954.61 | -0.5 | Wed 12:00 PM | too few trades (90/200) |
| value_ev20 | 26 | 30.8 | 35.7 | $-46.85 | -18.0% | $953.15 | -0.7 | Fri 2:30 PM | too few trades (26/200) |
| value_ev5 | 74 | 37.8 | 39.9 | $-83.46 | -11.3% | $916.54 | -0.8 | Wed 4:15 PM | too few trades (74/200) |
| trend_filter | 45 | 44.4 | 54.0 | $-101.16 | -22.5% | $898.84 | -1.7 | Thu 8:30 AM | too few trades (45/200) |
| momentum_60m_0.30pct | 61 | 36.1 | 52.8 | $-214.63 | -35.2% | $785.37 | -3.1 | Wed 9:45 PM | too few trades (61/200) |
| always_up | 148 | 41.9 | 48.7 | $-271.08 | -18.3% | $728.92 | -2.2 | Wed 3:45 AM | too few trades (148/200) |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 196 | 46.9 | 49.2 | $-110.70 |
| ETH | 222 | 45.0 | 47.7 | $-215.81 |
| SOL | 266 | 50.0 | 48.4 | $-34.28 |
| XRP | 264 | 50.4 | 48.3 | $-156.40 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
