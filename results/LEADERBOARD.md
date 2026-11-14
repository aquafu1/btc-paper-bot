# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 13, 8:05 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 288 windows, 7620 settled trades, 51 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 750 | 54.3 | 51.8 | $+25.70 | +0.3% | $1025.70 | +0.1 | done | can't tell from luck |
| value_ev20 | 142 | 35.9 | 36.4 | $-101.22 | -7.1% | $898.78 | -0.7 | Sun 3:30 AM | too few trades (142/200) |
| reversal_60m_0.30pct | 612 | 52.5 | 51.8 | $-190.58 | -3.1% | $809.42 | -0.8 | done | can't tell from luck |
| value_ev10 | 369 | 38.5 | 40.5 | $-336.90 | -9.1% | $663.10 | -1.5 | done | can't tell from luck |
| trend_filter | 406 | 46.6 | 50.4 | $-496.66 | -12.2% | $503.34 | -2.5 | done | losing for real |
| value_ev5 | 544 | 40.1 | 42.2 | $-505.43 | -9.3% | $494.57 | -1.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 612 | 47.5 | 49.8 | $-577.45 | -9.4% | $422.55 | -2.4 | done | losing for real |
| coinflip | 1145 | 50.1 | 50.9 | $-658.14 | -5.7% | $341.86 | -2.0 | done | can't tell from luck |
| momentum_5m_0.00pct | 1145 | 49.4 | 51.5 | $-921.97 | -8.1% | $78.03 | -2.8 | done | losing for real |
| momentum_15m_0.10pct | 750 | 45.7 | 49.9 | $-936.62 | -12.5% | $63.38 | -3.5 | done | losing for real |
| always_up | 1145 | 47.7 | 50.2 | $-1056.10 | -9.2% | $-56.10 | -3.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1701 | 46.9 | 49.4 | $-1526.83 |
| ETH | 1901 | 47.3 | 48.8 | $-1661.08 |
| SOL | 1979 | 48.3 | 49.3 | $-1543.32 |
| XRP | 2039 | 48.8 | 49.1 | $-1024.14 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
