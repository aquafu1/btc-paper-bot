# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 10, 8:47 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 23 windows, 557 settled trades, 55 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_5m_0.00pct | 84 | 58.3 | 51.8 | $+58.13 | +6.9% | $1058.13 | +0.7 | Wed 3:45 AM | too few trades (84/200) |
| reversal_60m_0.30pct | 34 | 55.9 | 48.7 | $+49.32 | +14.5% | $1049.32 | +0.8 | Wed 10:15 PM | too few trades (34/200) |
| coinflip | 84 | 56.0 | 51.9 | $+19.41 | +2.3% | $1019.41 | +0.2 | Wed 3:45 AM | too few trades (84/200) |
| momentum_15m_0.10pct | 50 | 52.0 | 51.0 | $-1.18 | -0.2% | $998.82 | -0.0 | Wed 12:15 PM | too few trades (50/200) |
| reversal_15m_0.10pct | 50 | 48.0 | 49.3 | $-19.49 | -3.9% | $980.51 | -0.3 | Wed 12:15 PM | too few trades (50/200) |
| value_ev10 | 40 | 40.0 | 39.0 | $-24.16 | -6.0% | $975.84 | -0.3 | Wed 5:30 PM | too few trades (40/200) |
| value_ev20 | 21 | 28.6 | 35.6 | $-50.76 | -24.2% | $949.24 | -0.9 | Thu 5:15 PM | too few trades (21/200) |
| trend_filter | 27 | 44.4 | 53.7 | $-54.09 | -20.0% | $945.91 | -1.1 | Thu 6:15 AM | too few trades (27/200) |
| momentum_60m_0.30pct | 34 | 44.1 | 52.7 | $-60.31 | -17.7% | $939.69 | -1.1 | Wed 10:15 PM | too few trades (34/200) |
| value_ev5 | 49 | 36.7 | 39.8 | $-74.19 | -15.1% | $925.81 | -0.9 | Wed 12:45 PM | too few trades (49/200) |
| always_up | 84 | 38.1 | 48.3 | $-220.97 | -26.3% | $779.03 | -2.4 | Wed 3:45 AM | too few trades (84/200) |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 122 | 48.4 | 48.8 | $-39.19 |
| ETH | 129 | 41.1 | 47.0 | $-260.18 |
| SOL | 152 | 50.0 | 48.0 | $+8.29 |
| XRP | 154 | 49.4 | 47.4 | $-87.23 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
