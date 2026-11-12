# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 12, 3:20 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 183 windows, 4674 settled trades, 35 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 344 | 59.9 | 53.0 | $+342.93 | +10.0% | $1342.93 | +2.0 | done | can't tell from luck |
| reversal_15m_0.10pct | 453 | 57.8 | 52.4 | $+333.98 | +7.4% | $1333.98 | +1.7 | done | can't tell from luck |
| value_ev20 | 88 | 34.1 | 36.7 | $-128.58 | -14.6% | $871.42 | -1.1 | Sun 4:30 AM | too few trades (88/200) |
| momentum_5m_0.00pct | 725 | 51.3 | 51.3 | $-284.81 | -3.9% | $715.19 | -1.1 | done | can't tell from luck |
| value_ev10 | 236 | 37.3 | 40.6 | $-313.12 | -13.3% | $686.88 | -1.8 | done | can't tell from luck |
| coinflip | 725 | 50.3 | 50.9 | $-389.49 | -5.4% | $610.51 | -1.5 | done | can't tell from luck |
| value_ev5 | 347 | 38.9 | 42.4 | $-438.61 | -12.6% | $561.39 | -2.1 | done | losing for real |
| trend_filter | 234 | 41.0 | 49.4 | $-458.40 | -19.6% | $541.60 | -3.0 | done | losing for real |
| momentum_60m_0.30pct | 344 | 40.1 | 49.0 | $-740.36 | -21.5% | $259.64 | -4.0 | done | losing for real |
| momentum_15m_0.10pct | 453 | 42.2 | 49.7 | $-823.94 | -18.2% | $176.06 | -3.9 | done | losing for real |
| always_up | 725 | 46.2 | 50.0 | $-871.36 | -12.0% | $128.64 | -3.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1025 | 45.8 | 49.4 | $-1055.97 |
| ETH | 1164 | 46.0 | 48.8 | $-1278.70 |
| SOL | 1210 | 47.6 | 49.0 | $-1056.56 |
| XRP | 1275 | 50.0 | 49.1 | $-380.54 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
