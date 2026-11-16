# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 16, 5:45 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 567 windows, 15712 settled trades, 60 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1335 | 51.3 | 49.7 | $-229.95 | -1.7% | $770.05 | -0.6 | done | can't tell from luck |
| value_ev20 | 309 | 33.3 | 35.2 | $-327.95 | -10.6% | $672.05 | -1.4 | done | can't tell from luck |
| trend_filter | 911 | 50.4 | 51.1 | $-536.93 | -5.9% | $463.07 | -1.8 | done | can't tell from luck |
| value_ev10 | 746 | 37.5 | 39.4 | $-698.44 | -9.4% | $301.56 | -2.1 | done | losing for real |
| reversal_15m_0.10pct | 1594 | 50.9 | 51.0 | $-797.56 | -5.0% | $202.44 | -2.0 | done | losing for real |
| value_ev5 | 1108 | 39.7 | 41.2 | $-880.17 | -7.9% | $119.83 | -2.3 | done | losing for real |
| momentum_15m_0.10pct | 1594 | 49.1 | 49.9 | $-924.74 | -5.8% | $75.26 | -2.3 | done | losing for real |
| coinflip | 2260 | 49.8 | 50.5 | $-1262.18 | -5.6% | $-262.18 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 1335 | 48.7 | 51.2 | $-1322.92 | -9.9% | $-322.92 | -3.7 | done | losing for real |
| momentum_5m_0.00pct | 2260 | 50.1 | 51.9 | $-1648.21 | -7.3% | $-648.21 | -3.6 | done | losing for real |
| always_up | 2260 | 47.2 | 49.9 | $-2211.48 | -9.8% | $-1211.48 | -4.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3550 | 47.6 | 49.2 | $-2758.06 |
| ETH | 3919 | 47.9 | 48.6 | $-2773.38 |
| SOL | 4100 | 47.8 | 48.7 | $-3057.56 |
| XRP | 4143 | 48.5 | 48.6 | $-2251.53 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
