# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 19, 10:50 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 827 windows, 22742 settled trades, 34 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 422 | 33.2 | 34.9 | $-390.80 | -9.3% | $609.20 | -1.4 | done | can't tell from luck |
| value_ev10 | 1041 | 37.5 | 39.1 | $-813.78 | -7.8% | $186.22 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 1909 | 50.0 | 49.7 | $-833.01 | -4.4% | $166.99 | -1.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 2318 | 50.9 | 50.6 | $-834.72 | -3.6% | $165.28 | -1.7 | done | can't tell from luck |
| trend_filter | 1340 | 49.8 | 50.8 | $-954.10 | -7.1% | $45.90 | -2.7 | done | losing for real |
| value_ev5 | 1576 | 39.8 | 41.0 | $-1067.21 | -6.8% | $-67.21 | -2.3 | done | losing for real |
| reversal_60m_0.30pct | 1909 | 50.0 | 51.1 | $-1353.01 | -7.1% | $-353.01 | -3.2 | done | losing for real |
| momentum_15m_0.10pct | 2318 | 49.1 | 50.3 | $-1456.81 | -6.3% | $-456.81 | -3.0 | done | losing for real |
| coinflip | 3303 | 50.2 | 50.3 | $-1459.21 | -4.4% | $-459.21 | -2.6 | done | losing for real |
| momentum_5m_0.00pct | 3303 | 51.2 | 51.6 | $-1568.75 | -4.7% | $-568.75 | -2.8 | done | losing for real |
| always_up | 3303 | 47.4 | 49.6 | $-2916.46 | -8.8% | $-1916.46 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5157 | 48.2 | 49.1 | $-3162.76 |
| ETH | 5662 | 48.0 | 48.5 | $-3836.96 |
| SOL | 5936 | 48.2 | 48.6 | $-3433.21 |
| XRP | 5987 | 48.4 | 48.5 | $-3214.92 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
