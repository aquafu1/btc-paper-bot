# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 18, 6:00 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 712 windows, 19636 settled trades, 46 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 376 | 33.8 | 34.8 | $-284.03 | -7.6% | $715.97 | -1.1 | done | can't tell from luck |
| reversal_15m_0.10pct | 2012 | 51.6 | 50.8 | $-503.48 | -2.5% | $496.52 | -1.1 | done | can't tell from luck |
| momentum_60m_0.30pct | 1651 | 50.2 | 49.5 | $-528.38 | -3.2% | $471.62 | -1.3 | done | can't tell from luck |
| value_ev10 | 906 | 38.2 | 39.0 | $-552.57 | -6.1% | $447.43 | -1.5 | done | can't tell from luck |
| value_ev5 | 1363 | 40.8 | 41.0 | $-615.69 | -4.5% | $384.31 | -1.4 | done | can't tell from luck |
| trend_filter | 1145 | 50.4 | 51.0 | $-630.05 | -5.5% | $369.95 | -1.9 | done | can't tell from luck |
| coinflip | 2840 | 50.3 | 50.3 | $-1167.89 | -4.1% | $-167.89 | -2.2 | done | losing for real |
| reversal_60m_0.30pct | 1651 | 49.8 | 51.3 | $-1249.69 | -7.6% | $-249.69 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 2840 | 51.1 | 51.8 | $-1404.79 | -4.9% | $-404.79 | -2.7 | done | losing for real |
| momentum_15m_0.10pct | 2012 | 48.4 | 50.0 | $-1438.15 | -7.1% | $-438.15 | -3.2 | done | losing for real |
| always_up | 2840 | 47.3 | 49.5 | $-2438.72 | -8.6% | $-1438.72 | -4.6 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4453 | 48.2 | 49.0 | $-2684.91 |
| ETH | 4885 | 48.4 | 48.5 | $-2765.11 |
| SOL | 5123 | 48.2 | 48.7 | $-2912.19 |
| XRP | 5175 | 48.6 | 48.4 | $-2451.23 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
