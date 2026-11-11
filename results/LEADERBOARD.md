# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 10, 6:17 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 13 windows, 301 settled trades, 49 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| coinflip | 44 | 61.4 | 52.6 | $+47.94 | +10.9% | $1047.94 | +0.8 | Wed 3:45 AM | too few trades (44/200) |
| reversal_60m_0.30pct | 21 | 52.4 | 48.1 | $+6.09 | +2.9% | $1006.09 | +0.1 | Wed 5:30 PM | too few trades (21/200) |
| reversal_15m_0.10pct | 26 | 53.8 | 50.8 | $-0.47 | -0.2% | $999.53 | -0.0 | Wed 12:30 PM | too few trades (26/200) |
| value_ev10 | 20 | 40.0 | 38.4 | $-17.99 | -9.0% | $982.01 | -0.3 | Wed 6:45 PM | too few trades (20/200) |
| momentum_15m_0.10pct | 26 | 46.2 | 48.9 | $-32.24 | -12.4% | $967.76 | -0.6 | Wed 12:30 PM | too few trades (26/200) |
| momentum_60m_0.30pct | 21 | 47.6 | 54.0 | $-33.54 | -16.0% | $966.46 | -0.8 | Wed 5:30 PM | too few trades (21/200) |
| value_ev20 | 10 | 20.0 | 34.4 | $-48.69 | -48.7% | $951.31 | -1.4 | Thu 10:15 PM | too few trades (10/200) |
| momentum_5m_0.00pct | 44 | 50.0 | 51.8 | $-49.72 | -11.3% | $950.28 | -0.8 | Wed 3:45 AM | too few trades (44/200) |
| trend_filter | 19 | 42.1 | 55.2 | $-57.22 | -30.1% | $942.78 | -1.5 | Wed 8:15 PM | too few trades (19/200) |
| value_ev5 | 26 | 30.8 | 39.6 | $-77.99 | -30.0% | $922.01 | -1.4 | Wed 12:30 PM | too few trades (26/200) |
| always_up | 44 | 43.2 | 49.8 | $-92.38 | -21.0% | $907.62 | -1.5 | Wed 3:45 AM | too few trades (44/200) |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 63 | 46.0 | 47.7 | $-62.72 |
| ETH | 72 | 40.3 | 46.7 | $-184.20 |
| SOL | 84 | 47.6 | 49.6 | $-117.20 |
| XRP | 82 | 52.4 | 48.4 | $+7.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
