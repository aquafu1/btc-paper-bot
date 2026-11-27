# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 26, 9:00 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1540 windows, 37955 settled trades, 401 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 779 | 34.1 | 35.3 | $-646.25 | -8.3% | $353.75 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 3765 | 50.9 | 50.0 | $-1016.82 | -2.7% | $-16.82 | -1.7 | done | can't tell from luck |
| value_ev10 | 1863 | 38.4 | 39.1 | $-1057.26 | -5.7% | $-57.26 | -2.0 | done | losing for real |
| value_ev5 | 2807 | 40.5 | 41.1 | $-1450.91 | -5.2% | $-450.91 | -2.3 | done | losing for real |
| reversal_60m_0.30pct | 3160 | 51.0 | 51.0 | $-1514.18 | -4.8% | $-514.18 | -2.8 | done | losing for real |
| momentum_60m_0.30pct | 3160 | 49.0 | 49.2 | $-1664.30 | -5.3% | $-664.30 | -2.9 | done | losing for real |
| trend_filter | 2246 | 48.6 | 50.3 | $-1921.41 | -8.6% | $-921.41 | -4.1 | done | losing for real |
| momentum_15m_0.10pct | 3765 | 49.1 | 50.2 | $-2319.63 | -6.2% | $-1319.63 | -3.8 | done | losing for real |
| coinflip | 5470 | 49.9 | 50.0 | $-2436.45 | -4.5% | $-1436.45 | -3.3 | done | losing for real |
| momentum_5m_0.00pct | 5470 | 50.2 | 51.3 | $-3410.83 | -6.2% | $-2410.83 | -4.8 | done | losing for real |
| always_up | 5470 | 48.2 | 49.2 | $-3532.45 | -6.5% | $-2532.45 | -4.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 9939 | 47.9 | 48.7 | $-5756.16 |
| ETH | 10706 | 48.1 | 47.8 | $-5630.09 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
