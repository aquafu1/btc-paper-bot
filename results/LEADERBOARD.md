# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 10, 11:15 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 33 windows, 813 settled trades, 47 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 53 | 62.3 | 47.4 | $+135.57 | +25.6% | $1135.57 | +1.8 | Wed 8:30 PM | too few trades (53/200) |
| reversal_15m_0.10pct | 76 | 55.3 | 48.6 | $+82.78 | +10.9% | $1082.78 | +0.9 | Wed 11:45 AM | too few trades (76/200) |
| momentum_5m_0.00pct | 124 | 57.3 | 52.4 | $+68.18 | +5.5% | $1068.18 | +0.6 | Wed 3:45 AM | too few trades (124/200) |
| value_ev10 | 54 | 40.7 | 38.6 | $-13.65 | -2.5% | $986.35 | -0.2 | Wed 8:00 PM | too few trades (54/200) |
| coinflip | 124 | 52.4 | 51.6 | $-33.26 | -2.7% | $966.74 | -0.3 | Wed 3:45 AM | too few trades (124/200) |
| value_ev20 | 25 | 32.0 | 35.8 | $-36.85 | -14.7% | $963.15 | -0.6 | Fri 5:15 AM | too few trades (25/200) |
| value_ev5 | 66 | 39.4 | 39.5 | $-46.32 | -7.0% | $953.68 | -0.5 | Wed 2:45 PM | too few trades (66/200) |
| trend_filter | 38 | 44.7 | 54.8 | $-90.50 | -23.8% | $909.50 | -1.7 | Thu 8:15 AM | too few trades (38/200) |
| momentum_15m_0.10pct | 76 | 44.7 | 52.2 | $-121.14 | -15.9% | $878.86 | -1.4 | Wed 11:45 AM | too few trades (76/200) |
| momentum_60m_0.30pct | 53 | 37.7 | 53.8 | $-176.67 | -33.3% | $823.33 | -2.7 | Wed 8:30 PM | too few trades (53/200) |
| always_up | 124 | 38.7 | 47.9 | $-283.31 | -22.8% | $716.69 | -2.5 | Wed 3:45 AM | too few trades (124/200) |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 175 | 47.4 | 49.0 | $-70.44 |
| ETH | 189 | 43.4 | 47.5 | $-228.58 |
| SOL | 225 | 48.9 | 47.9 | $-52.23 |
| XRP | 224 | 49.6 | 47.8 | $-163.92 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
