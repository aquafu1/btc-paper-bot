# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 21, 6:20 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1001 windows, 27824 settled trades, 58 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 514 | 34.2 | 34.9 | $-296.26 | -5.8% | $703.74 | -1.0 | done | can't tell from luck |
| reversal_15m_0.10pct | 2836 | 51.1 | 50.4 | $-861.54 | -3.0% | $138.46 | -1.6 | done | can't tell from luck |
| value_ev10 | 1274 | 37.5 | 39.1 | $-899.88 | -7.1% | $100.12 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 2389 | 49.9 | 49.7 | $-1071.29 | -4.5% | $-71.29 | -2.2 | done | losing for real |
| trend_filter | 1664 | 49.5 | 50.8 | $-1233.42 | -7.4% | $-233.42 | -3.1 | done | losing for real |
| value_ev5 | 1931 | 39.6 | 41.0 | $-1270.53 | -6.6% | $-270.53 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 2389 | 50.1 | 50.9 | $-1584.07 | -6.6% | $-584.07 | -3.3 | done | losing for real |
| coinflip | 3997 | 50.4 | 50.3 | $-1737.00 | -4.3% | $-737.00 | -2.8 | done | losing for real |
| momentum_15m_0.10pct | 2836 | 48.9 | 50.3 | $-1929.30 | -6.8% | $-929.30 | -3.7 | done | losing for real |
| momentum_5m_0.00pct | 3997 | 50.7 | 51.5 | $-2229.97 | -5.6% | $-1229.97 | -3.6 | done | losing for real |
| always_up | 3997 | 47.0 | 49.5 | $-3823.18 | -9.6% | $-2823.18 | -6.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6345 | 48.2 | 49.0 | $-3586.87 |
| ETH | 6911 | 48.0 | 48.5 | $-4563.32 |
| SOL | 7273 | 48.2 | 48.6 | $-4134.90 |
| XRP | 7295 | 48.1 | 48.4 | $-4651.36 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
