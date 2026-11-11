# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 10, 10:47 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 31 windows, 758 settled trades, 55 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 48 | 62.5 | 47.3 | $+131.65 | +27.4% | $1131.65 | +1.8 | Wed 9:30 PM | too few trades (48/200) |
| reversal_15m_0.10pct | 71 | 52.1 | 48.0 | $+45.66 | +6.4% | $1045.66 | +0.5 | Wed 11:45 AM | too few trades (71/200) |
| momentum_5m_0.00pct | 116 | 56.0 | 52.5 | $+37.23 | +3.2% | $1037.23 | +0.4 | Wed 3:45 AM | too few trades (116/200) |
| value_ev10 | 51 | 43.1 | 38.5 | $+16.35 | +3.2% | $1016.35 | +0.2 | Wed 7:45 PM | too few trades (51/200) |
| coinflip | 116 | 54.3 | 51.7 | $+12.92 | +1.1% | $1012.92 | +0.1 | Wed 3:45 AM | too few trades (116/200) |
| value_ev20 | 24 | 33.3 | 35.7 | $-26.85 | -11.2% | $973.15 | -0.4 | Fri 3:45 AM | too few trades (24/200) |
| value_ev5 | 62 | 40.3 | 39.4 | $-28.51 | -4.6% | $971.49 | -0.3 | Wed 2:45 PM | too few trades (62/200) |
| momentum_15m_0.10pct | 71 | 47.9 | 52.6 | $-71.14 | -10.0% | $928.86 | -0.9 | Wed 11:45 AM | too few trades (71/200) |
| trend_filter | 35 | 42.9 | 54.8 | $-90.80 | -25.9% | $909.20 | -1.7 | Thu 8:45 AM | too few trades (35/200) |
| momentum_60m_0.30pct | 48 | 37.5 | 53.7 | $-156.97 | -32.7% | $843.03 | -2.5 | Wed 9:30 PM | too few trades (48/200) |
| always_up | 116 | 37.9 | 48.1 | $-283.97 | -24.5% | $716.03 | -2.6 | Wed 3:45 AM | too few trades (116/200) |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 167 | 47.9 | 48.9 | $-49.47 |
| ETH | 175 | 44.0 | 47.6 | $-187.06 |
| SOL | 208 | 48.6 | 47.7 | $-36.20 |
| XRP | 208 | 49.5 | 47.6 | $-141.72 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
