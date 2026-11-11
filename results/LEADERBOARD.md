# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 11, 1:45 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 43 windows, 1062 settled trades, 40 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 72 | 59.7 | 50.2 | $+117.27 | +16.3% | $1117.27 | +1.4 | Wed 7:45 PM | too few trades (72/200) |
| momentum_5m_0.00pct | 164 | 56.1 | 51.9 | $+89.39 | +5.5% | $1089.39 | +0.7 | Wed 3:45 AM | too few trades (164/200) |
| value_ev10 | 64 | 45.3 | 39.0 | $+53.82 | +8.4% | $1053.82 | +0.5 | Wed 11:30 PM | too few trades (64/200) |
| momentum_15m_0.10pct | 98 | 52.0 | 51.1 | $+20.81 | +2.1% | $1020.81 | +0.2 | Wed 12:15 PM | too few trades (98/200) |
| value_ev20 | 28 | 35.7 | 35.9 | $-14.27 | -5.1% | $985.73 | -0.2 | Fri 4:30 PM | too few trades (28/200) |
| value_ev5 | 84 | 41.7 | 40.2 | $-14.45 | -1.7% | $985.55 | -0.1 | Wed 3:45 PM | too few trades (84/200) |
| coinflip | 164 | 52.4 | 51.5 | $-24.12 | -1.5% | $975.88 | -0.2 | Wed 3:45 AM | too few trades (164/200) |
| reversal_15m_0.10pct | 98 | 48.0 | 50.1 | $-48.38 | -4.9% | $951.62 | -0.5 | Wed 12:15 PM | too few trades (98/200) |
| trend_filter | 54 | 46.3 | 51.7 | $-67.00 | -12.4% | $933.00 | -0.9 | Thu 5:15 AM | too few trades (54/200) |
| momentum_60m_0.30pct | 72 | 40.3 | 51.2 | $-158.09 | -22.0% | $841.91 | -1.9 | Wed 7:45 PM | too few trades (72/200) |
| always_up | 164 | 40.2 | 49.6 | $-362.95 | -22.1% | $637.05 | -2.9 | Wed 3:45 AM | too few trades (164/200) |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 217 | 46.5 | 49.2 | $-120.61 |
| ETH | 253 | 45.1 | 47.8 | $-202.07 |
| SOL | 296 | 49.7 | 48.5 | $-16.80 |
| XRP | 296 | 51.0 | 48.4 | $-68.47 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
