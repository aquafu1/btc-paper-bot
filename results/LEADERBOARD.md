# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 13, 5:05 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 228 windows, 5973 settled trades, 53 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 591 | 56.2 | 52.6 | $+199.71 | +3.4% | $1199.71 | +0.9 | done | can't tell from luck |
| reversal_60m_0.30pct | 466 | 54.3 | 52.3 | $+7.26 | +0.2% | $1007.26 | +0.0 | done | can't tell from luck |
| value_ev20 | 112 | 33.9 | 36.6 | $-124.82 | -11.1% | $875.18 | -0.9 | Sun 5:15 AM | too few trades (112/200) |
| value_ev10 | 295 | 37.6 | 40.7 | $-330.78 | -11.2% | $669.22 | -1.6 | done | can't tell from luck |
| trend_filter | 311 | 45.0 | 50.2 | $-438.71 | -14.1% | $561.29 | -2.5 | done | losing for real |
| value_ev5 | 429 | 39.4 | 42.5 | $-468.82 | -10.9% | $531.18 | -2.0 | done | can't tell from luck |
| momentum_60m_0.30pct | 466 | 45.7 | 49.8 | $-568.08 | -12.2% | $431.92 | -2.7 | done | losing for real |
| momentum_5m_0.00pct | 904 | 50.2 | 51.5 | $-576.39 | -6.4% | $423.61 | -2.0 | done | can't tell from luck |
| coinflip | 904 | 49.7 | 51.0 | $-593.92 | -6.6% | $406.08 | -2.0 | done | losing for real |
| momentum_15m_0.10pct | 591 | 43.8 | 49.6 | $-897.00 | -15.2% | $103.00 | -3.7 | done | losing for real |
| always_up | 904 | 47.2 | 50.3 | $-926.64 | -10.3% | $73.36 | -3.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1341 | 46.5 | 49.7 | $-1325.44 |
| ETH | 1488 | 46.7 | 49.0 | $-1451.81 |
| SOL | 1544 | 47.9 | 49.3 | $-1271.09 |
| XRP | 1600 | 49.1 | 49.1 | $-669.85 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
