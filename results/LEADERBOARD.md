# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 24, 1:15 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1269 windows, 34188 settled trades, 417 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 667 | 34.2 | 35.3 | $-511.06 | -7.7% | $488.94 | -1.5 | done | can't tell from luck |
| value_ev10 | 1638 | 38.6 | 39.2 | $-846.12 | -5.2% | $153.88 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 3427 | 50.7 | 50.2 | $-1200.75 | -3.5% | $-200.75 | -2.1 | done | losing for real |
| value_ev5 | 2478 | 40.4 | 41.1 | $-1289.09 | -5.2% | $-289.09 | -2.2 | done | losing for real |
| momentum_60m_0.30pct | 2871 | 49.5 | 49.4 | $-1324.67 | -4.6% | $-324.67 | -2.5 | done | losing for real |
| trend_filter | 2025 | 49.0 | 50.4 | $-1618.74 | -8.0% | $-618.74 | -3.7 | done | losing for real |
| reversal_60m_0.30pct | 2871 | 50.5 | 51.0 | $-1650.57 | -5.7% | $-650.57 | -3.2 | done | losing for real |
| momentum_15m_0.10pct | 3427 | 49.3 | 50.2 | $-2036.54 | -5.9% | $-1036.54 | -3.5 | done | losing for real |
| coinflip | 4928 | 50.0 | 50.1 | $-2235.53 | -4.5% | $-1235.53 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 4928 | 50.4 | 51.4 | $-2795.64 | -5.7% | $-1795.64 | -4.1 | done | losing for real |
| always_up | 4928 | 47.9 | 49.4 | $-3580.46 | -7.3% | $-2580.46 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 8116 | 48.0 | 48.9 | $-4745.43 |
| ETH | 8762 | 48.2 | 48.3 | $-4759.50 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
