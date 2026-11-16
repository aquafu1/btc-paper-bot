# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 15, 6:45 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 475 windows, 13020 settled trades, 69 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 238 | 35.3 | 35.9 | $-125.26 | -5.3% | $874.74 | -0.6 | done | can't tell from luck |
| momentum_60m_0.30pct | 1100 | 50.7 | 50.0 | $-301.76 | -2.7% | $698.24 | -0.9 | done | can't tell from luck |
| value_ev10 | 614 | 39.3 | 40.2 | $-344.93 | -5.6% | $655.07 | -1.2 | done | can't tell from luck |
| momentum_15m_0.10pct | 1314 | 50.2 | 50.1 | $-441.21 | -3.4% | $558.79 | -1.2 | done | can't tell from luck |
| value_ev5 | 909 | 41.1 | 41.9 | $-487.62 | -5.4% | $512.38 | -1.4 | done | can't tell from luck |
| trend_filter | 755 | 49.4 | 50.8 | $-505.90 | -6.7% | $494.10 | -1.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 1314 | 49.8 | 51.4 | $-915.74 | -7.0% | $84.26 | -2.6 | done | losing for real |
| reversal_60m_0.30pct | 1100 | 49.3 | 51.4 | $-924.14 | -8.4% | $75.86 | -2.8 | done | losing for real |
| coinflip | 1892 | 49.9 | 50.8 | $-1030.59 | -5.4% | $-30.59 | -2.4 | done | losing for real |
| momentum_5m_0.00pct | 1892 | 49.6 | 51.7 | $-1406.53 | -7.4% | $-406.53 | -3.4 | done | losing for real |
| always_up | 1892 | 46.6 | 50.4 | $-2128.70 | -11.3% | $-1128.70 | -5.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2940 | 47.5 | 49.3 | $-2255.83 |
| ETH | 3263 | 48.1 | 48.9 | $-2152.65 |
| SOL | 3390 | 47.7 | 49.3 | $-2504.71 |
| XRP | 3427 | 48.7 | 49.1 | $-1699.18 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
