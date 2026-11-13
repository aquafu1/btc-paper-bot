# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 12, 9:30 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 198 windows, 5106 settled trades, 60 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 498 | 59.2 | 52.7 | $+444.26 | +8.9% | $1444.26 | +2.1 | done | real edge? (z>=2) |
| reversal_60m_0.30pct | 376 | 58.8 | 52.8 | $+281.99 | +7.5% | $1281.99 | +1.6 | done | can't tell from luck |
| value_ev20 | 99 | 30.3 | 37.1 | $-238.58 | -24.1% | $761.42 | -2.0 | Sun 4:30 AM | too few trades (99/200) |
| momentum_5m_0.00pct | 784 | 51.4 | 51.4 | $-343.19 | -4.4% | $656.81 | -1.3 | done | can't tell from luck |
| trend_filter | 259 | 42.5 | 49.7 | $-472.19 | -18.2% | $527.81 | -3.0 | done | losing for real |
| coinflip | 784 | 50.3 | 51.0 | $-484.95 | -6.2% | $515.05 | -1.8 | done | can't tell from luck |
| value_ev10 | 264 | 35.2 | 41.0 | $-494.03 | -18.7% | $505.97 | -2.7 | done | losing for real |
| value_ev5 | 384 | 38.0 | 42.7 | $-595.55 | -15.5% | $404.45 | -2.8 | done | losing for real |
| momentum_60m_0.30pct | 376 | 41.2 | 49.3 | $-773.28 | -20.6% | $226.72 | -4.1 | done | losing for real |
| always_up | 784 | 46.0 | 50.2 | $-1026.42 | -13.1% | $-26.42 | -3.8 | done | losing for real |
| momentum_15m_0.10pct | 498 | 40.8 | 49.5 | $-1060.54 | -21.3% | $-60.54 | -4.9 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1125 | 45.8 | 49.5 | $-1275.51 |
| ETH | 1270 | 45.9 | 48.9 | $-1505.85 |
| SOL | 1323 | 47.7 | 49.1 | $-1201.08 |
| XRP | 1388 | 49.1 | 49.2 | $-780.04 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
