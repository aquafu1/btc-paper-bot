# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 10, 6:02 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 12 windows, 269 settled trades, 59 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| coinflip | 40 | 57.5 | 52.3 | $+16.86 | +4.2% | $1016.86 | +0.3 | Wed 3:45 AM | too few trades (40/200) |
| reversal_60m_0.30pct | 20 | 50.0 | 47.9 | $-2.85 | -1.4% | $997.15 | -0.1 | Wed 4:15 PM | too few trades (20/200) |
| reversal_15m_0.10pct | 22 | 50.0 | 48.7 | $-6.11 | -2.8% | $993.89 | -0.1 | Wed 2:00 PM | too few trades (22/200) |
| value_ev10 | 17 | 41.2 | 39.3 | $-6.93 | -4.1% | $993.07 | -0.1 | Wed 8:45 PM | too few trades (17/200) |
| momentum_15m_0.10pct | 22 | 50.0 | 52.7 | $-17.68 | -8.0% | $982.32 | -0.4 | Wed 2:00 PM | too few trades (22/200) |
| momentum_60m_0.30pct | 20 | 50.0 | 54.1 | $-23.54 | -11.8% | $976.46 | -0.6 | Wed 4:15 PM | too few trades (20/200) |
| value_ev20 | 8 | 25.0 | 36.1 | $-28.69 | -35.9% | $971.31 | -0.9 | Fri 5:45 AM | too few trades (8/200) |
| momentum_5m_0.00pct | 40 | 52.5 | 54.3 | $-35.17 | -8.8% | $964.83 | -0.6 | Wed 3:45 AM | too few trades (40/200) |
| trend_filter | 17 | 47.1 | 58.6 | $-37.22 | -21.9% | $962.78 | -1.0 | Wed 8:45 PM | too few trades (17/200) |
| value_ev5 | 23 | 30.4 | 40.5 | $-66.93 | -29.1% | $933.07 | -1.3 | Wed 1:00 PM | too few trades (23/200) |
| always_up | 40 | 45.0 | 52.0 | $-77.83 | -19.5% | $922.17 | -1.3 | Wed 3:45 AM | too few trades (40/200) |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 55 | 49.1 | 50.4 | $-9.60 |
| ETH | 63 | 42.9 | 49.7 | $-120.74 |
| SOL | 74 | 47.3 | 49.2 | $-111.88 |
| XRP | 77 | 50.6 | 48.8 | $-43.88 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
