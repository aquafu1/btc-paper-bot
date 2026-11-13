# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 12, 9:20 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 197 windows, 5063 settled trades, 75 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 494 | 58.9 | 52.6 | $+422.86 | +8.6% | $1422.86 | +2.0 | done | real edge? (z>=2) |
| reversal_60m_0.30pct | 372 | 59.4 | 53.0 | $+321.99 | +8.7% | $1321.99 | +1.8 | done | can't tell from luck |
| value_ev20 | 96 | 31.2 | 37.1 | $-208.58 | -21.7% | $791.42 | -1.8 | Sun 7:15 AM | too few trades (96/200) |
| momentum_5m_0.00pct | 780 | 51.2 | 51.3 | $-364.60 | -4.7% | $635.40 | -1.4 | done | can't tell from luck |
| value_ev10 | 260 | 35.8 | 41.0 | $-454.03 | -17.5% | $545.97 | -2.5 | done | losing for real |
| coinflip | 780 | 50.1 | 50.9 | $-490.90 | -6.3% | $509.10 | -1.8 | done | can't tell from luck |
| trend_filter | 255 | 41.6 | 49.5 | $-493.59 | -19.4% | $506.41 | -3.1 | done | losing for real |
| value_ev5 | 380 | 38.4 | 42.7 | $-555.55 | -14.6% | $444.45 | -2.6 | done | losing for real |
| momentum_60m_0.30pct | 372 | 40.6 | 49.2 | $-794.69 | -21.4% | $205.31 | -4.2 | done | losing for real |
| always_up | 780 | 46.3 | 50.3 | $-986.42 | -12.6% | $13.58 | -3.7 | done | losing for real |
| momentum_15m_0.10pct | 494 | 41.1 | 49.6 | $-1020.54 | -20.7% | $-20.54 | -4.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1115 | 45.7 | 49.5 | $-1254.01 |
| ETH | 1259 | 46.0 | 48.9 | $-1457.70 |
| SOL | 1312 | 47.7 | 49.1 | $-1169.58 |
| XRP | 1377 | 49.2 | 49.2 | $-742.74 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
