# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 17, 6:15 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 617 windows, 17050 settled trades, 60 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1440 | 51.4 | 49.6 | $-115.69 | -0.8% | $884.31 | -0.3 | done | can't tell from luck |
| value_ev20 | 328 | 34.1 | 35.3 | $-254.70 | -7.8% | $745.30 | -1.1 | done | can't tell from luck |
| trend_filter | 987 | 50.7 | 51.0 | $-461.42 | -4.7% | $538.58 | -1.5 | done | can't tell from luck |
| value_ev10 | 792 | 38.0 | 39.4 | $-601.87 | -7.6% | $398.13 | -1.8 | done | can't tell from luck |
| value_ev5 | 1195 | 40.2 | 41.3 | $-794.88 | -6.7% | $205.12 | -2.0 | done | can't tell from luck |
| momentum_15m_0.10pct | 1744 | 49.5 | 50.0 | $-858.14 | -4.9% | $141.86 | -2.1 | done | losing for real |
| reversal_15m_0.10pct | 1744 | 50.5 | 51.0 | $-884.83 | -5.1% | $115.17 | -2.1 | done | losing for real |
| coinflip | 2460 | 50.1 | 50.5 | $-1156.95 | -4.7% | $-156.95 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 1440 | 48.6 | 51.3 | $-1406.34 | -9.8% | $-406.34 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 2460 | 50.5 | 51.8 | $-1458.68 | -5.9% | $-458.68 | -3.0 | done | losing for real |
| always_up | 2460 | 47.3 | 49.7 | $-2194.00 | -8.9% | $-1194.00 | -4.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3872 | 48.2 | 49.2 | $-2435.94 |
| ETH | 4266 | 48.0 | 48.6 | $-2714.15 |
| SOL | 4428 | 48.0 | 48.8 | $-2881.11 |
| XRP | 4484 | 48.6 | 48.6 | $-2156.28 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
