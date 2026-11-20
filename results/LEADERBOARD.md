# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 19, 10:15 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 873 windows, 24099 settled trades, 46 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 454 | 35.5 | 34.9 | $-126.41 | -2.8% | $873.59 | -0.4 | done | can't tell from luck |
| value_ev10 | 1106 | 38.3 | 39.1 | $-595.75 | -5.4% | $404.25 | -1.5 | done | can't tell from luck |
| momentum_60m_0.30pct | 2038 | 50.0 | 49.8 | $-847.75 | -4.2% | $152.25 | -1.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 2461 | 50.7 | 50.5 | $-925.89 | -3.8% | $74.11 | -1.9 | done | can't tell from luck |
| value_ev5 | 1669 | 40.0 | 41.0 | $-968.15 | -5.8% | $31.85 | -2.0 | done | can't tell from luck |
| trend_filter | 1420 | 50.0 | 51.0 | $-974.20 | -6.9% | $25.80 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 2038 | 50.0 | 51.0 | $-1396.13 | -6.9% | $-396.13 | -3.2 | done | losing for real |
| momentum_15m_0.10pct | 2461 | 49.3 | 50.4 | $-1438.59 | -5.8% | $-438.59 | -2.9 | done | losing for real |
| coinflip | 3484 | 50.1 | 50.3 | $-1560.61 | -4.5% | $-560.61 | -2.7 | done | losing for real |
| momentum_5m_0.00pct | 3484 | 51.2 | 51.7 | $-1648.37 | -4.7% | $-648.37 | -2.9 | done | losing for real |
| always_up | 3484 | 47.0 | 49.6 | $-3349.25 | -9.6% | $-2349.25 | -5.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5499 | 48.3 | 49.1 | $-2950.69 |
| ETH | 5992 | 48.1 | 48.5 | $-3834.82 |
| SOL | 6290 | 48.3 | 48.6 | $-3564.48 |
| XRP | 6318 | 48.4 | 48.5 | $-3481.11 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
