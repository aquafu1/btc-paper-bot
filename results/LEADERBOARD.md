# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 10, 5:30 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 10 windows, 217 settled trades, 52 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| coinflip | 32 | 59.4 | 52.1 | $+31.98 | +10.0% | $1031.98 | +0.6 | Wed 3:45 AM | too few trades (32/200) |
| value_ev10 | 14 | 50.0 | 39.5 | $+23.07 | +16.5% | $1023.07 | +0.5 | Wed 8:00 PM | too few trades (14/200) |
| momentum_60m_0.30pct | 15 | 60.0 | 56.7 | $+6.39 | +4.3% | $1006.39 | +0.2 | Wed 6:00 PM | too few trades (15/200) |
| momentum_5m_0.00pct | 32 | 56.2 | 55.4 | $-3.97 | -1.2% | $996.03 | -0.1 | Wed 3:45 AM | too few trades (32/200) |
| momentum_15m_0.10pct | 18 | 50.0 | 51.0 | $-6.65 | -3.7% | $993.35 | -0.2 | Wed 1:30 PM | too few trades (18/200) |
| reversal_15m_0.10pct | 18 | 50.0 | 50.5 | $-7.59 | -4.2% | $992.41 | -0.2 | Wed 1:30 PM | too few trades (18/200) |
| value_ev20 | 6 | 33.3 | 35.7 | $-8.69 | -14.5% | $991.31 | -0.3 | Fri 10:00 AM | too few trades (6/200) |
| reversal_60m_0.30pct | 15 | 40.0 | 45.9 | $-25.52 | -17.0% | $974.48 | -0.6 | Wed 6:00 PM | too few trades (15/200) |
| value_ev5 | 19 | 36.8 | 40.9 | $-26.93 | -14.2% | $973.07 | -0.5 | Wed 12:30 PM | too few trades (19/200) |
| trend_filter | 16 | 50.0 | 58.3 | $-27.22 | -17.0% | $972.78 | -0.8 | Wed 4:15 PM | too few trades (16/200) |
| always_up | 32 | 34.4 | 50.6 | $-116.45 | -36.4% | $883.55 | -2.3 | Wed 3:45 AM | too few trades (32/200) |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 46 | 52.2 | 50.2 | $+29.40 |
| ETH | 53 | 41.5 | 49.8 | $-104.50 |
| SOL | 59 | 45.8 | 49.3 | $-94.29 |
| XRP | 59 | 54.2 | 48.8 | $+7.81 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
