# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 19, 9:50 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 823 windows, 22614 settled trades, 45 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 419 | 33.4 | 34.9 | $-360.80 | -8.6% | $639.20 | -1.3 | done | can't tell from luck |
| value_ev10 | 1036 | 37.5 | 39.2 | $-786.63 | -7.6% | $213.37 | -2.0 | done | can't tell from luck |
| momentum_60m_0.30pct | 1893 | 50.0 | 49.7 | $-791.94 | -4.2% | $208.06 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 2306 | 50.9 | 50.6 | $-867.39 | -3.8% | $132.61 | -1.8 | done | can't tell from luck |
| trend_filter | 1332 | 49.9 | 50.9 | $-903.31 | -6.8% | $96.69 | -2.5 | done | losing for real |
| value_ev5 | 1568 | 39.8 | 41.1 | $-1050.83 | -6.7% | $-50.83 | -2.3 | done | losing for real |
| reversal_60m_0.30pct | 1893 | 50.0 | 51.1 | $-1352.43 | -7.1% | $-352.43 | -3.2 | done | losing for real |
| momentum_15m_0.10pct | 2306 | 49.1 | 50.3 | $-1400.23 | -6.1% | $-400.23 | -2.9 | done | losing for real |
| momentum_5m_0.00pct | 3287 | 51.3 | 51.7 | $-1494.28 | -4.5% | $-494.28 | -2.7 | done | losing for real |
| coinflip | 3287 | 50.1 | 50.3 | $-1509.98 | -4.6% | $-509.98 | -2.7 | done | losing for real |
| always_up | 3287 | 47.4 | 49.6 | $-2915.88 | -8.9% | $-1915.88 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5135 | 48.1 | 49.1 | $-3176.71 |
| ETH | 5630 | 48.0 | 48.5 | $-3797.49 |
| SOL | 5901 | 48.2 | 48.6 | $-3340.98 |
| XRP | 5948 | 48.5 | 48.5 | $-3118.52 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
