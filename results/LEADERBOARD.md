# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 19, 8:30 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 818 windows, 22436 settled trades, 61 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 413 | 33.4 | 35.0 | $-341.28 | -8.3% | $658.72 | -1.3 | done | can't tell from luck |
| value_ev10 | 1023 | 37.7 | 39.2 | $-719.76 | -7.0% | $280.24 | -1.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 1877 | 50.0 | 49.6 | $-778.10 | -4.1% | $221.90 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 2295 | 50.8 | 50.6 | $-861.83 | -3.8% | $138.17 | -1.8 | done | can't tell from luck |
| trend_filter | 1316 | 49.9 | 50.9 | $-875.49 | -6.7% | $124.51 | -2.5 | done | losing for real |
| value_ev5 | 1548 | 40.1 | 41.1 | $-933.94 | -6.0% | $66.06 | -2.0 | done | losing for real |
| reversal_60m_0.30pct | 1877 | 50.0 | 51.2 | $-1312.99 | -7.0% | $-312.99 | -3.1 | done | losing for real |
| momentum_15m_0.10pct | 2295 | 49.2 | 50.2 | $-1364.83 | -5.9% | $-364.83 | -2.9 | done | losing for real |
| coinflip | 3264 | 50.1 | 50.3 | $-1462.89 | -4.5% | $-462.89 | -2.6 | done | losing for real |
| momentum_5m_0.00pct | 3264 | 51.2 | 51.7 | $-1479.26 | -4.5% | $-479.26 | -2.7 | done | losing for real |
| always_up | 3264 | 47.5 | 49.7 | $-2835.53 | -8.7% | $-1835.53 | -5.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5089 | 48.2 | 49.1 | $-2992.56 |
| ETH | 5584 | 48.2 | 48.6 | $-3572.81 |
| SOL | 5851 | 48.2 | 48.6 | $-3313.25 |
| XRP | 5912 | 48.4 | 48.5 | $-3087.29 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
