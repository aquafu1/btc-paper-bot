# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 26, 6:20 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1481 windows, 37211 settled trades, 357 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 754 | 34.4 | 35.4 | $-573.12 | -7.6% | $426.88 | -1.6 | done | can't tell from luck |
| value_ev10 | 1814 | 38.5 | 39.2 | $-945.06 | -5.2% | $54.94 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 3706 | 50.9 | 50.1 | $-1010.97 | -2.7% | $-10.97 | -1.7 | done | can't tell from luck |
| value_ev5 | 2735 | 40.5 | 41.1 | $-1396.86 | -5.1% | $-396.86 | -2.3 | done | losing for real |
| reversal_60m_0.30pct | 3113 | 50.9 | 51.0 | $-1525.30 | -4.9% | $-525.30 | -2.8 | done | losing for real |
| momentum_60m_0.30pct | 3113 | 49.1 | 49.2 | $-1596.03 | -5.1% | $-596.03 | -2.8 | done | losing for real |
| trend_filter | 2211 | 48.5 | 50.3 | $-1933.15 | -8.7% | $-933.15 | -4.2 | done | losing for real |
| momentum_15m_0.10pct | 3706 | 49.1 | 50.2 | $-2274.40 | -6.1% | $-1274.40 | -3.8 | done | losing for real |
| coinflip | 5353 | 50.0 | 50.0 | $-2355.25 | -4.4% | $-1355.25 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 5353 | 50.0 | 51.3 | $-3442.58 | -6.4% | $-2442.58 | -4.8 | done | losing for real |
| always_up | 5353 | 48.1 | 49.2 | $-3510.14 | -6.6% | $-2510.14 | -4.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 9591 | 48.0 | 48.7 | $-5264.43 |
| ETH | 10310 | 47.9 | 47.9 | $-5714.20 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
