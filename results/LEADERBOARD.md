# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 11, 5:30 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 58 windows, 1467 settled trades, 46 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 105 | 61.0 | 52.1 | $+153.92 | +14.7% | $1153.92 | +1.5 | Wed 6:00 PM | too few trades (105/200) |
| reversal_15m_0.10pct | 138 | 57.2 | 51.7 | $+116.69 | +8.5% | $1116.69 | +1.0 | Wed 11:45 AM | too few trades (138/200) |
| value_ev10 | 81 | 44.4 | 38.7 | $+61.79 | +7.6% | $1061.79 | +0.6 | Thu 2:00 AM | too few trades (81/200) |
| momentum_5m_0.00pct | 224 | 53.6 | 50.7 | $+50.60 | +2.3% | $1050.60 | +0.3 | done | can't tell from luck |
| value_ev20 | 38 | 36.8 | 35.4 | $-3.85 | -1.0% | $996.15 | -0.0 | Fri 5:00 PM | too few trades (38/200) |
| value_ev5 | 111 | 41.4 | 40.3 | $-20.40 | -1.8% | $979.60 | -0.2 | Wed 4:30 PM | too few trades (111/200) |
| trend_filter | 79 | 44.3 | 48.8 | $-99.43 | -12.6% | $900.57 | -1.1 | Thu 2:45 AM | too few trades (79/200) |
| coinflip | 224 | 50.0 | 51.6 | $-146.18 | -6.5% | $853.82 | -1.0 | done | can't tell from luck |
| momentum_15m_0.10pct | 138 | 42.8 | 49.5 | $-216.79 | -15.7% | $783.21 | -1.8 | Wed 11:45 AM | too few trades (138/200) |
| momentum_60m_0.30pct | 105 | 39.0 | 48.9 | $-222.91 | -21.2% | $777.10 | -2.1 | Wed 6:00 PM | too few trades (105/200) |
| always_up | 224 | 42.9 | 49.6 | $-379.24 | -16.9% | $620.76 | -2.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 304 | 47.4 | 49.1 | $-48.46 |
| ETH | 350 | 44.6 | 48.0 | $-312.51 |
| SOL | 407 | 48.2 | 47.9 | $-238.45 |
| XRP | 406 | 50.7 | 48.0 | $-106.37 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
