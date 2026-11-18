# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 18, 3:05 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 748 windows, 20644 settled trades, 57 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 389 | 33.7 | 34.9 | $-301.39 | -7.7% | $698.61 | -1.2 | done | can't tell from luck |
| reversal_15m_0.10pct | 2112 | 51.6 | 50.6 | $-461.19 | -2.2% | $538.81 | -1.0 | done | can't tell from luck |
| momentum_60m_0.30pct | 1746 | 50.1 | 49.6 | $-615.37 | -3.5% | $384.63 | -1.5 | done | can't tell from luck |
| value_ev10 | 946 | 37.8 | 39.1 | $-639.74 | -6.8% | $360.26 | -1.7 | done | can't tell from luck |
| trend_filter | 1216 | 49.9 | 50.9 | $-782.88 | -6.4% | $217.12 | -2.3 | done | losing for real |
| value_ev5 | 1425 | 40.3 | 41.1 | $-802.97 | -5.6% | $197.03 | -1.8 | done | can't tell from luck |
| coinflip | 2984 | 50.3 | 50.3 | $-1176.41 | -3.9% | $-176.41 | -2.2 | done | losing for real |
| reversal_60m_0.30pct | 1746 | 49.9 | 51.2 | $-1254.36 | -7.2% | $-254.36 | -3.1 | done | losing for real |
| momentum_15m_0.10pct | 2112 | 48.4 | 50.2 | $-1575.99 | -7.5% | $-575.99 | -3.5 | done | losing for real |
| momentum_5m_0.00pct | 2984 | 50.8 | 51.8 | $-1658.90 | -5.6% | $-658.90 | -3.1 | done | losing for real |
| always_up | 2984 | 46.8 | 49.5 | $-2847.17 | -9.5% | $-1847.17 | -5.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4674 | 48.1 | 49.1 | $-2998.12 |
| ETH | 5144 | 48.1 | 48.5 | $-3316.59 |
| SOL | 5381 | 48.0 | 48.6 | $-3173.06 |
| XRP | 5445 | 48.5 | 48.4 | $-2628.60 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
