# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 19, 12:35 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 834 windows, 22933 settled trades, 44 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 423 | 33.1 | 34.9 | $-400.80 | -9.5% | $599.20 | -1.5 | done | can't tell from luck |
| reversal_15m_0.10pct | 2341 | 51.0 | 50.6 | $-845.98 | -3.6% | $154.02 | -1.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 1927 | 50.0 | 49.7 | $-851.22 | -4.4% | $148.78 | -1.9 | done | can't tell from luck |
| value_ev10 | 1047 | 37.2 | 39.1 | $-873.78 | -8.3% | $126.22 | -2.2 | done | losing for real |
| trend_filter | 1352 | 49.9 | 50.8 | $-951.58 | -7.0% | $48.42 | -2.7 | done | losing for real |
| value_ev5 | 1585 | 39.6 | 41.1 | $-1137.89 | -7.2% | $-137.89 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 1927 | 50.0 | 51.1 | $-1382.72 | -7.2% | $-382.72 | -3.2 | done | losing for real |
| coinflip | 3330 | 50.3 | 50.3 | $-1426.52 | -4.3% | $-426.52 | -2.5 | done | losing for real |
| momentum_15m_0.10pct | 2341 | 49.0 | 50.3 | $-1493.75 | -6.4% | $-493.75 | -3.1 | done | losing for real |
| momentum_5m_0.00pct | 3330 | 51.2 | 51.7 | $-1566.17 | -4.7% | $-566.17 | -2.8 | done | losing for real |
| always_up | 3330 | 47.3 | 49.6 | $-3022.79 | -9.1% | $-2022.79 | -5.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5215 | 48.1 | 49.1 | $-3270.40 |
| ETH | 5706 | 48.0 | 48.5 | $-3920.78 |
| SOL | 5984 | 48.3 | 48.6 | $-3468.33 |
| XRP | 6028 | 48.4 | 48.5 | $-3293.71 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
