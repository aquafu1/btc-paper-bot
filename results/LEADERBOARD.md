# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 19, 2:45 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 795 windows, 21874 settled trades, 55 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 405 | 33.1 | 34.9 | $-372.37 | -9.2% | $627.63 | -1.4 | done | can't tell from luck |
| momentum_60m_0.30pct | 1848 | 50.2 | 49.6 | $-688.43 | -3.7% | $311.57 | -1.6 | done | can't tell from luck |
| value_ev10 | 997 | 37.6 | 39.1 | $-729.85 | -7.3% | $270.15 | -1.9 | done | can't tell from luck |
| trend_filter | 1285 | 50.4 | 50.8 | $-730.66 | -5.7% | $269.34 | -2.1 | done | losing for real |
| reversal_15m_0.10pct | 2234 | 50.8 | 50.6 | $-866.09 | -3.9% | $133.91 | -1.8 | done | can't tell from luck |
| value_ev5 | 1507 | 39.9 | 41.1 | $-935.57 | -6.2% | $64.43 | -2.0 | done | losing for real |
| momentum_15m_0.10pct | 2234 | 49.2 | 50.2 | $-1308.02 | -5.9% | $-308.02 | -2.8 | done | losing for real |
| coinflip | 3172 | 50.3 | 50.3 | $-1347.09 | -4.2% | $-347.09 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 1848 | 49.8 | 51.2 | $-1351.44 | -7.3% | $-351.44 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 3172 | 51.4 | 51.7 | $-1370.48 | -4.3% | $-370.48 | -2.5 | done | losing for real |
| always_up | 3172 | 47.5 | 49.6 | $-2702.92 | -8.5% | $-1702.92 | -4.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4969 | 48.3 | 49.1 | $-2897.76 |
| ETH | 5451 | 48.2 | 48.5 | $-3481.41 |
| SOL | 5697 | 48.3 | 48.6 | $-3190.36 |
| XRP | 5757 | 48.5 | 48.5 | $-2833.38 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
