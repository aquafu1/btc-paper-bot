# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 15, 2:35 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 458 windows, 12574 settled trades, 63 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 231 | 34.2 | 35.9 | $-192.39 | -8.3% | $807.61 | -1.0 | done | can't tell from luck |
| momentum_60m_0.30pct | 1071 | 51.1 | 49.9 | $-233.64 | -2.2% | $766.36 | -0.7 | done | can't tell from luck |
| trend_filter | 729 | 50.1 | 50.7 | $-385.98 | -5.3% | $614.02 | -1.5 | done | can't tell from luck |
| value_ev10 | 590 | 38.6 | 40.1 | $-417.06 | -7.1% | $582.94 | -1.4 | done | can't tell from luck |
| momentum_15m_0.10pct | 1268 | 49.9 | 50.0 | $-485.49 | -3.8% | $514.51 | -1.4 | done | can't tell from luck |
| value_ev5 | 874 | 40.7 | 41.8 | $-551.74 | -6.3% | $448.26 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 1268 | 50.1 | 51.6 | $-924.61 | -7.3% | $75.39 | -2.7 | done | losing for real |
| coinflip | 1824 | 49.9 | 50.8 | $-1033.66 | -5.7% | $-33.66 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 1071 | 48.9 | 51.8 | $-1059.49 | -9.9% | $-59.49 | -3.4 | done | losing for real |
| momentum_5m_0.00pct | 1824 | 49.7 | 51.5 | $-1317.17 | -7.2% | $-317.17 | -3.2 | done | losing for real |
| always_up | 1824 | 46.1 | 50.5 | $-2314.70 | -12.7% | $-1314.70 | -5.6 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2842 | 47.4 | 49.3 | $-2375.24 |
| ETH | 3156 | 48.0 | 48.8 | $-2083.87 |
| SOL | 3274 | 47.7 | 49.3 | $-2553.80 |
| XRP | 3302 | 48.5 | 49.2 | $-1903.03 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
