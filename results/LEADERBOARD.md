# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 27, 6:15 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1625 windows, 39048 settled trades, 355 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 827 | 34.5 | 35.2 | $-595.19 | -7.2% | $404.81 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 3848 | 50.8 | 50.0 | $-1024.52 | -2.7% | $-24.52 | -1.6 | done | can't tell from luck |
| value_ev10 | 1956 | 38.3 | 39.0 | $-1088.52 | -5.6% | $-88.52 | -2.0 | done | losing for real |
| reversal_60m_0.30pct | 3218 | 51.1 | 50.9 | $-1475.66 | -4.6% | $-475.66 | -2.7 | done | losing for real |
| value_ev5 | 2924 | 40.4 | 41.0 | $-1518.93 | -5.2% | $-518.93 | -2.4 | done | losing for real |
| momentum_60m_0.30pct | 3218 | 48.9 | 49.2 | $-1751.56 | -5.4% | $-751.56 | -3.1 | done | losing for real |
| trend_filter | 2289 | 48.5 | 50.4 | $-2023.76 | -8.8% | $-1023.76 | -4.3 | done | losing for real |
| coinflip | 5640 | 50.1 | 49.9 | $-2328.66 | -4.1% | $-1328.66 | -3.1 | done | losing for real |
| momentum_15m_0.10pct | 3848 | 49.2 | 50.2 | $-2345.19 | -6.1% | $-1345.19 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 5640 | 50.2 | 51.3 | $-3426.10 | -6.1% | $-2426.10 | -4.7 | done | losing for real |
| always_up | 5640 | 48.2 | 49.1 | $-3578.54 | -6.3% | $-2578.54 | -4.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 10435 | 48.0 | 48.6 | $-5821.49 |
| ETH | 11303 | 48.0 | 47.7 | $-5750.92 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
