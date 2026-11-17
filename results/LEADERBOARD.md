# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 16, 7:35 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 574 windows, 15902 settled trades, 35 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1354 | 51.3 | 49.7 | $-208.07 | -1.5% | $791.93 | -0.6 | done | can't tell from luck |
| value_ev20 | 309 | 33.3 | 35.2 | $-327.95 | -10.6% | $672.05 | -1.4 | done | can't tell from luck |
| trend_filter | 922 | 50.8 | 51.1 | $-454.64 | -4.9% | $545.36 | -1.5 | done | can't tell from luck |
| value_ev10 | 748 | 37.6 | 39.4 | $-691.32 | -9.2% | $308.68 | -2.1 | done | losing for real |
| reversal_15m_0.10pct | 1613 | 50.9 | 51.1 | $-799.66 | -5.0% | $200.34 | -2.0 | done | losing for real |
| value_ev5 | 1119 | 39.9 | 41.3 | $-845.56 | -7.6% | $154.44 | -2.2 | done | losing for real |
| momentum_15m_0.10pct | 1613 | 49.1 | 49.9 | $-926.94 | -5.7% | $73.06 | -2.3 | done | losing for real |
| coinflip | 2290 | 49.9 | 50.5 | $-1228.58 | -5.4% | $-228.58 | -2.6 | done | losing for real |
| reversal_60m_0.30pct | 1354 | 48.7 | 51.2 | $-1343.84 | -9.9% | $-343.84 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 2290 | 50.4 | 51.9 | $-1533.63 | -6.7% | $-533.63 | -3.3 | done | losing for real |
| always_up | 2290 | 47.1 | 49.9 | $-2266.30 | -9.9% | $-1266.30 | -4.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3602 | 47.8 | 49.3 | $-2682.92 |
| ETH | 3966 | 48.0 | 48.6 | $-2678.66 |
| SOL | 4139 | 47.8 | 48.7 | $-3054.39 |
| XRP | 4195 | 48.6 | 48.6 | $-2210.51 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
