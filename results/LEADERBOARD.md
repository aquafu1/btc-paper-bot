# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 19, 9:20 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 869 windows, 23985 settled trades, 42 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 451 | 35.5 | 34.9 | $-124.46 | -2.8% | $875.54 | -0.4 | done | can't tell from luck |
| value_ev10 | 1099 | 38.4 | 39.1 | $-573.48 | -5.2% | $426.52 | -1.4 | done | can't tell from luck |
| momentum_60m_0.30pct | 2027 | 50.0 | 49.7 | $-845.96 | -4.2% | $154.04 | -1.9 | done | can't tell from luck |
| value_ev5 | 1661 | 40.1 | 41.0 | $-935.88 | -5.6% | $64.12 | -1.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 2449 | 50.6 | 50.5 | $-955.00 | -3.9% | $45.00 | -1.9 | done | can't tell from luck |
| trend_filter | 1409 | 49.9 | 50.9 | $-972.42 | -6.9% | $27.58 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 2027 | 50.0 | 51.0 | $-1373.65 | -6.8% | $-373.65 | -3.1 | done | losing for real |
| momentum_15m_0.10pct | 2449 | 49.4 | 50.4 | $-1379.65 | -5.6% | $-379.65 | -2.8 | done | losing for real |
| coinflip | 3471 | 50.1 | 50.3 | $-1524.93 | -4.4% | $-524.93 | -2.6 | done | losing for real |
| momentum_5m_0.00pct | 3471 | 51.1 | 51.7 | $-1656.97 | -4.8% | $-656.97 | -2.9 | done | losing for real |
| always_up | 3471 | 46.9 | 49.6 | $-3357.85 | -9.7% | $-2357.85 | -5.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5474 | 48.3 | 49.0 | $-2919.52 |
| ETH | 5969 | 48.1 | 48.5 | $-3844.01 |
| SOL | 6261 | 48.3 | 48.6 | $-3458.27 |
| XRP | 6281 | 48.3 | 48.5 | $-3478.45 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
