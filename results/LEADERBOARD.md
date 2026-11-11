# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 10, 10:02 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 28 windows, 695 settled trades, 31 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 46 | 65.2 | 48.9 | $+151.65 | +33.0% | $1151.65 | +2.1 | Wed 7:45 PM | too few trades (46/200) |
| reversal_15m_0.10pct | 66 | 56.1 | 49.0 | $+95.66 | +14.5% | $1095.66 | +1.1 | Wed 11:00 AM | too few trades (66/200) |
| coinflip | 104 | 56.7 | 51.8 | $+63.73 | +6.1% | $1063.73 | +0.6 | Wed 3:45 AM | too few trades (104/200) |
| value_ev10 | 47 | 44.7 | 39.4 | $+26.62 | +5.7% | $1026.62 | +0.3 | Wed 7:00 PM | too few trades (47/200) |
| momentum_5m_0.00pct | 104 | 54.8 | 52.0 | $+20.42 | +2.0% | $1020.42 | +0.2 | Wed 3:45 AM | too few trades (104/200) |
| value_ev5 | 58 | 41.4 | 40.2 | $-18.24 | -3.1% | $981.76 | -0.2 | Wed 1:45 PM | too few trades (58/200) |
| value_ev20 | 22 | 31.8 | 35.8 | $-36.58 | -16.6% | $963.42 | -0.6 | Fri 2:30 AM | too few trades (22/200) |
| momentum_15m_0.10pct | 66 | 43.9 | 52.0 | $-102.36 | -15.5% | $897.64 | -1.3 | Wed 11:00 AM | too few trades (66/200) |
| trend_filter | 32 | 37.5 | 53.7 | $-104.09 | -32.5% | $895.91 | -2.0 | Thu 8:00 AM | too few trades (32/200) |
| momentum_60m_0.30pct | 46 | 34.8 | 53.1 | $-162.95 | -35.4% | $837.05 | -2.6 | Wed 7:45 PM | too few trades (46/200) |
| always_up | 104 | 38.5 | 48.8 | $-250.50 | -24.1% | $749.50 | -2.4 | Wed 3:45 AM | too few trades (104/200) |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 156 | 48.7 | 49.3 | $-12.97 |
| ETH | 163 | 42.9 | 47.7 | $-240.48 |
| SOL | 188 | 48.9 | 47.9 | $+15.31 |
| XRP | 188 | 50.0 | 48.1 | $-78.49 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
