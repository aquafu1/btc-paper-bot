# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 10, 7:47 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 19 windows, 458 settled trades, 58 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 36 | 52.8 | 49.2 | $+22.00 | +6.1% | $1022.00 | +0.3 | Wed 3:00 PM | too few trades (36/200) |
| reversal_60m_0.30pct | 31 | 51.6 | 48.5 | $+19.48 | +6.3% | $1019.48 | +0.3 | Wed 6:45 PM | too few trades (31/200) |
| value_ev10 | 34 | 44.1 | 38.2 | $+15.36 | +4.5% | $1015.36 | +0.2 | Wed 4:15 PM | too few trades (34/200) |
| coinflip | 68 | 55.9 | 51.5 | $+13.93 | +2.0% | $1013.93 | +0.2 | Wed 3:45 AM | too few trades (68/200) |
| momentum_5m_0.00pct | 68 | 52.9 | 51.1 | $-21.75 | -3.2% | $978.25 | -0.3 | Wed 3:45 AM | too few trades (68/200) |
| momentum_15m_0.10pct | 36 | 47.2 | 50.0 | $-27.51 | -7.6% | $972.49 | -0.4 | Wed 3:00 PM | too few trades (36/200) |
| momentum_60m_0.30pct | 31 | 48.4 | 52.6 | $-30.31 | -9.8% | $969.69 | -0.6 | Wed 6:45 PM | too few trades (31/200) |
| value_ev20 | 19 | 31.6 | 35.0 | $-30.76 | -16.2% | $969.24 | -0.5 | Thu 12:00 PM | too few trades (19/200) |
| value_ev5 | 42 | 38.1 | 39.2 | $-46.14 | -11.0% | $953.86 | -0.6 | Wed 11:30 AM | too few trades (42/200) |
| trend_filter | 25 | 44.0 | 53.4 | $-49.79 | -19.9% | $950.21 | -1.0 | Thu 1:15 AM | too few trades (25/200) |
| always_up | 68 | 38.2 | 47.1 | $-167.32 | -24.6% | $832.68 | -2.0 | Wed 3:45 AM | too few trades (68/200) |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 98 | 46.9 | 48.1 | $-45.81 |
| ETH | 103 | 39.8 | 46.0 | $-231.29 |
| SOL | 129 | 49.6 | 47.5 | $+16.10 |
| XRP | 128 | 50.0 | 46.5 | $-41.82 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
