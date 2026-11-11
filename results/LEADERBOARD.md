# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 10, 8:00 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 20 windows, 489 settled trades, 47 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| coinflip | 72 | 56.9 | 51.7 | $+22.03 | +3.1% | $1022.03 | +0.3 | Wed 3:45 AM | too few trades (72/200) |
| reversal_60m_0.30pct | 31 | 51.6 | 48.5 | $+19.48 | +6.3% | $1019.48 | +0.3 | Wed 8:30 PM | too few trades (31/200) |
| momentum_5m_0.00pct | 72 | 55.6 | 51.7 | $+2.06 | +0.3% | $1002.06 | +0.0 | Wed 3:45 AM | too few trades (72/200) |
| momentum_15m_0.10pct | 40 | 52.5 | 51.0 | $-3.70 | -0.9% | $996.30 | -0.1 | Wed 1:45 PM | too few trades (40/200) |
| reversal_15m_0.10pct | 40 | 47.5 | 48.4 | $-18.00 | -4.5% | $982.00 | -0.3 | Wed 1:45 PM | too few trades (40/200) |
| value_ev10 | 38 | 39.5 | 38.6 | $-24.64 | -6.5% | $975.36 | -0.3 | Wed 3:00 PM | too few trades (38/200) |
| momentum_60m_0.30pct | 31 | 48.4 | 52.6 | $-30.31 | -9.8% | $969.69 | -0.6 | Wed 8:30 PM | too few trades (31/200) |
| trend_filter | 26 | 46.2 | 53.7 | $-44.09 | -17.0% | $955.91 | -0.9 | Thu 2:00 AM | too few trades (26/200) |
| value_ev20 | 21 | 28.6 | 35.6 | $-50.76 | -24.2% | $949.24 | -0.9 | Thu 10:15 AM | too few trades (21/200) |
| value_ev5 | 46 | 34.8 | 39.5 | $-86.14 | -18.7% | $913.86 | -1.1 | Wed 11:00 AM | too few trades (46/200) |
| always_up | 72 | 41.7 | 47.7 | $-143.51 | -19.9% | $856.49 | -1.7 | Wed 3:45 AM | too few trades (72/200) |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 105 | 47.6 | 48.3 | $-49.96 |
| ETH | 111 | 41.4 | 46.4 | $-232.79 |
| SOL | 137 | 48.9 | 47.5 | $-16.80 |
| XRP | 136 | 50.0 | 46.8 | $-58.04 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
