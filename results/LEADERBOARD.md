# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 19, 6:45 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 811 windows, 22254 settled trades, 55 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 413 | 33.4 | 35.0 | $-341.28 | -8.3% | $658.72 | -1.3 | done | can't tell from luck |
| value_ev10 | 1018 | 37.8 | 39.2 | $-691.12 | -6.8% | $308.88 | -1.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 1864 | 50.0 | 49.6 | $-756.58 | -4.1% | $243.42 | -1.8 | done | can't tell from luck |
| trend_filter | 1302 | 50.1 | 50.9 | $-811.06 | -6.2% | $188.94 | -2.3 | done | losing for real |
| reversal_15m_0.10pct | 2273 | 50.8 | 50.6 | $-862.42 | -3.8% | $137.58 | -1.8 | done | can't tell from luck |
| value_ev5 | 1539 | 40.0 | 41.1 | $-923.25 | -6.0% | $76.75 | -2.0 | done | can't tell from luck |
| reversal_60m_0.30pct | 1864 | 50.0 | 51.2 | $-1310.47 | -7.0% | $-310.47 | -3.1 | done | losing for real |
| momentum_15m_0.10pct | 2273 | 49.2 | 50.2 | $-1323.33 | -5.8% | $-323.33 | -2.8 | done | losing for real |
| momentum_5m_0.00pct | 3236 | 51.3 | 51.6 | $-1392.93 | -4.3% | $-392.93 | -2.5 | done | losing for real |
| coinflip | 3236 | 50.2 | 50.3 | $-1416.60 | -4.4% | $-416.60 | -2.5 | done | losing for real |
| always_up | 3236 | 47.4 | 49.7 | $-2851.12 | -8.8% | $-1851.12 | -5.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5050 | 48.3 | 49.1 | $-2858.56 |
| ETH | 5537 | 48.1 | 48.5 | $-3535.83 |
| SOL | 5800 | 48.2 | 48.6 | $-3270.89 |
| XRP | 5867 | 48.4 | 48.5 | $-3014.88 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
