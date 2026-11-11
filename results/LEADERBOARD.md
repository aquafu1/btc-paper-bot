# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 10, 7:15 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 17 windows, 390 settled trades, 68 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| coinflip | 60 | 56.7 | 51.3 | $+2.37 | +0.4% | $1002.37 | +0.0 | Wed 3:45 AM | too few trades (60/200) |
| reversal_60m_0.30pct | 26 | 50.0 | 49.8 | $-13.67 | -5.3% | $986.33 | -0.3 | Wed 8:15 PM | too few trades (26/200) |
| reversal_15m_0.10pct | 29 | 51.7 | 50.3 | $-15.09 | -5.2% | $984.91 | -0.3 | Wed 5:15 PM | too few trades (29/200) |
| momentum_60m_0.30pct | 26 | 50.0 | 52.0 | $-25.20 | -9.7% | $974.80 | -0.5 | Wed 8:15 PM | too few trades (26/200) |
| momentum_15m_0.10pct | 29 | 48.3 | 49.1 | $-27.18 | -9.4% | $972.82 | -0.5 | Wed 5:15 PM | too few trades (29/200) |
| trend_filter | 21 | 42.9 | 53.7 | $-57.92 | -27.6% | $942.08 | -1.5 | Thu 3:00 AM | too few trades (21/200) |
| value_ev10 | 28 | 32.1 | 38.0 | $-77.46 | -27.7% | $922.54 | -1.3 | Wed 6:15 PM | too few trades (28/200) |
| momentum_5m_0.00pct | 60 | 50.0 | 51.7 | $-81.80 | -13.6% | $918.20 | -1.2 | Wed 3:45 AM | too few trades (60/200) |
| value_ev20 | 15 | 13.3 | 34.5 | $-98.69 | -65.8% | $901.31 | -2.8 | Thu 5:15 PM | too few trades (15/200) |
| value_ev5 | 36 | 27.8 | 39.2 | $-138.96 | -38.6% | $861.04 | -2.3 | Wed 12:15 PM | too few trades (36/200) |
| always_up | 60 | 36.7 | 47.1 | $-194.41 | -32.4% | $805.59 | -2.7 | Wed 3:45 AM | too few trades (60/200) |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 82 | 45.1 | 47.9 | $-101.36 |
| ETH | 90 | 36.7 | 45.7 | $-295.87 |
| SOL | 109 | 46.8 | 48.8 | $-173.47 |
| XRP | 109 | 45.9 | 46.2 | $-157.32 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
