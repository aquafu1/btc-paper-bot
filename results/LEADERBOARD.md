# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 16, 6:05 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 568 windows, 15765 settled trades, 30 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1341 | 51.3 | 49.7 | $-231.06 | -1.7% | $768.94 | -0.6 | done | can't tell from luck |
| value_ev20 | 309 | 33.3 | 35.2 | $-327.95 | -10.6% | $672.05 | -1.4 | done | can't tell from luck |
| trend_filter | 915 | 50.6 | 51.1 | $-499.11 | -5.5% | $500.89 | -1.7 | done | can't tell from luck |
| value_ev10 | 746 | 37.5 | 39.4 | $-698.44 | -9.4% | $301.56 | -2.1 | done | losing for real |
| reversal_15m_0.10pct | 1601 | 50.8 | 51.0 | $-809.74 | -5.1% | $190.26 | -2.1 | done | losing for real |
| value_ev5 | 1110 | 39.7 | 41.3 | $-878.84 | -7.9% | $121.16 | -2.3 | done | losing for real |
| momentum_15m_0.10pct | 1601 | 49.2 | 49.9 | $-916.92 | -5.7% | $83.08 | -2.3 | done | losing for real |
| coinflip | 2267 | 49.8 | 50.5 | $-1231.47 | -5.4% | $-231.47 | -2.6 | done | losing for real |
| reversal_60m_0.30pct | 1341 | 48.7 | 51.2 | $-1325.10 | -9.9% | $-325.10 | -3.7 | done | losing for real |
| momentum_5m_0.00pct | 2267 | 50.3 | 51.9 | $-1582.57 | -7.0% | $-582.57 | -3.5 | done | losing for real |
| always_up | 2267 | 47.2 | 49.9 | $-2223.66 | -9.8% | $-1223.66 | -4.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3564 | 47.7 | 49.2 | $-2725.82 |
| ETH | 3927 | 47.9 | 48.6 | $-2780.39 |
| SOL | 4115 | 47.8 | 48.7 | $-3044.32 |
| XRP | 4159 | 48.6 | 48.6 | $-2174.31 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
