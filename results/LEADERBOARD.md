# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 10, 9:45 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 27 windows, 668 settled trades, 44 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 42 | 61.9 | 48.0 | $+125.57 | +29.9% | $1125.57 | +1.8 | Wed 9:15 PM | too few trades (42/200) |
| reversal_15m_0.10pct | 64 | 57.8 | 49.1 | $+115.66 | +18.1% | $1115.66 | +1.4 | Wed 11:00 AM | too few trades (64/200) |
| coinflip | 100 | 56.0 | 51.7 | $+53.35 | +5.3% | $1053.35 | +0.5 | Wed 3:45 AM | too few trades (100/200) |
| value_ev10 | 46 | 45.7 | 39.4 | $+36.62 | +8.0% | $1036.62 | +0.4 | Wed 6:30 PM | too few trades (46/200) |
| momentum_5m_0.00pct | 100 | 54.0 | 51.9 | $+10.04 | +1.0% | $1010.04 | +0.1 | Wed 3:45 AM | too few trades (100/200) |
| value_ev5 | 57 | 42.1 | 40.2 | $-8.24 | -1.4% | $991.76 | -0.1 | Wed 1:15 PM | too few trades (57/200) |
| value_ev20 | 22 | 31.8 | 35.8 | $-36.58 | -16.6% | $963.42 | -0.6 | Fri 12:15 AM | too few trades (22/200) |
| trend_filter | 31 | 38.7 | 54.2 | $-94.09 | -30.4% | $905.91 | -1.8 | Thu 7:45 AM | too few trades (31/200) |
| momentum_15m_0.10pct | 64 | 42.2 | 51.8 | $-116.01 | -18.1% | $883.99 | -1.4 | Wed 11:00 AM | too few trades (64/200) |
| momentum_60m_0.30pct | 42 | 38.1 | 53.9 | $-122.95 | -29.3% | $877.05 | -2.0 | Wed 9:15 PM | too few trades (42/200) |
| always_up | 100 | 40.0 | 49.0 | $-210.50 | -21.0% | $789.50 | -2.1 | Wed 3:45 AM | too few trades (100/200) |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 151 | 48.3 | 49.2 | $-13.17 |
| ETH | 156 | 42.3 | 47.5 | $-242.27 |
| SOL | 180 | 50.6 | 48.1 | $+79.61 |
| XRP | 181 | 49.7 | 48.0 | $-71.29 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
