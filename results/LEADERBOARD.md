# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 25, 10:20 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1401 windows, 36117 settled trades, 391 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 726 | 34.8 | 35.3 | $-452.49 | -6.2% | $547.51 | -1.3 | done | can't tell from luck |
| value_ev10 | 1751 | 38.9 | 39.2 | $-727.28 | -4.2% | $272.72 | -1.4 | done | can't tell from luck |
| reversal_15m_0.10pct | 3609 | 50.8 | 50.1 | $-1031.50 | -2.9% | $-31.50 | -1.7 | done | can't tell from luck |
| value_ev5 | 2640 | 40.7 | 41.1 | $-1196.14 | -4.5% | $-196.14 | -2.0 | done | can't tell from luck |
| momentum_60m_0.30pct | 3029 | 49.3 | 49.3 | $-1433.57 | -4.7% | $-433.57 | -2.6 | done | losing for real |
| reversal_60m_0.30pct | 3029 | 50.7 | 51.0 | $-1587.67 | -5.2% | $-587.67 | -3.0 | done | losing for real |
| trend_filter | 2145 | 48.5 | 50.4 | $-1891.37 | -8.8% | $-891.37 | -4.2 | done | losing for real |
| momentum_15m_0.10pct | 3609 | 49.2 | 50.2 | $-2203.94 | -6.1% | $-1203.94 | -3.7 | done | losing for real |
| coinflip | 5193 | 50.0 | 50.0 | $-2214.82 | -4.3% | $-1214.82 | -3.1 | done | losing for real |
| momentum_5m_0.00pct | 5193 | 50.1 | 51.4 | $-3241.95 | -6.2% | $-2241.95 | -4.6 | done | losing for real |
| always_up | 5193 | 47.9 | 49.3 | $-3659.96 | -7.0% | $-2659.96 | -5.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 9056 | 48.1 | 48.8 | $-4889.01 |
| ETH | 9751 | 48.1 | 48.1 | $-5167.46 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
