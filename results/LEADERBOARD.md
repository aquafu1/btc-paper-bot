# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 26, 10:20 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1497 windows, 37398 settled trades, 373 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 758 | 34.3 | 35.4 | $-583.02 | -7.7% | $416.98 | -1.6 | done | can't tell from luck |
| value_ev10 | 1821 | 38.4 | 39.2 | $-984.96 | -5.4% | $15.04 | -1.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 3720 | 50.8 | 50.1 | $-1048.57 | -2.8% | $-48.57 | -1.7 | done | can't tell from luck |
| value_ev5 | 2751 | 40.5 | 41.1 | $-1372.83 | -5.0% | $-372.83 | -2.2 | done | losing for real |
| reversal_60m_0.30pct | 3127 | 51.0 | 51.0 | $-1449.63 | -4.6% | $-449.63 | -2.7 | done | losing for real |
| momentum_60m_0.30pct | 3127 | 49.0 | 49.2 | $-1677.92 | -5.4% | $-677.92 | -3.0 | done | losing for real |
| trend_filter | 2219 | 48.6 | 50.3 | $-1909.82 | -8.6% | $-909.82 | -4.1 | done | losing for real |
| momentum_15m_0.10pct | 3720 | 49.2 | 50.2 | $-2220.51 | -6.0% | $-1220.51 | -3.7 | done | losing for real |
| coinflip | 5385 | 50.0 | 50.0 | $-2358.87 | -4.4% | $-1358.87 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 5385 | 50.2 | 51.3 | $-3298.50 | -6.1% | $-2298.50 | -4.6 | done | losing for real |
| always_up | 5385 | 48.0 | 49.2 | $-3584.45 | -6.7% | $-2584.45 | -4.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 9677 | 48.0 | 48.7 | $-5302.74 |
| ETH | 10411 | 48.0 | 47.9 | $-5602.11 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
