# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 18, 11:30 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 782 windows, 21578 settled trades, 40 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 404 | 32.9 | 34.9 | $-391.45 | -9.7% | $608.55 | -1.5 | done | can't tell from luck |
| momentum_60m_0.30pct | 1832 | 50.1 | 49.6 | $-695.86 | -3.8% | $304.14 | -1.6 | done | can't tell from luck |
| trend_filter | 1271 | 50.3 | 50.8 | $-737.72 | -5.8% | $262.28 | -2.1 | done | losing for real |
| reversal_15m_0.10pct | 2204 | 51.0 | 50.6 | $-776.82 | -3.5% | $223.18 | -1.7 | done | can't tell from luck |
| value_ev10 | 983 | 37.3 | 39.1 | $-784.62 | -8.0% | $215.38 | -2.0 | done | losing for real |
| value_ev5 | 1488 | 39.7 | 41.0 | $-1012.25 | -6.8% | $-12.25 | -2.2 | done | losing for real |
| reversal_60m_0.30pct | 1832 | 49.9 | 51.2 | $-1321.10 | -7.2% | $-321.10 | -3.2 | done | losing for real |
| coinflip | 3120 | 50.2 | 50.3 | $-1355.46 | -4.3% | $-355.46 | -2.4 | done | losing for real |
| momentum_15m_0.10pct | 2204 | 49.0 | 50.2 | $-1380.16 | -6.3% | $-380.16 | -3.0 | done | losing for real |
| momentum_5m_0.00pct | 3120 | 51.2 | 51.6 | $-1436.47 | -4.6% | $-436.47 | -2.7 | done | losing for real |
| always_up | 3120 | 47.3 | 49.5 | $-2757.60 | -8.8% | $-1757.60 | -4.9 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4900 | 48.3 | 49.1 | $-2883.94 |
| ETH | 5387 | 48.0 | 48.5 | $-3627.19 |
| SOL | 5617 | 48.1 | 48.6 | $-3266.87 |
| XRP | 5674 | 48.5 | 48.5 | $-2871.51 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
