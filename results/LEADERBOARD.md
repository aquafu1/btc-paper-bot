# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 17, 1:05 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 644 windows, 17812 settled trades, 36 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 334 | 34.1 | 35.3 | $-256.80 | -7.7% | $743.20 | -1.1 | done | can't tell from luck |
| momentum_60m_0.30pct | 1503 | 50.8 | 49.6 | $-273.57 | -1.8% | $726.43 | -0.7 | done | can't tell from luck |
| trend_filter | 1029 | 50.2 | 50.8 | $-558.76 | -5.4% | $441.24 | -1.8 | done | can't tell from luck |
| value_ev10 | 822 | 38.3 | 39.5 | $-584.07 | -7.1% | $415.93 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 1834 | 51.4 | 51.0 | $-613.70 | -3.3% | $386.30 | -1.5 | done | can't tell from luck |
| value_ev5 | 1243 | 40.8 | 41.4 | $-679.18 | -5.5% | $320.82 | -1.6 | done | can't tell from luck |
| coinflip | 2570 | 50.2 | 50.5 | $-1168.89 | -4.5% | $-168.89 | -2.3 | done | losing for real |
| momentum_15m_0.10pct | 1834 | 48.6 | 50.0 | $-1220.30 | -6.7% | $-220.30 | -2.9 | done | losing for real |
| reversal_60m_0.30pct | 1503 | 49.2 | 51.4 | $-1319.95 | -8.8% | $-319.95 | -3.5 | done | losing for real |
| momentum_5m_0.00pct | 2570 | 50.6 | 51.7 | $-1428.47 | -5.6% | $-428.47 | -2.9 | done | losing for real |
| always_up | 2570 | 47.2 | 49.7 | $-2285.31 | -8.9% | $-1285.31 | -4.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4047 | 48.3 | 49.3 | $-2430.10 |
| ETH | 4456 | 48.2 | 48.7 | $-2702.26 |
| SOL | 4624 | 48.0 | 48.8 | $-2940.87 |
| XRP | 4685 | 48.5 | 48.5 | $-2315.75 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
