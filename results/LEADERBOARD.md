# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 19, 1:35 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 790 windows, 21782 settled trades, 34 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 404 | 32.9 | 34.9 | $-391.45 | -9.7% | $608.55 | -1.5 | done | can't tell from luck |
| momentum_60m_0.30pct | 1847 | 50.1 | 49.6 | $-700.47 | -3.8% | $299.53 | -1.6 | done | can't tell from luck |
| trend_filter | 1283 | 50.4 | 50.8 | $-732.70 | -5.7% | $267.30 | -2.1 | done | losing for real |
| value_ev10 | 991 | 37.4 | 39.1 | $-774.94 | -7.8% | $225.06 | -2.0 | done | losing for real |
| reversal_15m_0.10pct | 2225 | 50.9 | 50.6 | $-811.07 | -3.6% | $188.93 | -1.7 | done | can't tell from luck |
| value_ev5 | 1498 | 39.8 | 41.1 | $-1003.27 | -6.7% | $-3.27 | -2.2 | done | losing for real |
| reversal_60m_0.30pct | 1847 | 49.9 | 51.2 | $-1341.44 | -7.3% | $-341.44 | -3.2 | done | losing for real |
| coinflip | 3154 | 50.3 | 50.3 | $-1353.94 | -4.3% | $-353.94 | -2.4 | done | losing for real |
| momentum_15m_0.10pct | 2225 | 49.1 | 50.3 | $-1380.18 | -6.2% | $-380.18 | -2.9 | done | losing for real |
| momentum_5m_0.00pct | 3154 | 51.3 | 51.7 | $-1452.43 | -4.6% | $-452.43 | -2.7 | done | losing for real |
| always_up | 3154 | 47.5 | 49.6 | $-2667.03 | -8.5% | $-1667.03 | -4.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4945 | 48.3 | 49.1 | $-2957.14 |
| ETH | 5428 | 48.1 | 48.5 | $-3527.34 |
| SOL | 5676 | 48.2 | 48.6 | $-3236.88 |
| XRP | 5733 | 48.5 | 48.5 | $-2887.58 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
