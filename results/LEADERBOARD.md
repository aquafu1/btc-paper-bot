# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 19, 4:15 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 849 windows, 23400 settled trades, 62 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 438 | 34.0 | 34.8 | $-282.45 | -6.4% | $717.55 | -1.0 | done | can't tell from luck |
| momentum_60m_0.30pct | 1977 | 50.4 | 49.7 | $-687.91 | -3.5% | $312.09 | -1.6 | done | can't tell from luck |
| value_ev10 | 1071 | 37.7 | 39.0 | $-738.84 | -6.9% | $261.16 | -1.8 | done | can't tell from luck |
| trend_filter | 1378 | 50.2 | 50.9 | $-889.35 | -6.5% | $110.65 | -2.5 | done | losing for real |
| reversal_15m_0.10pct | 2389 | 50.7 | 50.5 | $-932.55 | -3.9% | $67.45 | -1.9 | done | can't tell from luck |
| value_ev5 | 1617 | 39.8 | 41.0 | $-1041.38 | -6.4% | $-41.38 | -2.2 | done | losing for real |
| momentum_15m_0.10pct | 2389 | 49.3 | 50.4 | $-1420.69 | -5.9% | $-420.69 | -2.9 | done | losing for real |
| coinflip | 3388 | 50.1 | 50.3 | $-1539.68 | -4.5% | $-539.68 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 1977 | 49.6 | 51.0 | $-1556.96 | -7.9% | $-556.96 | -3.6 | done | losing for real |
| momentum_5m_0.00pct | 3388 | 51.2 | 51.7 | $-1623.75 | -4.8% | $-623.75 | -2.9 | done | losing for real |
| always_up | 3388 | 46.8 | 49.5 | $-3348.82 | -9.9% | $-2348.82 | -5.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5329 | 48.2 | 49.0 | $-3122.25 |
| ETH | 5825 | 48.0 | 48.5 | $-3967.61 |
| SOL | 6102 | 48.2 | 48.5 | $-3656.58 |
| XRP | 6144 | 48.4 | 48.5 | $-3315.94 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
