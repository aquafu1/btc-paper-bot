# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 19, 9:20 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 821 windows, 22545 settled trades, 39 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 416 | 33.7 | 35.0 | $-330.80 | -8.0% | $669.20 | -1.2 | done | can't tell from luck |
| value_ev10 | 1030 | 37.8 | 39.2 | $-726.63 | -7.1% | $273.37 | -1.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 1886 | 49.9 | 49.6 | $-804.97 | -4.3% | $195.03 | -1.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 2302 | 50.9 | 50.6 | $-844.12 | -3.7% | $155.88 | -1.8 | done | can't tell from luck |
| trend_filter | 1326 | 49.8 | 50.8 | $-912.36 | -6.9% | $87.64 | -2.6 | done | losing for real |
| value_ev5 | 1560 | 40.0 | 41.1 | $-970.83 | -6.2% | $29.17 | -2.1 | done | losing for real |
| reversal_60m_0.30pct | 1886 | 50.1 | 51.2 | $-1299.17 | -6.9% | $-299.17 | -3.1 | done | losing for real |
| momentum_15m_0.10pct | 2302 | 49.1 | 50.2 | $-1402.67 | -6.1% | $-402.67 | -2.9 | done | losing for real |
| momentum_5m_0.00pct | 3279 | 51.2 | 51.6 | $-1496.05 | -4.6% | $-496.05 | -2.7 | done | losing for real |
| coinflip | 3279 | 50.0 | 50.3 | $-1515.00 | -4.6% | $-515.00 | -2.7 | done | losing for real |
| always_up | 3279 | 47.5 | 49.7 | $-2852.61 | -8.7% | $-1852.61 | -5.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5109 | 48.2 | 49.1 | $-3099.63 |
| ETH | 5613 | 48.1 | 48.5 | $-3726.03 |
| SOL | 5884 | 48.3 | 48.6 | $-3263.63 |
| XRP | 5939 | 48.5 | 48.5 | $-3065.94 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
