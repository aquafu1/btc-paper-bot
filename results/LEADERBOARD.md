# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 16, 6:45 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 571 windows, 15827 settled trades, 42 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1348 | 51.5 | 49.7 | $-165.08 | -1.2% | $834.92 | -0.5 | done | can't tell from luck |
| value_ev20 | 309 | 33.3 | 35.2 | $-327.95 | -10.6% | $672.05 | -1.4 | done | can't tell from luck |
| trend_filter | 920 | 50.9 | 51.1 | $-434.64 | -4.7% | $565.36 | -1.5 | done | can't tell from luck |
| value_ev10 | 747 | 37.6 | 39.4 | $-681.32 | -9.1% | $318.68 | -2.1 | done | losing for real |
| reversal_15m_0.10pct | 1608 | 50.8 | 51.0 | $-818.60 | -5.1% | $181.40 | -2.1 | done | losing for real |
| value_ev5 | 1111 | 39.8 | 41.3 | $-861.72 | -7.8% | $138.28 | -2.2 | done | losing for real |
| momentum_15m_0.10pct | 1608 | 49.2 | 49.9 | $-894.55 | -5.6% | $105.45 | -2.2 | done | losing for real |
| coinflip | 2276 | 49.9 | 50.4 | $-1210.52 | -5.3% | $-210.52 | -2.6 | done | losing for real |
| reversal_60m_0.30pct | 1348 | 48.5 | 51.2 | $-1377.79 | -10.2% | $-377.79 | -3.9 | done | losing for real |
| momentum_5m_0.00pct | 2276 | 50.4 | 51.9 | $-1524.05 | -6.7% | $-524.05 | -3.3 | done | losing for real |
| always_up | 2276 | 47.1 | 49.9 | $-2279.62 | -10.0% | $-1279.62 | -4.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3578 | 47.7 | 49.2 | $-2702.25 |
| ETH | 3949 | 48.0 | 48.6 | $-2679.40 |
| SOL | 4126 | 47.8 | 48.7 | $-3047.83 |
| XRP | 4174 | 48.6 | 48.6 | $-2146.37 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
