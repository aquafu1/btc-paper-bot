# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 11, 1:00 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 40 windows, 965 settled trades, 65 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 61 | 63.9 | 48.6 | $+159.14 | +26.1% | $1159.14 | +2.0 | Wed 10:30 PM | too few trades (61/200) |
| momentum_5m_0.00pct | 152 | 57.2 | 52.4 | $+85.23 | +5.6% | $1085.23 | +0.7 | Wed 3:45 AM | too few trades (152/200) |
| coinflip | 152 | 53.3 | 51.5 | $-13.99 | -0.9% | $986.01 | -0.1 | Wed 3:45 AM | too few trades (152/200) |
| momentum_15m_0.10pct | 92 | 51.1 | 51.8 | $-21.52 | -2.3% | $978.48 | -0.2 | Wed 12:00 PM | too few trades (92/200) |
| value_ev10 | 57 | 40.4 | 38.7 | $-21.81 | -3.8% | $978.19 | -0.2 | Thu 12:45 AM | too few trades (57/200) |
| reversal_15m_0.10pct | 92 | 48.9 | 49.5 | $-23.00 | -2.5% | $977.00 | -0.2 | Wed 12:00 PM | too few trades (92/200) |
| value_ev20 | 26 | 30.8 | 35.7 | $-46.85 | -18.0% | $953.15 | -0.7 | Fri 4:30 PM | too few trades (26/200) |
| value_ev5 | 75 | 38.7 | 40.0 | $-70.08 | -9.3% | $929.92 | -0.7 | Wed 4:45 PM | too few trades (75/200) |
| trend_filter | 45 | 44.4 | 54.0 | $-101.16 | -22.5% | $898.84 | -1.7 | Thu 9:30 AM | too few trades (45/200) |
| momentum_60m_0.30pct | 61 | 36.1 | 52.8 | $-214.63 | -35.2% | $785.37 | -3.1 | Wed 10:30 PM | too few trades (61/200) |
| always_up | 152 | 40.8 | 48.8 | $-311.08 | -20.5% | $688.92 | -2.5 | Wed 3:45 AM | too few trades (152/200) |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 199 | 46.7 | 49.2 | $-121.02 |
| ETH | 228 | 44.7 | 47.8 | $-229.04 |
| SOL | 269 | 49.4 | 48.4 | $-64.28 |
| XRP | 269 | 50.2 | 48.4 | $-165.43 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
