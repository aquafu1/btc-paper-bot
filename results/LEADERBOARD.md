# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 26, 9:15 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1541 windows, 37971 settled trades, 414 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 781 | 34.1 | 35.3 | $-666.25 | -8.5% | $333.75 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 3765 | 50.9 | 50.0 | $-1016.82 | -2.7% | $-16.82 | -1.7 | done | can't tell from luck |
| value_ev10 | 1865 | 38.3 | 39.1 | $-1077.26 | -5.8% | $-77.26 | -2.0 | done | losing for real |
| value_ev5 | 2809 | 40.4 | 41.1 | $-1470.91 | -5.2% | $-470.91 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 3162 | 51.0 | 51.0 | $-1507.71 | -4.8% | $-507.71 | -2.7 | done | losing for real |
| momentum_60m_0.30pct | 3162 | 49.0 | 49.2 | $-1684.30 | -5.3% | $-684.30 | -3.0 | done | losing for real |
| trend_filter | 2246 | 48.6 | 50.3 | $-1921.41 | -8.6% | $-921.41 | -4.1 | done | losing for real |
| momentum_15m_0.10pct | 3765 | 49.1 | 50.2 | $-2319.63 | -6.2% | $-1319.63 | -3.8 | done | losing for real |
| coinflip | 5472 | 49.9 | 50.0 | $-2456.45 | -4.5% | $-1456.45 | -3.3 | done | losing for real |
| momentum_5m_0.00pct | 5472 | 50.2 | 51.3 | $-3404.36 | -6.2% | $-2404.36 | -4.7 | done | losing for real |
| always_up | 5472 | 48.1 | 49.2 | $-3552.45 | -6.5% | $-2552.45 | -4.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 9947 | 47.9 | 48.7 | $-5809.14 |
| ETH | 10714 | 48.0 | 47.8 | $-5684.17 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
