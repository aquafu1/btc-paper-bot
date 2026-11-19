# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 19, 2:45 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 843 windows, 23187 settled trades, 74 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 426 | 33.3 | 34.9 | $-371.71 | -8.7% | $628.29 | -1.4 | done | can't tell from luck |
| value_ev10 | 1057 | 37.5 | 39.2 | $-830.95 | -7.9% | $169.05 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 1955 | 50.1 | 49.7 | $-831.64 | -4.3% | $168.36 | -1.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 2368 | 50.8 | 50.6 | $-930.05 | -3.9% | $69.95 | -1.9 | done | can't tell from luck |
| trend_filter | 1364 | 49.9 | 50.8 | $-937.33 | -6.9% | $62.67 | -2.6 | done | losing for real |
| value_ev5 | 1602 | 39.7 | 41.1 | $-1123.49 | -7.0% | $-123.49 | -2.4 | done | losing for real |
| momentum_15m_0.10pct | 2368 | 49.2 | 50.3 | $-1434.24 | -6.1% | $-434.24 | -3.0 | done | losing for real |
| reversal_60m_0.30pct | 1955 | 49.9 | 51.1 | $-1448.25 | -7.4% | $-448.25 | -3.4 | done | losing for real |
| coinflip | 3364 | 50.2 | 50.3 | $-1500.63 | -4.5% | $-500.63 | -2.6 | done | losing for real |
| momentum_5m_0.00pct | 3364 | 51.2 | 51.7 | $-1591.04 | -4.7% | $-591.04 | -2.8 | done | losing for real |
| always_up | 3364 | 47.0 | 49.6 | $-3220.11 | -9.6% | $-2220.11 | -5.6 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5276 | 48.1 | 49.1 | $-3292.22 |
| ETH | 5773 | 48.0 | 48.5 | $-4053.27 |
| SOL | 6047 | 48.2 | 48.6 | $-3555.04 |
| XRP | 6091 | 48.4 | 48.5 | $-3318.91 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
