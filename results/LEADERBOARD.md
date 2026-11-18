# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 18, 1:15 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 693 windows, 19164 settled trades, 54 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 368 | 34.0 | 34.9 | $-262.42 | -7.1% | $737.58 | -1.0 | done | can't tell from luck |
| momentum_60m_0.30pct | 1617 | 50.4 | 49.5 | $-429.72 | -2.7% | $570.28 | -1.1 | done | can't tell from luck |
| value_ev10 | 888 | 38.2 | 39.1 | $-558.58 | -6.3% | $441.42 | -1.5 | done | can't tell from luck |
| trend_filter | 1117 | 50.5 | 50.9 | $-572.75 | -5.1% | $427.25 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 1965 | 51.3 | 50.8 | $-635.01 | -3.2% | $364.99 | -1.4 | done | can't tell from luck |
| value_ev5 | 1335 | 40.7 | 41.1 | $-637.18 | -4.8% | $362.82 | -1.5 | done | can't tell from luck |
| coinflip | 2764 | 50.1 | 50.2 | $-1230.37 | -4.5% | $-230.37 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 1617 | 49.6 | 51.3 | $-1277.86 | -7.9% | $-277.86 | -3.3 | done | losing for real |
| momentum_15m_0.10pct | 1965 | 48.7 | 50.0 | $-1284.69 | -6.5% | $-284.69 | -2.9 | done | losing for real |
| momentum_5m_0.00pct | 2764 | 50.8 | 51.8 | $-1519.24 | -5.5% | $-519.24 | -3.0 | done | losing for real |
| always_up | 2764 | 47.4 | 49.6 | $-2374.35 | -8.6% | $-1374.35 | -4.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4348 | 48.2 | 49.1 | $-2533.07 |
| ETH | 4773 | 48.2 | 48.5 | $-2810.31 |
| SOL | 4996 | 48.1 | 48.6 | $-2950.07 |
| XRP | 5047 | 48.5 | 48.3 | $-2488.72 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
