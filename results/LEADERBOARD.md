# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 10, 4:32 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 6 windows, 102 settled trades, 56 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev10 | 7 | 71.4 | 38.1 | $+52.79 | +75.4% | $1052.79 | +1.6 | Wed 8:00 PM | too few trades (7/200) |
| coinflip | 16 | 68.8 | 54.7 | $+47.56 | +29.7% | $1047.56 | +1.2 | Wed 3:45 AM | too few trades (16/200) |
| value_ev5 | 10 | 50.0 | 39.9 | $+22.79 | +22.8% | $1022.79 | +0.6 | Wed 11:15 AM | too few trades (10/200) |
| value_ev20 | 3 | 66.7 | 35.7 | $+21.31 | +71.0% | $1021.31 | +0.8 | Fri 10:00 AM | too few trades (3/200) |
| momentum_15m_0.10pct | 8 | 50.0 | 45.5 | $+11.21 | +14.0% | $1011.21 | +0.3 | Wed 4:15 PM | too few trades (8/200) |
| reversal_60m_0.30pct | 6 | 50.0 | 51.1 | $+1.49 | +2.5% | $1001.49 | +0.1 | Thu 12:45 AM | too few trades (6/200) |
| momentum_60m_0.30pct | 6 | 50.0 | 52.4 | $-1.56 | -2.6% | $998.44 | -0.1 | Thu 12:45 AM | too few trades (6/200) |
| reversal_15m_0.10pct | 8 | 50.0 | 55.5 | $-2.86 | -3.6% | $997.14 | -0.1 | Wed 4:15 PM | too few trades (8/200) |
| always_up | 16 | 50.0 | 57.3 | $-19.45 | -12.2% | $980.55 | -0.5 | Wed 3:45 AM | too few trades (16/200) |
| trend_filter | 6 | 16.7 | 57.6 | $-42.19 | -70.3% | $957.81 | -2.4 | Thu 12:45 AM | too few trades (6/200) |
| momentum_5m_0.00pct | 16 | 31.2 | 53.6 | $-67.89 | -42.4% | $932.11 | -1.8 | Wed 3:45 AM | too few trades (16/200) |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 25 | 52.0 | 49.1 | $+24.41 |
| ETH | 24 | 41.7 | 50.2 | $-42.02 |
| SOL | 24 | 50.0 | 52.6 | $+9.26 |
| XRP | 29 | 55.2 | 48.2 | $+31.56 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
