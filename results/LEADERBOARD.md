# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 13, 1:00 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 212 windows, 5517 settled trades, 71 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 545 | 56.9 | 52.7 | $+265.14 | +4.9% | $1265.14 | +1.2 | done | can't tell from luck |
| reversal_60m_0.30pct | 424 | 55.7 | 52.7 | $+111.71 | +2.6% | $1111.71 | +0.6 | done | can't tell from luck |
| value_ev20 | 104 | 33.7 | 36.9 | $-137.53 | -13.2% | $862.47 | -1.1 | Sun 6:00 AM | too few trades (104/200) |
| value_ev10 | 272 | 36.8 | 40.8 | $-370.93 | -13.6% | $629.07 | -1.9 | done | can't tell from luck |
| trend_filter | 285 | 43.9 | 50.0 | $-442.97 | -15.5% | $557.03 | -2.7 | done | losing for real |
| coinflip | 840 | 50.1 | 51.0 | $-493.04 | -5.9% | $506.96 | -1.8 | done | can't tell from luck |
| value_ev5 | 398 | 38.9 | 42.6 | $-494.10 | -12.4% | $505.90 | -2.2 | done | losing for real |
| momentum_5m_0.00pct | 840 | 50.4 | 51.5 | $-516.50 | -6.1% | $483.50 | -1.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 424 | 44.3 | 49.5 | $-599.72 | -14.1% | $400.28 | -2.9 | done | losing for real |
| momentum_15m_0.10pct | 545 | 43.1 | 49.7 | $-904.99 | -16.6% | $95.01 | -3.9 | done | losing for real |
| always_up | 840 | 46.2 | 50.2 | $-1014.23 | -12.1% | $-14.23 | -3.6 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1224 | 45.9 | 49.7 | $-1318.75 |
| ETH | 1377 | 46.4 | 48.9 | $-1325.66 |
| SOL | 1423 | 47.7 | 49.3 | $-1253.35 |
| XRP | 1493 | 49.3 | 49.3 | $-699.40 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
