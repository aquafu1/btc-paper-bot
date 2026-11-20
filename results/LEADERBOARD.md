# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 19, 9:15 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 869 windows, 23952 settled trades, 75 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 448 | 35.0 | 34.9 | $-178.27 | -4.0% | $821.73 | -0.6 | done | can't tell from luck |
| value_ev10 | 1096 | 38.2 | 39.1 | $-627.29 | -5.7% | $372.71 | -1.5 | done | can't tell from luck |
| momentum_60m_0.30pct | 2024 | 50.0 | 49.7 | $-815.96 | -4.0% | $184.04 | -1.8 | done | can't tell from luck |
| trend_filter | 1406 | 50.0 | 50.9 | $-942.42 | -6.7% | $57.58 | -2.6 | done | losing for real |
| value_ev5 | 1658 | 40.0 | 41.0 | $-989.69 | -6.0% | $10.31 | -2.1 | done | losing for real |
| reversal_15m_0.10pct | 2446 | 50.5 | 50.5 | $-1008.81 | -4.1% | $-8.81 | -2.0 | done | losing for real |
| momentum_15m_0.10pct | 2446 | 49.5 | 50.4 | $-1349.65 | -5.5% | $-349.65 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 2024 | 50.0 | 51.1 | $-1427.45 | -7.1% | $-427.45 | -3.2 | done | losing for real |
| coinflip | 3468 | 50.1 | 50.3 | $-1552.90 | -4.5% | $-552.90 | -2.7 | done | losing for real |
| momentum_5m_0.00pct | 3468 | 51.2 | 51.7 | $-1626.97 | -4.7% | $-626.97 | -2.9 | done | losing for real |
| always_up | 3468 | 46.9 | 49.6 | $-3327.85 | -9.6% | $-2327.85 | -5.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5463 | 48.3 | 49.1 | $-2993.72 |
| ETH | 5958 | 48.1 | 48.5 | $-3863.18 |
| SOL | 6250 | 48.3 | 48.6 | $-3511.90 |
| XRP | 6281 | 48.3 | 48.5 | $-3478.45 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
