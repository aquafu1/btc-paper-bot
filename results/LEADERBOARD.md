# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 14, 2:45 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 363 windows, 9789 settled trades, 57 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 188 | 37.8 | 36.4 | $+2.39 | +0.1% | $1002.39 | +0.0 | Sat 8:45 PM | too few trades (188/200) |
| value_ev10 | 473 | 40.8 | 40.2 | $-87.57 | -1.9% | $912.43 | -0.3 | done | can't tell from luck |
| value_ev5 | 702 | 42.2 | 42.0 | $-213.89 | -3.0% | $786.11 | -0.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 972 | 51.9 | 52.1 | $-432.20 | -4.4% | $567.80 | -1.5 | done | can't tell from luck |
| reversal_60m_0.30pct | 804 | 51.0 | 52.0 | $-467.12 | -5.8% | $532.88 | -1.7 | done | can't tell from luck |
| trend_filter | 542 | 48.3 | 50.6 | $-475.35 | -8.8% | $524.65 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 804 | 49.0 | 49.8 | $-478.22 | -5.9% | $521.78 | -1.7 | done | can't tell from luck |
| momentum_15m_0.10pct | 972 | 48.1 | 49.6 | $-646.35 | -6.6% | $353.65 | -2.1 | done | losing for real |
| coinflip | 1444 | 50.1 | 50.8 | $-717.66 | -5.0% | $282.34 | -1.9 | done | can't tell from luck |
| momentum_5m_0.00pct | 1444 | 49.5 | 51.6 | $-1076.90 | -7.5% | $-76.90 | -2.9 | done | losing for real |
| always_up | 1444 | 46.0 | 50.7 | $-1847.41 | -12.8% | $-847.41 | -5.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2196 | 47.3 | 49.3 | $-1737.49 |
| ETH | 2462 | 47.7 | 48.8 | $-1744.29 |
| SOL | 2538 | 48.1 | 49.4 | $-1765.46 |
| XRP | 2593 | 48.9 | 49.1 | $-1193.03 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
