# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 16, 6:50 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 571 windows, 15841 settled trades, 28 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1349 | 51.5 | 49.7 | $-158.07 | -1.2% | $841.93 | -0.4 | done | can't tell from luck |
| value_ev20 | 309 | 33.3 | 35.2 | $-327.95 | -10.6% | $672.05 | -1.4 | done | can't tell from luck |
| trend_filter | 920 | 50.9 | 51.1 | $-434.64 | -4.7% | $565.36 | -1.5 | done | can't tell from luck |
| value_ev10 | 748 | 37.6 | 39.4 | $-691.32 | -9.2% | $308.68 | -2.1 | done | losing for real |
| reversal_15m_0.10pct | 1608 | 50.8 | 51.0 | $-818.60 | -5.1% | $181.40 | -2.1 | done | losing for real |
| value_ev5 | 1113 | 39.7 | 41.3 | $-881.72 | -7.9% | $118.28 | -2.3 | done | losing for real |
| momentum_15m_0.10pct | 1608 | 49.2 | 49.9 | $-894.55 | -5.6% | $105.45 | -2.2 | done | losing for real |
| coinflip | 2279 | 49.9 | 50.4 | $-1207.73 | -5.3% | $-207.73 | -2.6 | done | losing for real |
| reversal_60m_0.30pct | 1349 | 48.5 | 51.2 | $-1387.79 | -10.3% | $-387.79 | -3.9 | done | losing for real |
| momentum_5m_0.00pct | 2279 | 50.3 | 51.9 | $-1554.05 | -6.8% | $-554.05 | -3.4 | done | losing for real |
| always_up | 2279 | 47.0 | 49.9 | $-2309.62 | -10.1% | $-1309.62 | -4.9 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3578 | 47.7 | 49.2 | $-2702.25 |
| ETH | 3954 | 48.0 | 48.6 | $-2695.37 |
| SOL | 4130 | 47.8 | 48.7 | $-3072.05 |
| XRP | 4179 | 48.6 | 48.6 | $-2196.37 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
