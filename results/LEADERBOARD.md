# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 27, 12:15 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1601 windows, 38766 settled trades, 399 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 817 | 34.4 | 35.1 | $-605.00 | -7.4% | $395.00 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 3826 | 50.9 | 50.0 | $-954.88 | -2.5% | $45.12 | -1.5 | done | can't tell from luck |
| value_ev10 | 1932 | 38.4 | 39.0 | $-1045.86 | -5.4% | $-45.86 | -1.9 | done | can't tell from luck |
| reversal_60m_0.30pct | 3206 | 51.1 | 50.9 | $-1462.17 | -4.6% | $-462.17 | -2.6 | done | losing for real |
| value_ev5 | 2896 | 40.4 | 41.0 | $-1473.33 | -5.1% | $-473.33 | -2.3 | done | losing for real |
| momentum_60m_0.30pct | 3206 | 48.9 | 49.2 | $-1749.87 | -5.5% | $-749.87 | -3.1 | done | losing for real |
| trend_filter | 2281 | 48.4 | 50.4 | $-2050.99 | -9.0% | $-1050.99 | -4.4 | done | losing for real |
| coinflip | 5592 | 50.0 | 49.9 | $-2355.05 | -4.2% | $-1355.05 | -3.2 | done | losing for real |
| momentum_15m_0.10pct | 3826 | 49.1 | 50.2 | $-2402.09 | -6.3% | $-1402.09 | -3.9 | done | losing for real |
| momentum_5m_0.00pct | 5592 | 50.1 | 51.3 | $-3536.40 | -6.3% | $-2536.40 | -4.9 | done | losing for real |
| always_up | 5592 | 48.2 | 49.1 | $-3575.64 | -6.4% | $-2575.64 | -4.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 10315 | 47.9 | 48.6 | $-5877.02 |
| ETH | 11141 | 48.0 | 47.7 | $-5750.02 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
