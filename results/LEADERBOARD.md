# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 25, 3:45 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1423 windows, 36415 settled trades, 463 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 730 | 34.8 | 35.3 | $-465.63 | -6.4% | $534.37 | -1.3 | done | can't tell from luck |
| value_ev10 | 1765 | 38.9 | 39.2 | $-747.88 | -4.2% | $252.12 | -1.4 | done | can't tell from luck |
| reversal_15m_0.10pct | 3637 | 50.8 | 50.1 | $-1028.56 | -2.8% | $-28.56 | -1.7 | done | can't tell from luck |
| value_ev5 | 2665 | 40.7 | 41.1 | $-1212.32 | -4.5% | $-212.32 | -2.0 | done | can't tell from luck |
| momentum_60m_0.30pct | 3056 | 49.3 | 49.3 | $-1468.56 | -4.8% | $-468.56 | -2.6 | done | losing for real |
| reversal_60m_0.30pct | 3056 | 50.7 | 50.9 | $-1586.99 | -5.2% | $-586.99 | -2.9 | done | losing for real |
| trend_filter | 2161 | 48.6 | 50.3 | $-1873.07 | -8.7% | $-873.07 | -4.1 | done | losing for real |
| coinflip | 5236 | 50.1 | 50.0 | $-2209.94 | -4.2% | $-1209.94 | -3.1 | done | losing for real |
| momentum_15m_0.10pct | 3637 | 49.2 | 50.2 | $-2227.09 | -6.1% | $-1227.09 | -3.7 | done | losing for real |
| momentum_5m_0.00pct | 5236 | 50.2 | 51.3 | $-3242.85 | -6.2% | $-2242.85 | -4.6 | done | losing for real |
| always_up | 5236 | 48.0 | 49.3 | $-3611.88 | -6.9% | $-2611.88 | -5.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 9207 | 48.1 | 48.8 | $-4879.75 |
| ETH | 9898 | 48.1 | 48.0 | $-5210.78 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
