# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 14, 3:15 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 365 windows, 9846 settled trades, 71 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 189 | 38.1 | 36.4 | $+15.78 | +0.8% | $1015.78 | +0.1 | Sat 8:45 PM | too few trades (189/200) |
| value_ev10 | 477 | 41.3 | 40.3 | $-42.64 | -0.9% | $957.36 | -0.2 | done | can't tell from luck |
| value_ev5 | 706 | 42.5 | 42.0 | $-168.96 | -2.4% | $831.04 | -0.5 | done | can't tell from luck |
| momentum_60m_0.30pct | 809 | 49.3 | 49.7 | $-420.56 | -5.2% | $579.44 | -1.5 | done | can't tell from luck |
| trend_filter | 546 | 48.7 | 50.6 | $-426.99 | -7.8% | $573.01 | -1.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 977 | 51.7 | 52.1 | $-461.61 | -4.7% | $538.39 | -1.6 | done | can't tell from luck |
| reversal_60m_0.30pct | 809 | 50.7 | 52.0 | $-517.12 | -6.4% | $482.88 | -1.9 | done | can't tell from luck |
| momentum_15m_0.10pct | 977 | 48.3 | 49.6 | $-607.99 | -6.2% | $392.01 | -1.9 | done | can't tell from luck |
| coinflip | 1452 | 50.1 | 50.8 | $-732.18 | -5.0% | $267.82 | -2.0 | done | can't tell from luck |
| momentum_5m_0.00pct | 1452 | 49.5 | 51.6 | $-1068.54 | -7.4% | $-68.54 | -2.9 | done | losing for real |
| always_up | 1452 | 45.7 | 50.7 | $-1927.41 | -13.3% | $-927.41 | -5.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2209 | 47.3 | 49.3 | $-1736.84 |
| ETH | 2476 | 47.7 | 48.8 | $-1701.45 |
| SOL | 2553 | 48.1 | 49.4 | $-1725.56 |
| XRP | 2608 | 48.9 | 49.1 | $-1194.37 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
