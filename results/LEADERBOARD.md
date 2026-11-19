# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 19, 9:00 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 820 windows, 22497 settled trades, 57 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 416 | 33.7 | 35.0 | $-330.80 | -8.0% | $669.20 | -1.2 | done | can't tell from luck |
| value_ev10 | 1029 | 37.8 | 39.2 | $-716.63 | -7.0% | $283.37 | -1.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 1882 | 50.0 | 49.6 | $-764.97 | -4.1% | $235.03 | -1.8 | done | can't tell from luck |
| trend_filter | 1321 | 50.0 | 50.8 | $-862.36 | -6.5% | $137.64 | -2.4 | done | losing for real |
| reversal_15m_0.10pct | 2298 | 50.8 | 50.6 | $-871.34 | -3.8% | $128.66 | -1.8 | done | can't tell from luck |
| value_ev5 | 1555 | 40.1 | 41.1 | $-940.81 | -6.1% | $59.19 | -2.0 | done | losing for real |
| reversal_60m_0.30pct | 1882 | 50.0 | 51.2 | $-1328.82 | -7.1% | $-328.82 | -3.1 | done | losing for real |
| momentum_15m_0.10pct | 2298 | 49.2 | 50.2 | $-1362.67 | -5.9% | $-362.67 | -2.9 | done | losing for real |
| momentum_5m_0.00pct | 3272 | 51.3 | 51.6 | $-1461.49 | -4.5% | $-461.49 | -2.6 | done | losing for real |
| coinflip | 3272 | 50.1 | 50.3 | $-1479.76 | -4.5% | $-479.76 | -2.6 | done | losing for real |
| always_up | 3272 | 47.5 | 49.6 | $-2831.91 | -8.7% | $-1831.91 | -5.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5103 | 48.2 | 49.1 | $-3078.23 |
| ETH | 5600 | 48.1 | 48.5 | $-3686.18 |
| SOL | 5868 | 48.3 | 48.6 | $-3173.20 |
| XRP | 5926 | 48.5 | 48.5 | $-3013.96 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
