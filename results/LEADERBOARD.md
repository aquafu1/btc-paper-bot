# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 10, 7:30 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 18 windows, 424 settled trades, 65 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_15m_0.10pct | 32 | 53.1 | 48.4 | $+12.49 | +3.9% | $1012.49 | +0.2 | Wed 4:15 PM | too few trades (32/200) |
| coinflip | 64 | 56.2 | 51.3 | $+7.50 | +1.2% | $1007.50 | +0.1 | Wed 3:45 AM | too few trades (64/200) |
| momentum_60m_0.30pct | 28 | 53.6 | 51.4 | $-0.31 | -0.1% | $999.69 | -0.0 | Wed 8:00 PM | too few trades (28/200) |
| value_ev10 | 32 | 40.6 | 38.5 | $-23.84 | -7.4% | $976.16 | -0.4 | Wed 4:15 PM | too few trades (32/200) |
| momentum_5m_0.00pct | 64 | 53.1 | 51.0 | $-28.18 | -4.4% | $971.82 | -0.4 | Wed 3:45 AM | too few trades (64/200) |
| trend_filter | 23 | 47.8 | 52.3 | $-29.79 | -13.0% | $970.21 | -0.6 | Thu 2:15 AM | too few trades (23/200) |
| reversal_60m_0.30pct | 28 | 46.4 | 50.4 | $-33.67 | -12.0% | $966.33 | -0.6 | Wed 8:00 PM | too few trades (28/200) |
| reversal_15m_0.10pct | 32 | 46.9 | 51.2 | $-45.09 | -14.1% | $954.91 | -0.8 | Wed 4:15 PM | too few trades (32/200) |
| value_ev20 | 17 | 23.5 | 35.1 | $-69.96 | -41.2% | $930.04 | -1.6 | Thu 2:30 PM | too few trades (17/200) |
| value_ev5 | 40 | 35.0 | 39.5 | $-85.34 | -21.3% | $914.66 | -1.2 | Wed 11:15 AM | too few trades (40/200) |
| always_up | 64 | 34.4 | 47.9 | $-234.41 | -36.6% | $765.59 | -3.2 | Wed 3:45 AM | too few trades (64/200) |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 90 | 46.7 | 47.9 | $-61.61 |
| ETH | 98 | 38.8 | 45.8 | $-253.14 |
| SOL | 118 | 49.2 | 48.5 | $-94.19 |
| XRP | 118 | 47.5 | 46.5 | $-121.65 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
