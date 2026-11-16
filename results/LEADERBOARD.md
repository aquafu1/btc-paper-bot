# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 16, 2:15 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 505 windows, 13914 settled trades, 54 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 261 | 34.9 | 35.5 | $-148.91 | -5.7% | $851.09 | -0.7 | done | can't tell from luck |
| momentum_60m_0.30pct | 1180 | 51.2 | 49.8 | $-171.40 | -1.5% | $828.60 | -0.5 | done | can't tell from luck |
| value_ev10 | 654 | 38.4 | 39.8 | $-450.51 | -6.9% | $549.49 | -1.5 | done | can't tell from luck |
| momentum_15m_0.10pct | 1408 | 49.8 | 49.7 | $-538.33 | -3.8% | $461.67 | -1.4 | done | can't tell from luck |
| trend_filter | 817 | 49.6 | 50.7 | $-538.44 | -6.6% | $461.56 | -1.9 | done | can't tell from luck |
| value_ev5 | 970 | 40.2 | 41.6 | $-653.88 | -6.7% | $346.12 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 1408 | 50.2 | 51.5 | $-948.65 | -6.7% | $51.35 | -2.6 | done | losing for real |
| coinflip | 2012 | 50.0 | 50.7 | $-1059.46 | -5.3% | $-59.46 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 1180 | 48.8 | 51.4 | $-1097.52 | -9.3% | $-97.52 | -3.3 | done | losing for real |
| momentum_5m_0.00pct | 2012 | 49.5 | 51.5 | $-1536.95 | -7.6% | $-536.95 | -3.5 | done | losing for real |
| always_up | 2012 | 46.5 | 50.2 | $-2284.92 | -11.4% | $-1284.92 | -5.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3142 | 47.4 | 49.2 | $-2459.22 |
| ETH | 3478 | 48.0 | 48.7 | $-2218.29 |
| SOL | 3630 | 47.7 | 49.0 | $-2697.56 |
| XRP | 3664 | 48.3 | 48.8 | $-2053.89 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
