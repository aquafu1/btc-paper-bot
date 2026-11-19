# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 19, 4:20 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 849 windows, 23415 settled trades, 47 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 438 | 34.0 | 34.8 | $-282.45 | -6.4% | $717.55 | -1.0 | done | can't tell from luck |
| momentum_60m_0.30pct | 1979 | 50.4 | 49.7 | $-707.91 | -3.6% | $292.09 | -1.6 | done | can't tell from luck |
| value_ev10 | 1071 | 37.7 | 39.0 | $-738.84 | -6.9% | $261.16 | -1.8 | done | can't tell from luck |
| trend_filter | 1379 | 50.2 | 50.9 | $-899.35 | -6.5% | $100.65 | -2.5 | done | losing for real |
| reversal_15m_0.10pct | 2391 | 50.7 | 50.5 | $-910.59 | -3.8% | $89.41 | -1.9 | done | can't tell from luck |
| value_ev5 | 1617 | 39.8 | 41.0 | $-1041.38 | -6.4% | $-41.38 | -2.2 | done | losing for real |
| momentum_15m_0.10pct | 2391 | 49.3 | 50.4 | $-1440.69 | -6.0% | $-440.69 | -3.0 | done | losing for real |
| reversal_60m_0.30pct | 1979 | 49.6 | 51.0 | $-1534.99 | -7.8% | $-534.99 | -3.5 | done | losing for real |
| coinflip | 3390 | 50.1 | 50.3 | $-1536.29 | -4.5% | $-536.29 | -2.7 | done | losing for real |
| momentum_5m_0.00pct | 3390 | 51.2 | 51.7 | $-1620.37 | -4.8% | $-620.37 | -2.9 | done | losing for real |
| always_up | 3390 | 46.8 | 49.5 | $-3326.86 | -9.8% | $-2326.86 | -5.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5329 | 48.2 | 49.0 | $-3122.25 |
| ETH | 5832 | 48.0 | 48.5 | $-3920.70 |
| SOL | 6110 | 48.2 | 48.5 | $-3680.83 |
| XRP | 6144 | 48.4 | 48.5 | $-3315.94 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
