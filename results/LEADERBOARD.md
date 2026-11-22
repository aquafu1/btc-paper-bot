# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 22, 12:20 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1073 windows, 29700 settled trades, 43 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 554 | 34.3 | 35.1 | $-353.30 | -6.4% | $646.70 | -1.1 | done | can't tell from luck |
| reversal_15m_0.10pct | 3010 | 51.3 | 50.5 | $-746.15 | -2.5% | $253.85 | -1.4 | done | can't tell from luck |
| value_ev10 | 1371 | 37.6 | 39.2 | $-999.47 | -7.3% | $0.53 | -2.2 | done | losing for real |
| momentum_60m_0.30pct | 2525 | 49.7 | 49.6 | $-1121.47 | -4.4% | $-121.47 | -2.2 | done | losing for real |
| trend_filter | 1766 | 49.6 | 50.7 | $-1246.23 | -7.1% | $-246.23 | -3.0 | done | losing for real |
| value_ev5 | 2084 | 39.6 | 41.0 | $-1387.46 | -6.7% | $-387.46 | -2.6 | done | losing for real |
| reversal_60m_0.30pct | 2525 | 50.3 | 51.0 | $-1634.83 | -6.5% | $-634.83 | -3.3 | done | losing for real |
| coinflip | 4285 | 50.5 | 50.3 | $-1670.65 | -3.9% | $-670.65 | -2.6 | done | losing for real |
| momentum_5m_0.00pct | 4285 | 51.0 | 51.5 | $-2061.94 | -4.8% | $-1061.94 | -3.3 | done | losing for real |
| momentum_15m_0.10pct | 3010 | 48.7 | 50.3 | $-2158.57 | -7.2% | $-1158.57 | -4.0 | done | losing for real |
| always_up | 4285 | 47.2 | 49.4 | $-3818.44 | -8.9% | $-2818.44 | -5.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6782 | 48.4 | 49.0 | $-3480.81 |
| ETH | 7346 | 48.1 | 48.5 | $-4621.54 |
| SOL | 7745 | 48.1 | 48.5 | $-4502.51 |
| XRP | 7827 | 48.3 | 48.3 | $-4593.65 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
