# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 10, 7:02 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 16 windows, 372 settled trades, 52 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| coinflip | 56 | 58.9 | 52.1 | $+23.07 | +4.1% | $1023.07 | +0.3 | Wed 3:45 AM | too few trades (56/200) |
| reversal_60m_0.30pct | 25 | 52.0 | 49.7 | $-3.67 | -1.5% | $996.33 | -0.1 | Wed 7:15 PM | too few trades (25/200) |
| momentum_15m_0.10pct | 28 | 50.0 | 49.4 | $-17.18 | -6.1% | $982.82 | -0.3 | Wed 4:15 PM | too few trades (28/200) |
| reversal_15m_0.10pct | 28 | 50.0 | 49.9 | $-20.47 | -7.3% | $979.53 | -0.4 | Wed 4:15 PM | too few trades (28/200) |
| momentum_60m_0.30pct | 25 | 48.0 | 52.0 | $-34.50 | -13.8% | $965.50 | -0.7 | Wed 7:15 PM | too few trades (25/200) |
| trend_filter | 20 | 40.0 | 53.7 | $-67.22 | -33.6% | $932.78 | -1.8 | Thu 2:15 AM | too few trades (20/200) |
| value_ev10 | 28 | 32.1 | 38.0 | $-77.46 | -27.7% | $922.54 | -1.3 | Wed 4:15 PM | too few trades (28/200) |
| momentum_5m_0.00pct | 56 | 48.2 | 51.5 | $-90.98 | -16.2% | $909.02 | -1.3 | Wed 3:45 AM | too few trades (56/200) |
| value_ev20 | 15 | 13.3 | 34.5 | $-98.69 | -65.8% | $901.31 | -2.8 | Thu 2:00 PM | too few trades (15/200) |
| value_ev5 | 35 | 28.6 | 39.3 | $-128.96 | -36.8% | $871.04 | -2.1 | Wed 11:15 AM | too few trades (35/200) |
| always_up | 56 | 39.3 | 47.6 | $-154.41 | -27.6% | $845.59 | -2.2 | Wed 3:45 AM | too few trades (56/200) |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 76 | 43.4 | 47.6 | $-118.56 |
| ETH | 87 | 36.8 | 45.6 | $-281.82 |
| SOL | 105 | 47.6 | 49.2 | $-147.40 |
| XRP | 104 | 47.1 | 46.3 | $-122.69 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
