# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 15, 10:30 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 490 windows, 13461 settled trades, 54 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 249 | 34.5 | 35.8 | $-169.21 | -6.8% | $830.79 | -0.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 1144 | 51.0 | 49.8 | $-197.40 | -1.7% | $802.60 | -0.6 | done | can't tell from luck |
| value_ev10 | 633 | 38.7 | 40.0 | $-410.56 | -6.5% | $589.44 | -1.3 | done | can't tell from luck |
| momentum_15m_0.10pct | 1355 | 50.0 | 50.0 | $-458.56 | -3.4% | $541.44 | -1.2 | done | can't tell from luck |
| value_ev5 | 936 | 40.9 | 41.8 | $-506.78 | -5.4% | $493.22 | -1.4 | done | can't tell from luck |
| trend_filter | 789 | 49.4 | 50.7 | $-540.26 | -6.8% | $459.74 | -2.0 | done | can't tell from luck |
| reversal_15m_0.10pct | 1355 | 50.0 | 51.5 | $-933.87 | -6.9% | $66.13 | -2.6 | done | losing for real |
| coinflip | 1952 | 50.0 | 50.8 | $-990.92 | -5.1% | $9.08 | -2.3 | done | losing for real |
| reversal_60m_0.30pct | 1144 | 49.0 | 51.4 | $-1030.14 | -9.0% | $-30.14 | -3.1 | done | losing for real |
| momentum_5m_0.00pct | 1952 | 49.5 | 51.7 | $-1467.57 | -7.5% | $-467.57 | -3.4 | done | losing for real |
| always_up | 1952 | 46.4 | 50.4 | $-2249.97 | -11.5% | $-1249.97 | -5.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3034 | 47.3 | 49.3 | $-2448.74 |
| ETH | 3373 | 48.1 | 48.8 | $-2125.44 |
| SOL | 3512 | 47.8 | 49.2 | $-2497.20 |
| XRP | 3542 | 48.4 | 48.9 | $-1883.86 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
