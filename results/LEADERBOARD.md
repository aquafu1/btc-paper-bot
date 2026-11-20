# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 19, 10:35 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 874 windows, 24138 settled trades, 35 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 454 | 35.5 | 34.9 | $-126.41 | -2.8% | $873.59 | -0.4 | done | can't tell from luck |
| value_ev10 | 1106 | 38.3 | 39.1 | $-595.75 | -5.4% | $404.25 | -1.5 | done | can't tell from luck |
| momentum_60m_0.30pct | 2040 | 50.0 | 49.8 | $-853.37 | -4.2% | $146.63 | -1.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 2466 | 50.6 | 50.5 | $-961.51 | -3.9% | $38.49 | -1.9 | done | can't tell from luck |
| value_ev5 | 1671 | 40.0 | 41.0 | $-962.97 | -5.8% | $37.03 | -2.0 | done | can't tell from luck |
| trend_filter | 1422 | 50.1 | 51.0 | $-964.82 | -6.8% | $35.18 | -2.6 | done | losing for real |
| reversal_60m_0.30pct | 2040 | 50.0 | 51.0 | $-1401.12 | -6.9% | $-401.12 | -3.2 | done | losing for real |
| momentum_15m_0.10pct | 2466 | 49.4 | 50.4 | $-1408.54 | -5.7% | $-408.54 | -2.9 | done | losing for real |
| coinflip | 3491 | 50.1 | 50.3 | $-1551.87 | -4.4% | $-551.87 | -2.6 | done | losing for real |
| momentum_5m_0.00pct | 3491 | 51.2 | 51.8 | $-1641.56 | -4.7% | $-641.56 | -2.9 | done | losing for real |
| always_up | 3491 | 46.9 | 49.6 | $-3404.87 | -9.8% | $-2404.87 | -5.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5502 | 48.3 | 49.1 | $-2963.95 |
| ETH | 6004 | 48.1 | 48.5 | $-3834.27 |
| SOL | 6300 | 48.3 | 48.6 | $-3584.74 |
| XRP | 6332 | 48.4 | 48.5 | $-3489.83 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
