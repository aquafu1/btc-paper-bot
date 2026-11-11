# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 11, 7:05 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 64 windows, 1590 settled trades, 38 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 114 | 60.5 | 52.1 | $+159.73 | +14.0% | $1159.73 | +1.5 | Wed 6:30 PM | too few trades (114/200) |
| reversal_15m_0.10pct | 146 | 56.2 | 51.9 | $+90.86 | +6.2% | $1090.86 | +0.8 | Wed 12:30 PM | too few trades (146/200) |
| momentum_5m_0.00pct | 248 | 54.0 | 50.9 | $+71.38 | +2.9% | $1071.38 | +0.5 | done | can't tell from luck |
| value_ev10 | 84 | 42.9 | 38.9 | $+31.79 | +3.8% | $1031.79 | +0.3 | Thu 4:15 AM | too few trades (84/200) |
| value_ev20 | 38 | 36.8 | 35.4 | $-3.85 | -1.0% | $996.15 | -0.0 | Sat 1:00 AM | too few trades (38/200) |
| value_ev5 | 117 | 40.2 | 40.6 | $-62.45 | -5.3% | $937.55 | -0.5 | Wed 5:45 PM | too few trades (117/200) |
| coinflip | 248 | 51.2 | 51.7 | $-106.78 | -4.3% | $893.22 | -0.7 | done | can't tell from luck |
| trend_filter | 87 | 43.7 | 49.1 | $-122.25 | -14.1% | $877.75 | -1.3 | Thu 3:00 AM | too few trades (87/200) |
| momentum_15m_0.10pct | 146 | 43.8 | 49.4 | $-193.92 | -13.3% | $806.08 | -1.6 | Wed 12:30 PM | too few trades (146/200) |
| momentum_60m_0.30pct | 114 | 39.5 | 49.2 | $-238.44 | -20.9% | $761.56 | -2.2 | Wed 6:30 PM | too few trades (114/200) |
| always_up | 248 | 42.7 | 50.0 | $-440.60 | -17.8% | $559.40 | -2.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 327 | 47.1 | 49.4 | $-101.18 |
| ETH | 383 | 44.9 | 48.3 | $-330.43 |
| SOL | 432 | 48.6 | 48.1 | $-227.99 |
| XRP | 448 | 50.4 | 48.3 | $-154.94 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
