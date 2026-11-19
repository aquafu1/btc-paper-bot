# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 19, 6:50 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 811 windows, 22282 settled trades, 27 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 413 | 33.4 | 35.0 | $-341.28 | -8.3% | $658.72 | -1.3 | done | can't tell from luck |
| value_ev10 | 1018 | 37.8 | 39.2 | $-691.12 | -6.8% | $308.88 | -1.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 1866 | 50.0 | 49.6 | $-760.88 | -4.1% | $239.12 | -1.8 | done | can't tell from luck |
| trend_filter | 1306 | 50.1 | 50.9 | $-819.66 | -6.3% | $180.34 | -2.3 | done | losing for real |
| reversal_15m_0.10pct | 2277 | 50.8 | 50.6 | $-859.33 | -3.8% | $140.67 | -1.8 | done | can't tell from luck |
| value_ev5 | 1539 | 40.0 | 41.1 | $-923.25 | -6.0% | $76.75 | -2.0 | done | can't tell from luck |
| reversal_60m_0.30pct | 1866 | 50.0 | 51.2 | $-1306.06 | -7.0% | $-306.06 | -3.1 | done | losing for real |
| momentum_15m_0.10pct | 2277 | 49.2 | 50.2 | $-1331.93 | -5.8% | $-331.93 | -2.8 | done | losing for real |
| coinflip | 3240 | 50.2 | 50.3 | $-1400.79 | -4.3% | $-400.79 | -2.5 | done | losing for real |
| momentum_5m_0.00pct | 3240 | 51.3 | 51.6 | $-1401.53 | -4.3% | $-401.53 | -2.5 | done | losing for real |
| always_up | 3240 | 47.4 | 49.7 | $-2848.03 | -8.8% | $-1848.03 | -5.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5056 | 48.3 | 49.1 | $-2881.22 |
| ETH | 5545 | 48.2 | 48.6 | $-3537.33 |
| SOL | 5808 | 48.2 | 48.6 | $-3253.23 |
| XRP | 5873 | 48.5 | 48.5 | $-3012.08 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
