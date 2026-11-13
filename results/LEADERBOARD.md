# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 12, 10:00 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 200 windows, 5166 settled trades, 60 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 506 | 58.3 | 52.7 | $+364.26 | +7.2% | $1364.26 | +1.7 | done | can't tell from luck |
| reversal_60m_0.30pct | 384 | 57.6 | 52.8 | $+201.99 | +5.3% | $1201.99 | +1.1 | done | can't tell from luck |
| value_ev20 | 99 | 30.3 | 37.1 | $-238.58 | -24.1% | $761.42 | -2.0 | Sun 5:30 AM | too few trades (99/200) |
| momentum_5m_0.00pct | 792 | 51.4 | 51.4 | $-342.82 | -4.3% | $657.18 | -1.3 | done | can't tell from luck |
| trend_filter | 263 | 43.3 | 49.7 | $-431.82 | -16.4% | $568.18 | -2.7 | done | losing for real |
| value_ev10 | 264 | 35.2 | 41.0 | $-494.03 | -18.7% | $505.97 | -2.7 | done | losing for real |
| coinflip | 792 | 50.1 | 51.0 | $-507.24 | -6.4% | $492.76 | -1.9 | done | can't tell from luck |
| value_ev5 | 384 | 38.0 | 42.7 | $-595.55 | -15.5% | $404.45 | -2.8 | done | losing for real |
| momentum_60m_0.30pct | 384 | 42.4 | 49.4 | $-700.07 | -18.2% | $299.93 | -3.6 | done | losing for real |
| momentum_15m_0.10pct | 506 | 41.7 | 49.6 | $-987.34 | -19.5% | $12.66 | -4.5 | done | losing for real |
| always_up | 792 | 45.6 | 50.2 | $-1106.42 | -14.0% | $-106.42 | -4.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1140 | 45.8 | 49.6 | $-1291.45 |
| ETH | 1285 | 46.0 | 48.9 | $-1493.75 |
| SOL | 1338 | 47.6 | 49.2 | $-1234.28 |
| XRP | 1403 | 49.0 | 49.2 | $-818.13 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
