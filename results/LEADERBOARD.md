# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 10, 9:02 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 24 windows, 583 settled trades, 54 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 37 | 59.5 | 47.9 | $+93.57 | +25.3% | $1093.57 | +1.4 | Wed 9:00 PM | too few trades (37/200) |
| momentum_5m_0.00pct | 88 | 59.1 | 51.5 | $+90.28 | +10.3% | $1090.28 | +1.0 | Wed 3:45 AM | too few trades (88/200) |
| coinflip | 88 | 55.7 | 51.9 | $+26.38 | +3.0% | $1026.38 | +0.3 | Wed 3:45 AM | too few trades (88/200) |
| momentum_15m_0.10pct | 52 | 51.9 | 51.0 | $+3.99 | +0.8% | $1003.99 | +0.1 | Wed 12:30 PM | too few trades (52/200) |
| value_ev10 | 41 | 41.5 | 39.0 | $-8.20 | -2.0% | $991.80 | -0.1 | Wed 6:15 PM | too few trades (41/200) |
| reversal_15m_0.10pct | 52 | 48.1 | 49.2 | $-12.22 | -2.3% | $987.78 | -0.2 | Wed 12:30 PM | too few trades (52/200) |
| value_ev5 | 51 | 39.2 | 39.8 | $-43.06 | -8.4% | $956.94 | -0.5 | Wed 1:00 PM | too few trades (51/200) |
| value_ev20 | 21 | 28.6 | 35.6 | $-50.76 | -24.2% | $949.24 | -0.9 | Thu 7:45 PM | too few trades (21/200) |
| trend_filter | 28 | 42.9 | 54.1 | $-64.09 | -22.9% | $935.91 | -1.3 | Thu 6:45 AM | too few trades (28/200) |
| momentum_60m_0.30pct | 37 | 40.5 | 53.6 | $-90.31 | -24.4% | $909.69 | -1.6 | Wed 9:00 PM | too few trades (37/200) |
| always_up | 88 | 40.9 | 47.9 | $-161.54 | -18.4% | $838.46 | -1.7 | Wed 3:45 AM | too few trades (88/200) |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 130 | 47.7 | 48.9 | $-37.37 |
| ETH | 135 | 42.2 | 47.0 | $-219.49 |
| SOL | 159 | 51.6 | 47.6 | $+94.03 |
| XRP | 159 | 50.3 | 47.4 | $-53.14 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
