# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 15, 2:20 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 457 windows, 12564 settled trades, 49 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 230 | 34.3 | 35.9 | $-182.39 | -7.9% | $817.61 | -0.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 1070 | 51.1 | 50.0 | $-223.64 | -2.1% | $776.36 | -0.7 | done | can't tell from luck |
| trend_filter | 729 | 50.1 | 50.7 | $-385.98 | -5.3% | $614.02 | -1.5 | done | can't tell from luck |
| value_ev10 | 589 | 38.7 | 40.1 | $-407.06 | -6.9% | $592.94 | -1.4 | done | can't tell from luck |
| momentum_15m_0.10pct | 1267 | 49.9 | 50.0 | $-489.00 | -3.9% | $511.00 | -1.4 | done | can't tell from luck |
| value_ev5 | 873 | 40.8 | 41.8 | $-541.74 | -6.2% | $458.26 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 1267 | 50.1 | 51.6 | $-914.61 | -7.2% | $85.39 | -2.7 | done | losing for real |
| coinflip | 1823 | 49.9 | 50.8 | $-1037.17 | -5.7% | $-37.17 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 1070 | 48.9 | 51.8 | $-1063.00 | -9.9% | $-63.00 | -3.4 | done | losing for real |
| momentum_5m_0.00pct | 1823 | 49.6 | 51.5 | $-1320.67 | -7.2% | $-320.67 | -3.2 | done | losing for real |
| always_up | 1823 | 46.1 | 50.5 | $-2304.70 | -12.6% | $-1304.70 | -5.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2842 | 47.4 | 49.3 | $-2375.24 |
| ETH | 3156 | 48.0 | 48.8 | $-2083.87 |
| SOL | 3264 | 47.7 | 49.3 | $-2507.81 |
| XRP | 3302 | 48.5 | 49.2 | $-1903.03 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
