# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 10, 9:30 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 26 windows, 637 settled trades, 58 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 38 | 57.9 | 47.9 | $+83.57 | +22.0% | $1083.57 | +1.2 | Wed 11:00 PM | too few trades (38/200) |
| reversal_15m_0.10pct | 60 | 55.0 | 49.1 | $+73.65 | +12.3% | $1073.65 | +0.9 | Wed 11:15 AM | too few trades (60/200) |
| value_ev10 | 46 | 45.7 | 39.4 | $+36.62 | +8.0% | $1036.62 | +0.4 | Wed 5:30 PM | too few trades (46/200) |
| coinflip | 96 | 55.2 | 51.8 | $+30.47 | +3.2% | $1030.47 | +0.3 | Wed 3:45 AM | too few trades (96/200) |
| momentum_5m_0.00pct | 96 | 55.2 | 51.8 | $+28.20 | +2.9% | $1028.20 | +0.3 | Wed 3:45 AM | too few trades (96/200) |
| value_ev5 | 57 | 42.1 | 40.2 | $-8.24 | -1.4% | $991.76 | -0.1 | Wed 12:30 PM | too few trades (57/200) |
| value_ev20 | 22 | 31.8 | 35.8 | $-36.58 | -16.6% | $963.42 | -0.6 | Thu 10:00 PM | too few trades (22/200) |
| trend_filter | 28 | 42.9 | 54.1 | $-64.09 | -22.9% | $935.91 | -1.3 | Thu 10:15 AM | too few trades (28/200) |
| momentum_15m_0.10pct | 60 | 45.0 | 51.5 | $-76.01 | -12.7% | $923.99 | -1.0 | Wed 11:15 AM | too few trades (60/200) |
| momentum_60m_0.30pct | 38 | 42.1 | 53.7 | $-82.95 | -21.8% | $917.05 | -1.4 | Wed 11:00 PM | too few trades (38/200) |
| always_up | 96 | 41.7 | 48.7 | $-170.50 | -17.8% | $829.50 | -1.7 | Wed 3:45 AM | too few trades (96/200) |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 143 | 49.0 | 49.0 | $+5.36 |
| ETH | 149 | 41.6 | 47.3 | $-259.62 |
| SOL | 172 | 51.2 | 47.9 | $+97.93 |
| XRP | 173 | 50.9 | 47.7 | $-29.54 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
