# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 18, 8:15 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 769 windows, 21210 settled trades, 47 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 401 | 33.2 | 34.9 | $-361.45 | -9.0% | $638.55 | -1.4 | done | can't tell from luck |
| reversal_15m_0.10pct | 2167 | 51.4 | 50.6 | $-562.29 | -2.6% | $437.71 | -1.2 | done | can't tell from luck |
| value_ev10 | 972 | 37.8 | 39.1 | $-674.62 | -6.9% | $325.38 | -1.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 1792 | 49.7 | 49.6 | $-772.11 | -4.3% | $227.89 | -1.8 | done | can't tell from luck |
| value_ev5 | 1468 | 40.1 | 41.0 | $-854.74 | -5.8% | $145.26 | -1.9 | done | can't tell from luck |
| trend_filter | 1247 | 49.6 | 50.8 | $-855.43 | -6.9% | $144.57 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 1792 | 50.3 | 51.2 | $-1150.93 | -6.4% | $-150.93 | -2.8 | done | losing for real |
| coinflip | 3068 | 50.3 | 50.3 | $-1234.37 | -4.0% | $-234.37 | -2.2 | done | losing for real |
| momentum_15m_0.10pct | 2167 | 48.6 | 50.2 | $-1519.52 | -7.0% | $-519.52 | -3.3 | done | losing for real |
| momentum_5m_0.00pct | 3068 | 50.9 | 51.6 | $-1551.76 | -5.1% | $-551.76 | -2.9 | done | losing for real |
| always_up | 3068 | 47.2 | 49.6 | $-2765.06 | -9.0% | $-1765.06 | -5.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4812 | 48.2 | 49.1 | $-2871.13 |
| ETH | 5294 | 48.0 | 48.5 | $-3501.39 |
| SOL | 5522 | 48.0 | 48.5 | $-3252.28 |
| XRP | 5582 | 48.5 | 48.4 | $-2677.49 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
