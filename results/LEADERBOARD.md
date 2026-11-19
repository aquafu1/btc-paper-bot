# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 19, 11:05 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 828 windows, 22750 settled trades, 56 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 422 | 33.2 | 34.9 | $-390.80 | -9.3% | $609.20 | -1.4 | done | can't tell from luck |
| value_ev10 | 1042 | 37.4 | 39.1 | $-823.78 | -7.9% | $176.22 | -2.1 | done | losing for real |
| reversal_15m_0.10pct | 2318 | 50.9 | 50.6 | $-834.72 | -3.6% | $165.28 | -1.7 | done | can't tell from luck |
| momentum_60m_0.30pct | 1910 | 49.9 | 49.6 | $-843.01 | -4.4% | $156.99 | -1.9 | done | can't tell from luck |
| trend_filter | 1341 | 49.7 | 50.8 | $-964.10 | -7.2% | $35.90 | -2.7 | done | losing for real |
| value_ev5 | 1577 | 39.8 | 41.0 | $-1077.21 | -6.8% | $-77.21 | -2.3 | done | losing for real |
| reversal_60m_0.30pct | 1910 | 50.1 | 51.1 | $-1348.43 | -7.1% | $-348.43 | -3.2 | done | losing for real |
| coinflip | 3304 | 50.2 | 50.3 | $-1454.63 | -4.4% | $-454.63 | -2.6 | done | losing for real |
| momentum_15m_0.10pct | 2318 | 49.1 | 50.3 | $-1456.81 | -6.3% | $-456.81 | -3.0 | done | losing for real |
| momentum_5m_0.00pct | 3304 | 51.2 | 51.6 | $-1578.75 | -4.8% | $-578.75 | -2.8 | done | losing for real |
| always_up | 3304 | 47.4 | 49.6 | $-2911.88 | -8.8% | $-1911.88 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5165 | 48.2 | 49.1 | $-3199.02 |
| ETH | 5662 | 48.0 | 48.5 | $-3836.96 |
| SOL | 5936 | 48.2 | 48.6 | $-3433.21 |
| XRP | 5987 | 48.4 | 48.5 | $-3214.92 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
