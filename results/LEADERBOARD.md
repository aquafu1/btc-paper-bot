# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 21, 6:05 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1000 windows, 27795 settled trades, 50 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 514 | 34.2 | 34.9 | $-296.26 | -5.8% | $703.74 | -1.0 | done | can't tell from luck |
| reversal_15m_0.10pct | 2833 | 51.1 | 50.4 | $-851.44 | -3.0% | $148.56 | -1.6 | done | can't tell from luck |
| value_ev10 | 1274 | 37.5 | 39.1 | $-899.88 | -7.1% | $100.12 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 2385 | 49.8 | 49.7 | $-1090.34 | -4.6% | $-90.34 | -2.2 | done | losing for real |
| trend_filter | 1663 | 49.5 | 50.8 | $-1244.14 | -7.5% | $-244.14 | -3.1 | done | losing for real |
| value_ev5 | 1929 | 39.6 | 41.0 | $-1270.43 | -6.6% | $-270.43 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 2385 | 50.2 | 50.9 | $-1563.97 | -6.6% | $-563.97 | -3.3 | done | losing for real |
| coinflip | 3993 | 50.3 | 50.3 | $-1775.95 | -4.4% | $-775.95 | -2.8 | done | losing for real |
| momentum_15m_0.10pct | 2833 | 48.9 | 50.3 | $-1937.63 | -6.8% | $-937.63 | -3.7 | done | losing for real |
| momentum_5m_0.00pct | 3993 | 50.7 | 51.5 | $-2230.58 | -5.6% | $-1230.58 | -3.6 | done | losing for real |
| always_up | 3993 | 47.0 | 49.5 | $-3842.22 | -9.6% | $-2842.22 | -6.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6339 | 48.2 | 49.0 | $-3630.43 |
| ETH | 6903 | 48.0 | 48.5 | $-4562.91 |
| SOL | 7265 | 48.2 | 48.5 | $-4154.40 |
| XRP | 7288 | 48.1 | 48.4 | $-4655.09 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
