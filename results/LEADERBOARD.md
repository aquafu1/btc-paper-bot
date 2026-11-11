# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 11, 3:20 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 49 windows, 1225 settled trades, 75 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 84 | 63.1 | 51.5 | $+159.46 | +19.0% | $1159.46 | +1.8 | Wed 7:15 PM | too few trades (84/200) |
| reversal_15m_0.10pct | 116 | 53.4 | 51.6 | $+14.54 | +1.3% | $1014.54 | +0.1 | Wed 11:45 AM | too few trades (116/200) |
| value_ev10 | 71 | 42.3 | 39.0 | $+6.12 | +0.9% | $1006.12 | +0.1 | Thu 12:30 AM | too few trades (71/200) |
| momentum_5m_0.00pct | 188 | 52.7 | 50.9 | $-12.47 | -0.7% | $987.53 | -0.1 | Wed 3:45 AM | too few trades (188/200) |
| value_ev20 | 31 | 32.3 | 35.6 | $-44.27 | -14.3% | $955.73 | -0.6 | Fri 7:15 PM | too few trades (31/200) |
| momentum_15m_0.10pct | 116 | 46.6 | 49.5 | $-90.10 | -7.8% | $909.90 | -0.8 | Wed 11:45 AM | too few trades (116/200) |
| value_ev5 | 94 | 38.3 | 40.3 | $-92.15 | -9.8% | $907.85 | -0.8 | Wed 4:15 PM | too few trades (94/200) |
| coinflip | 188 | 50.0 | 51.0 | $-120.23 | -6.4% | $879.77 | -0.9 | Wed 3:45 AM | too few trades (188/200) |
| trend_filter | 65 | 41.5 | 49.6 | $-131.85 | -20.3% | $868.15 | -1.6 | Thu 3:30 AM | too few trades (65/200) |
| momentum_60m_0.30pct | 84 | 36.9 | 49.6 | $-232.94 | -27.7% | $767.06 | -2.6 | Wed 7:15 PM | too few trades (84/200) |
| always_up | 188 | 39.9 | 49.4 | $-439.36 | -23.4% | $560.64 | -3.3 | Wed 3:45 AM | too few trades (188/200) |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 249 | 45.4 | 49.1 | $-185.52 |
| ETH | 293 | 43.3 | 47.9 | $-389.66 |
| SOL | 341 | 46.9 | 47.9 | $-258.50 |
| XRP | 342 | 50.0 | 47.9 | $-149.58 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
