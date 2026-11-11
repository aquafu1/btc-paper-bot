# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 11, 12:02 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 36 windows, 880 settled trades, 46 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 56 | 62.5 | 48.0 | $+137.20 | +24.5% | $1137.20 | +1.8 | Wed 9:45 PM | too few trades (56/200) |
| momentum_5m_0.00pct | 136 | 56.6 | 52.4 | $+52.12 | +3.8% | $1052.12 | +0.5 | Wed 3:45 AM | too few trades (136/200) |
| reversal_15m_0.10pct | 82 | 52.4 | 48.9 | $+39.40 | +4.8% | $1039.40 | +0.4 | Wed 12:00 PM | too few trades (82/200) |
| coinflip | 136 | 53.7 | 51.6 | $-10.38 | -0.8% | $989.62 | -0.1 | Wed 3:45 AM | too few trades (136/200) |
| value_ev10 | 57 | 40.4 | 38.7 | $-21.81 | -3.8% | $978.19 | -0.2 | Wed 9:15 PM | too few trades (57/200) |
| value_ev20 | 26 | 30.8 | 35.7 | $-46.85 | -18.0% | $953.15 | -0.7 | Fri 8:45 AM | too few trades (26/200) |
| value_ev5 | 72 | 38.9 | 39.8 | $-63.46 | -8.8% | $936.54 | -0.6 | Wed 3:00 PM | too few trades (72/200) |
| trend_filter | 41 | 46.3 | 54.5 | $-82.18 | -20.0% | $917.82 | -1.4 | Thu 8:45 AM | too few trades (41/200) |
| momentum_15m_0.10pct | 82 | 47.6 | 52.1 | $-83.87 | -10.2% | $916.13 | -0.9 | Wed 12:00 PM | too few trades (82/200) |
| momentum_60m_0.30pct | 56 | 37.5 | 53.2 | $-185.65 | -33.2% | $814.35 | -2.8 | Wed 9:45 PM | too few trades (56/200) |
| always_up | 136 | 42.6 | 48.8 | $-236.37 | -17.4% | $763.63 | -2.0 | Wed 3:45 AM | too few trades (136/200) |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 184 | 47.3 | 49.2 | $-93.18 |
| ETH | 208 | 44.7 | 47.5 | $-213.76 |
| SOL | 245 | 50.2 | 48.2 | $-8.48 |
| XRP | 243 | 49.8 | 48.1 | $-186.45 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
