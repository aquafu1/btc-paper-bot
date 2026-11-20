# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 19, 8:30 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 866 windows, 23852 settled trades, 68 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 445 | 34.6 | 34.8 | $-223.90 | -5.0% | $776.10 | -0.8 | done | can't tell from luck |
| value_ev10 | 1092 | 38.0 | 39.1 | $-688.09 | -6.3% | $311.91 | -1.7 | done | can't tell from luck |
| momentum_60m_0.30pct | 2012 | 50.1 | 49.7 | $-796.76 | -4.0% | $203.24 | -1.8 | done | can't tell from luck |
| trend_filter | 1398 | 50.3 | 50.9 | $-862.42 | -6.2% | $137.58 | -2.4 | done | losing for real |
| reversal_15m_0.10pct | 2436 | 50.6 | 50.5 | $-990.67 | -4.1% | $9.33 | -2.0 | done | losing for real |
| value_ev5 | 1653 | 39.9 | 41.0 | $-1040.49 | -6.3% | $-40.49 | -2.2 | done | losing for real |
| momentum_15m_0.10pct | 2436 | 49.4 | 50.4 | $-1374.01 | -5.6% | $-374.01 | -2.8 | done | losing for real |
| reversal_60m_0.30pct | 2012 | 49.9 | 51.0 | $-1464.58 | -7.3% | $-464.58 | -3.3 | done | losing for real |
| momentum_5m_0.00pct | 3456 | 51.4 | 51.7 | $-1506.97 | -4.4% | $-506.97 | -2.6 | done | losing for real |
| coinflip | 3456 | 50.1 | 50.3 | $-1561.36 | -4.5% | $-561.36 | -2.7 | done | losing for real |
| always_up | 3456 | 46.9 | 49.6 | $-3364.97 | -9.7% | $-2364.97 | -5.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5440 | 48.3 | 49.0 | $-2983.68 |
| ETH | 5934 | 48.1 | 48.5 | $-3893.86 |
| SOL | 6223 | 48.3 | 48.6 | $-3539.59 |
| XRP | 6255 | 48.3 | 48.5 | $-3457.08 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
