# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 19, 8:35 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 866 windows, 23867 settled trades, 53 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 446 | 34.8 | 34.9 | $-207.36 | -4.6% | $792.64 | -0.7 | done | can't tell from luck |
| value_ev10 | 1094 | 38.1 | 39.1 | $-656.38 | -6.0% | $343.62 | -1.6 | done | can't tell from luck |
| momentum_60m_0.30pct | 2014 | 50.2 | 49.7 | $-765.06 | -3.8% | $234.94 | -1.7 | done | can't tell from luck |
| trend_filter | 1398 | 50.3 | 50.9 | $-862.42 | -6.2% | $137.58 | -2.4 | done | losing for real |
| reversal_15m_0.10pct | 2436 | 50.6 | 50.5 | $-990.67 | -4.1% | $9.33 | -2.0 | done | losing for real |
| value_ev5 | 1655 | 39.9 | 41.0 | $-1008.78 | -6.1% | $-8.78 | -2.1 | done | losing for real |
| momentum_15m_0.10pct | 2436 | 49.4 | 50.4 | $-1374.01 | -5.6% | $-374.01 | -2.8 | done | losing for real |
| reversal_60m_0.30pct | 2014 | 49.8 | 51.1 | $-1484.58 | -7.4% | $-484.58 | -3.4 | done | losing for real |
| momentum_5m_0.00pct | 3458 | 51.3 | 51.7 | $-1526.97 | -4.4% | $-526.97 | -2.7 | done | losing for real |
| coinflip | 3458 | 50.1 | 50.3 | $-1556.19 | -4.5% | $-556.19 | -2.7 | done | losing for real |
| always_up | 3458 | 46.8 | 49.6 | $-3384.97 | -9.8% | $-2384.97 | -5.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5447 | 48.3 | 49.0 | $-2952.98 |
| ETH | 5942 | 48.1 | 48.5 | $-3867.73 |
| SOL | 6223 | 48.3 | 48.6 | $-3539.59 |
| XRP | 6255 | 48.3 | 48.5 | $-3457.08 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
