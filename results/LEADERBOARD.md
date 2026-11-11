# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 11, 2:30 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 46 windows, 1138 settled trades, 56 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 76 | 59.2 | 50.7 | $+108.27 | +14.2% | $1108.27 | +1.2 | Wed 8:15 PM | too few trades (76/200) |
| momentum_5m_0.00pct | 176 | 55.1 | 51.7 | $+66.27 | +3.8% | $1066.27 | +0.5 | Wed 3:45 AM | too few trades (176/200) |
| value_ev10 | 67 | 44.8 | 39.3 | $+46.12 | +6.9% | $1046.12 | +0.5 | Thu 12:15 AM | too few trades (67/200) |
| reversal_15m_0.10pct | 109 | 51.4 | 50.8 | $-2.52 | -0.2% | $997.48 | -0.0 | Wed 11:30 AM | too few trades (109/200) |
| value_ev20 | 28 | 35.7 | 35.9 | $-14.27 | -5.1% | $985.73 | -0.2 | Fri 10:00 PM | too few trades (28/200) |
| value_ev5 | 87 | 41.4 | 40.4 | $-22.15 | -2.5% | $977.85 | -0.2 | Wed 4:45 PM | too few trades (87/200) |
| momentum_15m_0.10pct | 109 | 48.6 | 50.5 | $-44.05 | -4.0% | $955.95 | -0.4 | Wed 11:30 AM | too few trades (109/200) |
| trend_filter | 58 | 46.6 | 50.9 | $-61.85 | -10.7% | $938.15 | -0.8 | Thu 5:15 AM | too few trades (58/200) |
| coinflip | 176 | 50.6 | 51.3 | $-88.73 | -5.0% | $911.27 | -0.7 | Wed 3:45 AM | too few trades (176/200) |
| momentum_60m_0.30pct | 76 | 40.8 | 50.6 | $-152.94 | -20.1% | $847.06 | -1.8 | Wed 8:15 PM | too few trades (76/200) |
| always_up | 176 | 40.9 | 49.4 | $-363.42 | -20.6% | $636.58 | -2.8 | Wed 3:45 AM | too few trades (176/200) |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 233 | 46.8 | 49.3 | $-113.57 |
| ETH | 273 | 44.0 | 47.9 | $-299.04 |
| SOL | 316 | 48.7 | 48.4 | $-98.96 |
| XRP | 316 | 51.6 | 48.4 | $-17.69 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
