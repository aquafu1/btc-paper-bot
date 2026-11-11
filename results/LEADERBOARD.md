# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 11, 2:35 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 46 windows, 1146 settled trades, 48 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 77 | 59.7 | 50.8 | $+114.47 | +14.9% | $1114.47 | +1.3 | Wed 8:30 PM | too few trades (77/200) |
| momentum_5m_0.00pct | 177 | 54.8 | 51.6 | $+56.27 | +3.2% | $1056.27 | +0.4 | Wed 4:00 AM | too few trades (177/200) |
| value_ev10 | 68 | 44.1 | 39.3 | $+36.12 | +5.3% | $1036.12 | +0.4 | Thu 12:30 AM | too few trades (68/200) |
| reversal_15m_0.10pct | 109 | 51.4 | 50.8 | $-2.52 | -0.2% | $997.48 | -0.0 | Wed 12:00 PM | too few trades (109/200) |
| value_ev20 | 28 | 35.7 | 35.9 | $-14.27 | -5.1% | $985.73 | -0.2 | Fri 11:45 PM | too few trades (28/200) |
| value_ev5 | 88 | 40.9 | 40.4 | $-32.15 | -3.7% | $967.85 | -0.3 | Wed 5:00 PM | too few trades (88/200) |
| momentum_15m_0.10pct | 109 | 48.6 | 50.5 | $-44.05 | -4.0% | $955.95 | -0.4 | Wed 12:00 PM | too few trades (109/200) |
| trend_filter | 59 | 45.8 | 50.8 | $-71.85 | -12.2% | $928.15 | -0.9 | Thu 5:30 AM | too few trades (59/200) |
| coinflip | 177 | 50.3 | 51.3 | $-98.73 | -5.6% | $901.27 | -0.8 | Wed 4:00 AM | too few trades (177/200) |
| momentum_60m_0.30pct | 77 | 40.3 | 50.5 | $-162.94 | -21.2% | $837.06 | -1.9 | Wed 8:30 PM | too few trades (77/200) |
| always_up | 177 | 40.7 | 49.4 | $-373.42 | -21.1% | $626.58 | -2.8 | Wed 4:00 AM | too few trades (177/200) |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 241 | 45.6 | 49.1 | $-177.37 |
| ETH | 273 | 44.0 | 47.9 | $-299.04 |
| SOL | 316 | 48.7 | 48.4 | $-98.96 |
| XRP | 316 | 51.6 | 48.4 | $-17.69 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
