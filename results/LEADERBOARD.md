# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 11, 12:30 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 38 windows, 926 settled trades, 39 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 59 | 62.7 | 48.3 | $+144.80 | +24.5% | $1144.80 | +1.8 | Wed 10:00 PM | too few trades (59/200) |
| momentum_5m_0.00pct | 144 | 57.6 | 52.2 | $+95.34 | +6.6% | $1095.34 | +0.8 | Wed 3:45 AM | too few trades (144/200) |
| coinflip | 144 | 54.9 | 51.6 | $+27.91 | +1.9% | $1027.91 | +0.2 | Wed 3:45 AM | too few trades (144/200) |
| reversal_15m_0.10pct | 88 | 51.1 | 49.4 | $+17.00 | +1.9% | $1017.00 | +0.2 | Wed 11:45 AM | too few trades (88/200) |
| value_ev10 | 57 | 40.4 | 38.7 | $-21.81 | -3.8% | $978.19 | -0.2 | Wed 11:00 PM | too few trades (57/200) |
| value_ev20 | 26 | 30.8 | 35.7 | $-46.85 | -18.0% | $953.15 | -0.7 | Fri 12:30 PM | too few trades (26/200) |
| momentum_15m_0.10pct | 88 | 48.9 | 51.8 | $-58.59 | -6.7% | $941.41 | -0.6 | Wed 11:45 AM | too few trades (88/200) |
| value_ev5 | 73 | 38.4 | 39.9 | $-73.46 | -10.1% | $926.54 | -0.7 | Wed 4:00 PM | too few trades (73/200) |
| trend_filter | 44 | 45.5 | 54.1 | $-91.16 | -20.7% | $908.84 | -1.5 | Thu 8:15 AM | too few trades (44/200) |
| momentum_60m_0.30pct | 59 | 37.3 | 53.0 | $-194.63 | -33.0% | $805.37 | -2.8 | Wed 10:00 PM | too few trades (59/200) |
| always_up | 144 | 43.1 | 48.7 | $-231.08 | -16.0% | $768.92 | -1.9 | Wed 3:45 AM | too few trades (144/200) |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 193 | 47.2 | 49.1 | $-97.71 |
| ETH | 217 | 45.2 | 47.7 | $-198.73 |
| SOL | 258 | 50.4 | 48.3 | $-4.48 |
| XRP | 258 | 50.8 | 48.2 | $-131.62 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
