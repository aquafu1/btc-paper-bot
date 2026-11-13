# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 12, 9:45 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 199 windows, 5138 settled trades, 59 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 502 | 58.8 | 52.7 | $+404.26 | +8.1% | $1404.26 | +1.9 | done | can't tell from luck |
| reversal_60m_0.30pct | 380 | 58.2 | 52.8 | $+241.99 | +6.4% | $1241.99 | +1.3 | done | can't tell from luck |
| value_ev20 | 99 | 30.3 | 37.1 | $-238.58 | -24.1% | $761.42 | -2.0 | Sun 5:00 AM | too few trades (99/200) |
| momentum_5m_0.00pct | 788 | 51.6 | 51.4 | $-302.82 | -3.8% | $697.18 | -1.1 | done | can't tell from luck |
| trend_filter | 263 | 43.3 | 49.7 | $-431.82 | -16.4% | $568.18 | -2.7 | done | losing for real |
| value_ev10 | 264 | 35.2 | 41.0 | $-494.03 | -18.7% | $505.97 | -2.7 | done | losing for real |
| coinflip | 788 | 50.1 | 51.0 | $-503.59 | -6.4% | $496.41 | -1.9 | done | can't tell from luck |
| value_ev5 | 384 | 38.0 | 42.7 | $-595.55 | -15.5% | $404.45 | -2.8 | done | losing for real |
| momentum_60m_0.30pct | 380 | 41.8 | 49.3 | $-732.91 | -19.3% | $267.09 | -3.8 | done | losing for real |
| momentum_15m_0.10pct | 502 | 41.2 | 49.5 | $-1020.17 | -20.3% | $-20.17 | -4.7 | done | losing for real |
| always_up | 788 | 45.8 | 50.2 | $-1066.42 | -13.5% | $-66.42 | -3.9 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1133 | 45.8 | 49.6 | $-1275.21 |
| ETH | 1278 | 46.0 | 48.9 | $-1479.02 |
| SOL | 1331 | 47.7 | 49.2 | $-1200.78 |
| XRP | 1396 | 49.1 | 49.2 | $-784.62 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
