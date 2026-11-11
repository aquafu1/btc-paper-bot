# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 10, 9:15 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 25 windows, 612 settled trades, 56 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 37 | 59.5 | 47.9 | $+93.57 | +25.3% | $1093.57 | +1.4 | Wed 10:30 PM | too few trades (37/200) |
| momentum_5m_0.00pct | 92 | 56.5 | 51.9 | $+50.28 | +5.5% | $1050.28 | +0.5 | Wed 3:45 AM | too few trades (92/200) |
| value_ev10 | 45 | 46.7 | 39.2 | $+46.62 | +10.4% | $1046.62 | +0.6 | Wed 5:00 PM | too few trades (45/200) |
| reversal_15m_0.10pct | 56 | 51.8 | 48.6 | $+42.60 | +7.6% | $1042.60 | +0.5 | Wed 12:00 PM | too few trades (56/200) |
| coinflip | 92 | 55.4 | 51.8 | $+35.19 | +3.8% | $1035.19 | +0.4 | Wed 3:45 AM | too few trades (92/200) |
| value_ev5 | 55 | 43.6 | 40.0 | $+11.76 | +2.1% | $1011.76 | +0.1 | Wed 12:15 PM | too few trades (55/200) |
| momentum_15m_0.10pct | 56 | 48.2 | 51.7 | $-36.01 | -6.4% | $963.99 | -0.5 | Wed 12:00 PM | too few trades (56/200) |
| value_ev20 | 22 | 31.8 | 35.8 | $-36.58 | -16.6% | $963.42 | -0.6 | Thu 7:45 PM | too few trades (22/200) |
| trend_filter | 28 | 42.9 | 54.1 | $-64.09 | -22.9% | $935.91 | -1.3 | Thu 8:30 AM | too few trades (28/200) |
| momentum_60m_0.30pct | 37 | 40.5 | 53.6 | $-90.31 | -24.4% | $909.69 | -1.6 | Wed 10:30 PM | too few trades (37/200) |
| always_up | 92 | 39.1 | 48.4 | $-201.54 | -21.9% | $798.46 | -2.1 | Wed 3:45 AM | too few trades (92/200) |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 137 | 48.2 | 48.9 | $-6.33 |
| ETH | 142 | 42.3 | 47.2 | $-223.98 |
| SOL | 167 | 51.5 | 47.7 | $+110.76 |
| XRP | 166 | 50.6 | 47.5 | $-28.97 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
