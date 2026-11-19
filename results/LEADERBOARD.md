# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 19, 9:30 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 822 windows, 22554 settled trades, 70 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 416 | 33.7 | 35.0 | $-330.80 | -8.0% | $669.20 | -1.2 | done | can't tell from luck |
| value_ev10 | 1030 | 37.8 | 39.2 | $-726.63 | -7.1% | $273.37 | -1.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 1887 | 49.9 | 49.6 | $-814.97 | -4.3% | $185.03 | -1.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 2303 | 50.9 | 50.7 | $-837.39 | -3.6% | $162.61 | -1.8 | done | can't tell from luck |
| trend_filter | 1327 | 49.7 | 50.8 | $-922.36 | -7.0% | $77.64 | -2.6 | done | losing for real |
| value_ev5 | 1561 | 40.0 | 41.1 | $-980.83 | -6.3% | $19.17 | -2.1 | done | losing for real |
| reversal_60m_0.30pct | 1887 | 50.1 | 51.2 | $-1292.43 | -6.8% | $-292.43 | -3.0 | done | losing for real |
| momentum_15m_0.10pct | 2303 | 49.1 | 50.2 | $-1412.67 | -6.1% | $-412.67 | -3.0 | done | losing for real |
| momentum_5m_0.00pct | 3280 | 51.2 | 51.6 | $-1506.05 | -4.6% | $-506.05 | -2.7 | done | losing for real |
| coinflip | 3280 | 50.1 | 50.3 | $-1508.26 | -4.6% | $-508.26 | -2.7 | done | losing for real |
| always_up | 3280 | 47.5 | 49.7 | $-2845.88 | -8.7% | $-1845.88 | -5.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5118 | 48.1 | 49.1 | $-3122.69 |
| ETH | 5613 | 48.1 | 48.5 | $-3726.03 |
| SOL | 5884 | 48.3 | 48.6 | $-3263.63 |
| XRP | 5939 | 48.5 | 48.5 | $-3065.94 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
