# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 23, 1:30 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1222 windows, 33486 settled trades, 430 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 652 | 34.5 | 35.3 | $-443.45 | -6.8% | $556.55 | -1.3 | done | can't tell from luck |
| value_ev10 | 1600 | 38.8 | 39.2 | $-746.99 | -4.7% | $253.01 | -1.5 | done | can't tell from luck |
| reversal_15m_0.10pct | 3356 | 50.8 | 50.3 | $-1094.31 | -3.3% | $-94.31 | -1.9 | done | can't tell from luck |
| value_ev5 | 2418 | 40.6 | 41.1 | $-1162.22 | -4.8% | $-162.22 | -2.0 | done | losing for real |
| momentum_60m_0.30pct | 2810 | 49.5 | 49.4 | $-1276.88 | -4.5% | $-276.88 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 2810 | 50.5 | 51.0 | $-1665.91 | -5.9% | $-665.91 | -3.2 | done | losing for real |
| trend_filter | 1982 | 48.7 | 50.4 | $-1677.09 | -8.5% | $-677.09 | -3.9 | done | losing for real |
| momentum_15m_0.10pct | 3356 | 49.2 | 50.2 | $-2053.84 | -6.1% | $-1053.84 | -3.6 | done | losing for real |
| coinflip | 4834 | 50.0 | 50.1 | $-2210.17 | -4.6% | $-1210.17 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 4834 | 50.2 | 51.4 | $-2947.50 | -6.1% | $-1947.50 | -4.4 | done | losing for real |
| always_up | 4834 | 47.9 | 49.3 | $-3507.24 | -7.3% | $-2507.24 | -5.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7782 | 48.1 | 48.9 | $-4325.31 |
| ETH | 8394 | 48.1 | 48.3 | $-4876.06 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
