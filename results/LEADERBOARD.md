# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 19, 4:35 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 850 windows, 23452 settled trades, 53 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 438 | 34.0 | 34.8 | $-282.45 | -6.4% | $717.55 | -1.0 | done | can't tell from luck |
| momentum_60m_0.30pct | 1983 | 50.3 | 49.7 | $-747.91 | -3.8% | $252.09 | -1.7 | done | can't tell from luck |
| value_ev10 | 1072 | 37.7 | 39.1 | $-748.84 | -7.0% | $251.16 | -1.9 | done | can't tell from luck |
| trend_filter | 1380 | 50.1 | 50.9 | $-909.35 | -6.6% | $90.65 | -2.5 | done | losing for real |
| reversal_15m_0.10pct | 2396 | 50.7 | 50.5 | $-922.70 | -3.9% | $77.30 | -1.9 | done | can't tell from luck |
| value_ev5 | 1619 | 39.8 | 41.0 | $-1061.38 | -6.6% | $-61.38 | -2.2 | done | losing for real |
| momentum_15m_0.10pct | 2396 | 49.3 | 50.4 | $-1442.03 | -6.0% | $-442.03 | -3.0 | done | losing for real |
| reversal_60m_0.30pct | 1983 | 49.7 | 51.0 | $-1505.18 | -7.6% | $-505.18 | -3.5 | done | losing for real |
| coinflip | 3395 | 50.2 | 50.3 | $-1519.04 | -4.5% | $-519.04 | -2.6 | done | losing for real |
| momentum_5m_0.00pct | 3395 | 51.3 | 51.7 | $-1602.41 | -4.7% | $-602.41 | -2.8 | done | losing for real |
| always_up | 3395 | 46.9 | 49.5 | $-3290.31 | -9.7% | $-2290.31 | -5.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5343 | 48.2 | 49.1 | $-3118.11 |
| ETH | 5832 | 48.0 | 48.5 | $-3920.70 |
| SOL | 6117 | 48.2 | 48.5 | $-3667.33 |
| XRP | 6160 | 48.4 | 48.5 | $-3325.45 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
