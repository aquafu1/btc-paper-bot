# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 10, 8:32 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 22 windows, 542 settled trades, 41 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_5m_0.00pct | 81 | 58.0 | 51.7 | $+50.83 | +6.3% | $1050.83 | +0.6 | Wed 4:15 AM | too few trades (81/200) |
| reversal_60m_0.30pct | 34 | 55.9 | 48.7 | $+49.32 | +14.5% | $1049.32 | +0.8 | Wed 10:15 PM | too few trades (34/200) |
| coinflip | 81 | 56.8 | 51.7 | $+32.59 | +4.0% | $1032.59 | +0.4 | Wed 4:15 AM | too few trades (81/200) |
| momentum_15m_0.10pct | 48 | 52.1 | 51.0 | $-1.67 | -0.3% | $998.33 | -0.0 | Wed 1:15 PM | too few trades (48/200) |
| reversal_15m_0.10pct | 48 | 47.9 | 49.2 | $-20.57 | -4.3% | $979.43 | -0.3 | Wed 1:15 PM | too few trades (48/200) |
| value_ev10 | 39 | 38.5 | 38.8 | $-34.64 | -8.9% | $965.36 | -0.5 | Wed 6:15 PM | too few trades (39/200) |
| value_ev20 | 21 | 28.6 | 35.6 | $-50.76 | -24.2% | $949.24 | -0.9 | Thu 5:15 PM | too few trades (21/200) |
| trend_filter | 27 | 44.4 | 53.7 | $-54.09 | -20.0% | $945.91 | -1.1 | Thu 6:15 AM | too few trades (27/200) |
| momentum_60m_0.30pct | 34 | 44.1 | 52.7 | $-60.31 | -17.7% | $939.69 | -1.1 | Wed 10:15 PM | too few trades (34/200) |
| value_ev5 | 48 | 35.4 | 39.7 | $-84.68 | -17.6% | $915.32 | -1.1 | Wed 1:15 PM | too few trades (48/200) |
| always_up | 81 | 38.3 | 48.3 | $-212.05 | -26.2% | $787.95 | -2.4 | Wed 4:15 AM | too few trades (81/200) |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 115 | 47.8 | 48.6 | $-51.13 |
| ETH | 124 | 41.1 | 46.8 | $-252.34 |
| SOL | 149 | 49.7 | 47.8 | $+4.66 |
| XRP | 154 | 49.4 | 47.4 | $-87.23 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
