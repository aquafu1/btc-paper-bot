# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 10, 10:32 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 30 windows, 726 settled trades, 53 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 46 | 65.2 | 48.9 | $+151.65 | +33.0% | $1151.65 | +2.1 | Wed 9:45 PM | too few trades (46/200) |
| reversal_15m_0.10pct | 69 | 53.6 | 49.1 | $+65.66 | +9.5% | $1065.66 | +0.7 | Wed 11:45 AM | too few trades (69/200) |
| coinflip | 112 | 55.4 | 51.9 | $+40.73 | +3.6% | $1040.73 | +0.4 | Wed 3:45 AM | too few trades (112/200) |
| momentum_5m_0.00pct | 112 | 55.4 | 51.9 | $+37.26 | +3.3% | $1037.26 | +0.4 | Wed 3:45 AM | too few trades (112/200) |
| value_ev10 | 47 | 44.7 | 39.4 | $+26.62 | +5.7% | $1026.62 | +0.3 | Wed 9:15 PM | too few trades (47/200) |
| value_ev5 | 58 | 41.4 | 40.2 | $-18.24 | -3.1% | $981.76 | -0.2 | Wed 3:30 PM | too few trades (58/200) |
| value_ev20 | 22 | 31.8 | 35.8 | $-36.58 | -16.6% | $963.42 | -0.6 | Fri 7:00 AM | too few trades (22/200) |
| momentum_15m_0.10pct | 69 | 46.4 | 52.1 | $-77.12 | -11.2% | $922.88 | -0.9 | Wed 11:45 AM | too few trades (69/200) |
| trend_filter | 33 | 39.4 | 53.9 | $-96.78 | -29.3% | $903.22 | -1.8 | Thu 9:45 AM | too few trades (33/200) |
| momentum_60m_0.30pct | 46 | 34.8 | 53.1 | $-162.95 | -35.4% | $837.05 | -2.6 | Wed 9:45 PM | too few trades (46/200) |
| always_up | 112 | 38.4 | 49.1 | $-273.69 | -24.4% | $726.31 | -2.6 | Wed 3:45 AM | too few trades (112/200) |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 162 | 48.8 | 49.5 | $-13.45 |
| ETH | 169 | 43.2 | 47.9 | $-245.96 |
| SOL | 197 | 49.2 | 48.1 | $+18.60 |
| XRP | 198 | 49.5 | 48.4 | $-102.63 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
