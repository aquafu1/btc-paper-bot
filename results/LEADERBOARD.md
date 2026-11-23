# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 23, 10:30 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1210 windows, 33308 settled trades, 249 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 651 | 34.4 | 35.3 | $-458.79 | -7.0% | $541.21 | -1.4 | done | can't tell from luck |
| value_ev10 | 1592 | 38.6 | 39.2 | $-814.81 | -5.1% | $185.19 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 3339 | 50.8 | 50.3 | $-1101.34 | -3.3% | $-101.34 | -1.9 | done | can't tell from luck |
| value_ev5 | 2408 | 40.4 | 41.1 | $-1233.15 | -5.1% | $-233.15 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 2791 | 49.5 | 49.4 | $-1298.89 | -4.7% | $-298.89 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 2791 | 50.5 | 51.1 | $-1646.40 | -5.9% | $-646.40 | -3.2 | done | losing for real |
| trend_filter | 1967 | 48.7 | 50.4 | $-1673.47 | -8.5% | $-673.47 | -3.9 | done | losing for real |
| momentum_15m_0.10pct | 3339 | 49.2 | 50.2 | $-2040.76 | -6.1% | $-1040.76 | -3.6 | done | losing for real |
| coinflip | 4810 | 50.0 | 50.1 | $-2188.80 | -4.6% | $-1188.80 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 4810 | 50.3 | 51.4 | $-2896.83 | -6.0% | $-1896.83 | -4.3 | done | losing for real |
| always_up | 4810 | 47.9 | 49.3 | $-3495.92 | -7.3% | $-2495.92 | -5.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7689 | 48.1 | 48.9 | $-4336.34 |
| ETH | 8309 | 48.1 | 48.3 | $-4928.60 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
