# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 18, 11:45 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 783 windows, 21601 settled trades, 33 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 404 | 32.9 | 34.9 | $-391.45 | -9.7% | $608.55 | -1.5 | done | can't tell from luck |
| momentum_60m_0.30pct | 1832 | 50.1 | 49.6 | $-695.86 | -3.8% | $304.14 | -1.6 | done | can't tell from luck |
| trend_filter | 1271 | 50.3 | 50.8 | $-737.72 | -5.8% | $262.28 | -2.1 | done | losing for real |
| reversal_15m_0.10pct | 2208 | 51.0 | 50.6 | $-756.11 | -3.4% | $243.89 | -1.6 | done | can't tell from luck |
| value_ev10 | 984 | 37.3 | 39.1 | $-794.62 | -8.1% | $205.38 | -2.1 | done | losing for real |
| value_ev5 | 1490 | 39.7 | 41.0 | $-1012.95 | -6.8% | $-12.95 | -2.2 | done | losing for real |
| reversal_60m_0.30pct | 1832 | 49.9 | 51.2 | $-1321.10 | -7.2% | $-321.10 | -3.2 | done | losing for real |
| coinflip | 3124 | 50.2 | 50.3 | $-1338.51 | -4.3% | $-338.51 | -2.4 | done | losing for real |
| momentum_15m_0.10pct | 2208 | 49.0 | 50.2 | $-1403.42 | -6.4% | $-403.42 | -3.0 | done | losing for real |
| momentum_5m_0.00pct | 3124 | 51.2 | 51.7 | $-1459.73 | -4.7% | $-459.73 | -2.7 | done | losing for real |
| always_up | 3124 | 47.3 | 49.5 | $-2736.89 | -8.8% | $-1736.89 | -4.9 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4907 | 48.3 | 49.1 | $-2903.74 |
| ETH | 5392 | 48.0 | 48.5 | $-3636.21 |
| SOL | 5623 | 48.2 | 48.6 | $-3249.67 |
| XRP | 5679 | 48.5 | 48.5 | $-2858.76 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
