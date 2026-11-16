# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 16, 10:05 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 536 windows, 14815 settled trades, 75 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1266 | 51.6 | 49.8 | $-111.48 | -0.9% | $888.52 | -0.3 | done | can't tell from luck |
| value_ev20 | 281 | 34.5 | 35.5 | $-222.64 | -7.9% | $777.36 | -1.0 | done | can't tell from luck |
| trend_filter | 867 | 50.4 | 50.8 | $-445.28 | -5.1% | $554.72 | -1.5 | done | can't tell from luck |
| momentum_15m_0.10pct | 1501 | 50.1 | 49.8 | $-536.03 | -3.6% | $463.97 | -1.4 | done | can't tell from luck |
| value_ev10 | 692 | 37.9 | 39.7 | $-600.63 | -8.7% | $399.37 | -1.9 | done | can't tell from luck |
| value_ev5 | 1033 | 40.0 | 41.5 | $-786.07 | -7.6% | $213.93 | -2.1 | done | losing for real |
| reversal_15m_0.10pct | 1501 | 49.9 | 51.3 | $-1109.34 | -7.4% | $-109.34 | -2.9 | done | losing for real |
| coinflip | 2136 | 49.9 | 50.6 | $-1197.66 | -5.6% | $-197.66 | -2.6 | done | losing for real |
| reversal_60m_0.30pct | 1266 | 48.4 | 51.3 | $-1287.51 | -10.2% | $-287.51 | -3.7 | done | losing for real |
| momentum_5m_0.00pct | 2136 | 50.0 | 51.7 | $-1539.96 | -7.2% | $-539.96 | -3.5 | done | losing for real |
| always_up | 2136 | 46.6 | 50.1 | $-2414.63 | -11.3% | $-1414.63 | -5.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3358 | 47.5 | 49.3 | $-2675.14 |
| ETH | 3694 | 48.1 | 48.7 | $-2429.17 |
| SOL | 3863 | 47.7 | 48.9 | $-2871.82 |
| XRP | 3900 | 48.4 | 48.8 | $-2275.09 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
