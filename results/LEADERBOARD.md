# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 26, 7:05 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1484 windows, 37241 settled trades, 350 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 754 | 34.4 | 35.4 | $-573.12 | -7.6% | $426.88 | -1.6 | done | can't tell from luck |
| value_ev10 | 1815 | 38.5 | 39.2 | $-955.06 | -5.3% | $44.94 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 3707 | 50.9 | 50.1 | $-1002.19 | -2.7% | $-2.19 | -1.6 | done | can't tell from luck |
| value_ev5 | 2737 | 40.4 | 41.1 | $-1416.86 | -5.2% | $-416.86 | -2.3 | done | losing for real |
| reversal_60m_0.30pct | 3116 | 51.0 | 51.0 | $-1502.63 | -4.8% | $-502.63 | -2.8 | done | losing for real |
| momentum_60m_0.30pct | 3116 | 49.0 | 49.2 | $-1626.03 | -5.2% | $-626.03 | -2.9 | done | losing for real |
| trend_filter | 2212 | 48.5 | 50.3 | $-1943.15 | -8.8% | $-943.15 | -4.2 | done | losing for real |
| momentum_15m_0.10pct | 3707 | 49.1 | 50.2 | $-2284.40 | -6.2% | $-1284.40 | -3.8 | done | losing for real |
| coinflip | 5359 | 50.0 | 50.0 | $-2376.18 | -4.4% | $-1376.18 | -3.3 | done | losing for real |
| momentum_5m_0.00pct | 5359 | 50.1 | 51.3 | $-3409.18 | -6.4% | $-2409.18 | -4.8 | done | losing for real |
| always_up | 5359 | 48.1 | 49.2 | $-3530.14 | -6.6% | $-2530.14 | -4.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 9602 | 48.0 | 48.7 | $-5263.82 |
| ETH | 10329 | 47.9 | 48.0 | $-5770.90 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
