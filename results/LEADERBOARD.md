# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 19, 2:15 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 793 windows, 21829 settled trades, 45 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 405 | 33.1 | 34.9 | $-372.37 | -9.2% | $627.63 | -1.4 | done | can't tell from luck |
| momentum_60m_0.30pct | 1847 | 50.1 | 49.6 | $-700.47 | -3.8% | $299.53 | -1.6 | done | can't tell from luck |
| trend_filter | 1283 | 50.4 | 50.8 | $-732.70 | -5.7% | $267.30 | -2.1 | done | losing for real |
| value_ev10 | 994 | 37.4 | 39.1 | $-775.87 | -7.8% | $224.13 | -2.0 | done | losing for real |
| reversal_15m_0.10pct | 2229 | 50.8 | 50.6 | $-851.07 | -3.8% | $148.93 | -1.8 | done | can't tell from luck |
| value_ev5 | 1503 | 39.8 | 41.1 | $-1001.35 | -6.7% | $-1.35 | -2.2 | done | losing for real |
| momentum_15m_0.10pct | 2229 | 49.2 | 50.3 | $-1331.54 | -6.0% | $-331.54 | -2.8 | done | losing for real |
| coinflip | 3164 | 50.3 | 50.3 | $-1338.85 | -4.2% | $-338.85 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 1847 | 49.9 | 51.2 | $-1341.44 | -7.3% | $-341.44 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 3164 | 51.4 | 51.7 | $-1362.24 | -4.3% | $-362.24 | -2.5 | done | losing for real |
| always_up | 3164 | 47.5 | 49.6 | $-2672.64 | -8.4% | $-1672.64 | -4.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4958 | 48.3 | 49.1 | $-2938.80 |
| ETH | 5442 | 48.1 | 48.5 | $-3543.90 |
| SOL | 5684 | 48.3 | 48.6 | $-3188.20 |
| XRP | 5745 | 48.6 | 48.5 | $-2809.62 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
