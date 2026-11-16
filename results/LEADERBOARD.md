# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 16, 5:50 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 567 windows, 15734 settled trades, 38 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1337 | 51.4 | 49.7 | $-212.40 | -1.6% | $787.60 | -0.6 | done | can't tell from luck |
| value_ev20 | 309 | 33.3 | 35.2 | $-327.95 | -10.6% | $672.05 | -1.4 | done | can't tell from luck |
| trend_filter | 914 | 50.5 | 51.1 | $-510.45 | -5.6% | $489.55 | -1.7 | done | can't tell from luck |
| value_ev10 | 746 | 37.5 | 39.4 | $-698.44 | -9.4% | $301.56 | -2.1 | done | losing for real |
| reversal_15m_0.10pct | 1597 | 50.8 | 51.0 | $-827.56 | -5.2% | $172.44 | -2.1 | done | losing for real |
| value_ev5 | 1108 | 39.7 | 41.2 | $-880.17 | -7.9% | $119.83 | -2.3 | done | losing for real |
| momentum_15m_0.10pct | 1597 | 49.2 | 49.9 | $-898.25 | -5.6% | $101.75 | -2.3 | done | losing for real |
| coinflip | 2263 | 49.8 | 50.5 | $-1253.94 | -5.5% | $-253.94 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 1337 | 48.6 | 51.2 | $-1342.92 | -10.0% | $-342.92 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 2263 | 50.2 | 51.9 | $-1621.72 | -7.2% | $-621.72 | -3.6 | done | losing for real |
| always_up | 2263 | 47.1 | 49.9 | $-2241.48 | -9.9% | $-1241.48 | -4.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3556 | 47.7 | 49.2 | $-2742.32 |
| ETH | 3927 | 47.9 | 48.6 | $-2780.39 |
| SOL | 4108 | 47.8 | 48.7 | $-3041.06 |
| XRP | 4143 | 48.5 | 48.6 | $-2251.53 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
