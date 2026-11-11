# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 10, 11:02 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 32 windows, 779 settled trades, 63 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 50 | 64.0 | 47.5 | $+149.63 | +29.9% | $1149.63 | +2.0 | Wed 9:15 PM | too few trades (50/200) |
| momentum_5m_0.00pct | 120 | 57.5 | 52.4 | $+77.88 | +6.5% | $1077.88 | +0.7 | Wed 3:45 AM | too few trades (120/200) |
| reversal_15m_0.10pct | 73 | 53.4 | 48.2 | $+63.63 | +8.7% | $1063.63 | +0.7 | Wed 12:00 PM | too few trades (73/200) |
| value_ev10 | 51 | 43.1 | 38.5 | $+16.35 | +3.2% | $1016.35 | +0.2 | Wed 8:45 PM | too few trades (51/200) |
| coinflip | 120 | 53.3 | 51.8 | $-8.41 | -0.7% | $991.59 | -0.1 | Wed 3:45 AM | too few trades (120/200) |
| value_ev5 | 63 | 41.3 | 39.5 | $-16.32 | -2.6% | $983.68 | -0.2 | Wed 3:15 PM | too few trades (63/200) |
| value_ev20 | 24 | 33.3 | 35.7 | $-26.85 | -11.2% | $973.15 | -0.4 | Fri 5:45 AM | too few trades (24/200) |
| trend_filter | 35 | 42.9 | 54.8 | $-90.80 | -25.9% | $909.20 | -1.7 | Thu 10:15 AM | too few trades (35/200) |
| momentum_15m_0.10pct | 73 | 46.6 | 52.6 | $-91.14 | -12.5% | $908.86 | -1.1 | Wed 12:00 PM | too few trades (73/200) |
| momentum_60m_0.30pct | 50 | 36.0 | 53.7 | $-176.97 | -35.4% | $823.03 | -2.8 | Wed 9:15 PM | too few trades (50/200) |
| always_up | 120 | 40.0 | 48.1 | $-243.31 | -20.3% | $756.69 | -2.2 | Wed 3:45 AM | too few trades (120/200) |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 170 | 48.2 | 49.0 | $-38.49 |
| ETH | 179 | 44.7 | 47.6 | $-160.48 |
| SOL | 215 | 49.3 | 47.9 | $-12.83 |
| XRP | 215 | 49.8 | 47.7 | $-134.52 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
