# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 12, 12:20 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 171 windows, 4374 settled trades, 56 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 429 | 58.7 | 52.7 | $+379.79 | +8.9% | $1379.79 | +1.9 | done | can't tell from luck |
| reversal_60m_0.30pct | 321 | 60.7 | 53.2 | $+373.96 | +11.6% | $1373.96 | +2.2 | done | real edge? (z>=2) |
| value_ev20 | 80 | 35.0 | 37.1 | $-101.99 | -12.7% | $898.01 | -0.9 | Sun 7:15 AM | too few trades (80/200) |
| momentum_5m_0.00pct | 676 | 51.5 | 51.2 | $-228.50 | -3.4% | $771.50 | -0.9 | done | can't tell from luck |
| value_ev10 | 219 | 37.9 | 40.8 | $-261.47 | -11.9% | $738.53 | -1.5 | done | can't tell from luck |
| value_ev5 | 324 | 39.2 | 42.6 | $-392.86 | -12.1% | $607.14 | -2.0 | done | can't tell from luck |
| coinflip | 676 | 49.7 | 50.9 | $-452.69 | -6.7% | $547.31 | -1.8 | done | can't tell from luck |
| trend_filter | 223 | 40.4 | 49.1 | $-452.69 | -20.3% | $547.31 | -3.0 | done | losing for real |
| momentum_60m_0.30pct | 321 | 39.3 | 48.9 | $-727.33 | -22.7% | $272.67 | -4.1 | done | losing for real |
| always_up | 676 | 46.3 | 50.0 | $-787.58 | -11.7% | $212.42 | -3.1 | done | losing for real |
| momentum_15m_0.10pct | 429 | 41.3 | 49.5 | $-837.00 | -19.5% | $163.00 | -4.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 950 | 45.9 | 49.5 | $-913.71 |
| ETH | 1090 | 45.7 | 48.9 | $-1222.71 |
| SOL | 1148 | 47.9 | 49.0 | $-915.51 |
| XRP | 1186 | 49.8 | 49.1 | $-436.45 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
