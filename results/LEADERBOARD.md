# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 11, 3:35 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 50 windows, 1272 settled trades, 50 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 88 | 61.4 | 51.9 | $+132.30 | +15.0% | $1132.30 | +1.5 | Wed 7:15 PM | too few trades (88/200) |
| reversal_15m_0.10pct | 118 | 54.2 | 51.9 | $+20.56 | +1.7% | $1020.56 | +0.2 | Wed 12:15 PM | too few trades (118/200) |
| value_ev10 | 76 | 42.1 | 38.5 | $+16.16 | +2.1% | $1016.16 | +0.2 | Wed 11:30 PM | too few trades (76/200) |
| momentum_5m_0.00pct | 193 | 52.8 | 50.3 | $+13.52 | +0.7% | $1013.52 | +0.1 | Wed 4:00 AM | too few trades (193/200) |
| value_ev20 | 36 | 33.3 | 35.1 | $-34.23 | -9.5% | $965.77 | -0.4 | Fri 11:30 AM | too few trades (36/200) |
| value_ev5 | 99 | 38.4 | 39.8 | $-82.11 | -8.3% | $917.89 | -0.7 | Wed 4:00 PM | too few trades (99/200) |
| trend_filter | 70 | 42.9 | 48.1 | $-105.87 | -15.1% | $894.13 | -1.2 | Thu 2:15 AM | too few trades (70/200) |
| momentum_15m_0.10pct | 118 | 45.8 | 48.9 | $-110.10 | -9.3% | $889.90 | -1.0 | Wed 12:15 PM | too few trades (118/200) |
| coinflip | 193 | 50.3 | 51.4 | $-128.26 | -6.6% | $871.74 | -1.0 | Wed 4:00 AM | too few trades (193/200) |
| momentum_60m_0.30pct | 88 | 38.6 | 48.7 | $-196.96 | -22.4% | $803.04 | -2.1 | Wed 7:15 PM | too few trades (88/200) |
| always_up | 193 | 39.9 | 49.7 | $-463.33 | -24.0% | $536.67 | -3.4 | Wed 4:00 AM | too few trades (193/200) |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 258 | 46.1 | 48.8 | $-111.89 |
| ETH | 302 | 44.0 | 47.5 | $-283.04 |
| SOL | 352 | 46.6 | 47.4 | $-317.14 |
| XRP | 360 | 49.4 | 47.7 | $-226.24 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
