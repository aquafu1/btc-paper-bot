# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 11, 1:17 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 41 windows, 1002 settled trades, 60 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_5m_0.00pct | 156 | 58.3 | 51.9 | $+147.56 | +9.5% | $1147.56 | +1.2 | Wed 3:45 AM | too few trades (156/200) |
| reversal_60m_0.30pct | 64 | 60.9 | 49.2 | $+129.14 | +20.2% | $1129.14 | +1.6 | Wed 9:45 PM | too few trades (64/200) |
| momentum_15m_0.10pct | 96 | 53.1 | 51.1 | $+40.81 | +4.3% | $1040.81 | +0.4 | Wed 11:45 AM | too few trades (96/200) |
| value_ev10 | 60 | 43.3 | 38.8 | $+21.63 | +3.6% | $1021.63 | +0.2 | Wed 11:45 PM | too few trades (60/200) |
| coinflip | 156 | 53.2 | 51.5 | $-5.72 | -0.4% | $994.28 | -0.0 | Wed 3:45 AM | too few trades (156/200) |
| value_ev5 | 78 | 41.0 | 40.0 | $-26.64 | -3.4% | $973.36 | -0.3 | Wed 4:15 PM | too few trades (78/200) |
| value_ev20 | 27 | 33.3 | 35.8 | $-31.24 | -11.6% | $968.76 | -0.5 | Fri 3:30 PM | too few trades (27/200) |
| trend_filter | 49 | 49.0 | 52.3 | $-38.83 | -7.9% | $961.17 | -0.6 | Thu 7:15 AM | too few trades (49/200) |
| reversal_15m_0.10pct | 96 | 46.9 | 50.0 | $-63.00 | -6.6% | $937.00 | -0.6 | Wed 11:45 AM | too few trades (96/200) |
| momentum_60m_0.30pct | 64 | 39.1 | 52.1 | $-171.19 | -26.7% | $828.81 | -2.3 | Wed 9:45 PM | too few trades (64/200) |
| always_up | 156 | 39.7 | 49.2 | $-351.08 | -22.5% | $648.92 | -2.8 | Wed 3:45 AM | too few trades (156/200) |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 205 | 46.8 | 49.1 | $-94.37 |
| ETH | 238 | 45.4 | 47.8 | $-178.00 |
| SOL | 279 | 50.2 | 48.4 | $-5.71 |
| XRP | 280 | 51.1 | 48.2 | $-70.48 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
