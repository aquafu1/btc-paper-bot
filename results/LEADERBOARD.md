# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 12, 10:20 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 201 windows, 5218 settled trades, 40 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 513 | 57.5 | 52.7 | $+294.26 | +5.7% | $1294.26 | +1.4 | done | can't tell from luck |
| reversal_60m_0.30pct | 391 | 56.5 | 52.8 | $+131.99 | +3.4% | $1131.99 | +0.7 | done | can't tell from luck |
| value_ev20 | 99 | 30.3 | 37.1 | $-238.58 | -24.1% | $761.42 | -2.0 | Sun 6:30 AM | too few trades (99/200) |
| momentum_5m_0.00pct | 799 | 51.3 | 51.4 | $-352.92 | -4.4% | $647.08 | -1.3 | done | can't tell from luck |
| trend_filter | 266 | 44.0 | 49.7 | $-401.92 | -15.1% | $598.08 | -2.5 | done | losing for real |
| value_ev10 | 264 | 35.2 | 41.0 | $-494.03 | -18.7% | $505.97 | -2.7 | done | losing for real |
| coinflip | 799 | 50.2 | 51.0 | $-500.24 | -6.3% | $499.76 | -1.8 | done | can't tell from luck |
| value_ev5 | 384 | 38.0 | 42.7 | $-595.55 | -15.5% | $404.45 | -2.8 | done | losing for real |
| momentum_60m_0.30pct | 391 | 43.5 | 49.4 | $-630.74 | -16.1% | $369.26 | -3.2 | done | losing for real |
| momentum_15m_0.10pct | 513 | 42.5 | 49.6 | $-918.00 | -17.9% | $82.00 | -4.1 | done | losing for real |
| always_up | 799 | 45.2 | 50.3 | $-1176.42 | -14.7% | $-176.42 | -4.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1155 | 45.8 | 49.6 | $-1303.04 |
| ETH | 1293 | 46.1 | 48.9 | $-1477.23 |
| SOL | 1352 | 47.5 | 49.2 | $-1273.12 |
| XRP | 1418 | 49.0 | 49.3 | $-828.76 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
