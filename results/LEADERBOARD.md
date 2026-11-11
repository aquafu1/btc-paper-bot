# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 11, 12:17 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 37 windows, 903 settled trades, 45 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 57 | 61.4 | 48.2 | $+127.20 | +22.3% | $1127.20 | +1.6 | Wed 10:00 PM | too few trades (57/200) |
| momentum_5m_0.00pct | 140 | 57.9 | 52.2 | $+97.41 | +7.0% | $1097.41 | +0.9 | Wed 3:45 AM | too few trades (140/200) |
| coinflip | 140 | 54.3 | 51.5 | $+12.06 | +0.9% | $1012.06 | +0.1 | Wed 3:45 AM | too few trades (140/200) |
| reversal_15m_0.10pct | 86 | 50.0 | 49.3 | $-0.60 | -0.1% | $999.40 | -0.0 | Wed 11:45 AM | too few trades (86/200) |
| value_ev10 | 57 | 40.4 | 38.7 | $-21.81 | -3.8% | $978.19 | -0.2 | Wed 10:00 PM | too few trades (57/200) |
| momentum_15m_0.10pct | 86 | 50.0 | 51.8 | $-38.59 | -4.5% | $961.41 | -0.4 | Wed 11:45 AM | too few trades (86/200) |
| value_ev20 | 26 | 30.8 | 35.7 | $-46.85 | -18.0% | $953.15 | -0.7 | Fri 10:45 AM | too few trades (26/200) |
| value_ev5 | 72 | 38.9 | 39.8 | $-63.46 | -8.8% | $936.54 | -0.6 | Wed 3:45 PM | too few trades (72/200) |
| trend_filter | 42 | 47.6 | 54.3 | $-71.16 | -16.9% | $928.84 | -1.2 | Thu 9:00 AM | too few trades (42/200) |
| momentum_60m_0.30pct | 57 | 38.6 | 53.1 | $-174.63 | -30.6% | $825.37 | -2.6 | Wed 10:00 PM | too few trades (57/200) |
| always_up | 140 | 44.3 | 48.7 | $-191.08 | -13.6% | $808.92 | -1.6 | Wed 3:45 AM | too few trades (140/200) |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 189 | 48.1 | 49.2 | $-57.71 |
| ETH | 213 | 45.1 | 47.6 | $-195.23 |
| SOL | 250 | 50.8 | 48.2 | $+21.75 |
| XRP | 251 | 50.6 | 48.1 | $-140.34 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
