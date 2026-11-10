# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 10, 5:17 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 9 windows, 184 settled trades, 58 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| coinflip | 28 | 60.7 | 51.7 | $+40.79 | +14.6% | $1040.79 | +0.8 | Wed 3:45 AM | too few trades (28/200) |
| value_ev10 | 11 | 54.5 | 39.5 | $+30.74 | +27.9% | $1030.74 | +0.7 | Wed 11:15 PM | too few trades (11/200) |
| value_ev20 | 4 | 50.0 | 35.1 | $+11.31 | +28.3% | $1011.31 | +0.4 | Sat 6:45 AM | too few trades (4/200) |
| momentum_60m_0.30pct | 12 | 58.3 | 55.0 | $+6.67 | +5.6% | $1006.67 | +0.2 | Wed 8:30 PM | too few trades (12/200) |
| reversal_15m_0.10pct | 17 | 52.9 | 51.2 | $+2.41 | +1.4% | $1002.41 | +0.1 | Wed 12:00 PM | too few trades (17/200) |
| value_ev5 | 15 | 40.0 | 41.0 | $-9.26 | -6.2% | $990.74 | -0.2 | Wed 2:45 PM | too few trades (15/200) |
| momentum_5m_0.00pct | 28 | 53.6 | 54.4 | $-10.70 | -3.8% | $989.30 | -0.2 | Wed 3:45 AM | too few trades (28/200) |
| momentum_15m_0.10pct | 17 | 47.1 | 50.4 | $-12.19 | -7.2% | $987.81 | -0.3 | Wed 12:00 PM | too few trades (17/200) |
| reversal_60m_0.30pct | 12 | 41.7 | 47.9 | $-17.85 | -14.9% | $982.15 | -0.5 | Wed 8:30 PM | too few trades (12/200) |
| trend_filter | 12 | 41.7 | 56.9 | $-33.95 | -28.3% | $966.05 | -1.1 | Wed 8:30 PM | too few trades (12/200) |
| always_up | 28 | 35.7 | 52.4 | $-98.78 | -35.3% | $901.22 | -2.1 | Wed 3:45 AM | too few trades (28/200) |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 41 | 51.2 | 49.9 | $+28.35 |
| ETH | 45 | 40.0 | 49.5 | $-113.81 |
| SOL | 48 | 47.9 | 49.7 | $-46.44 |
| XRP | 50 | 56.0 | 49.9 | $+41.10 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
