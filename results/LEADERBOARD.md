# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 19, 11:20 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 829 windows, 22801 settled trades, 42 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 422 | 33.2 | 34.9 | $-390.80 | -9.3% | $609.20 | -1.4 | done | can't tell from luck |
| value_ev10 | 1042 | 37.4 | 39.1 | $-823.78 | -7.9% | $176.22 | -2.1 | done | losing for real |
| reversal_15m_0.10pct | 2325 | 51.0 | 50.6 | $-841.75 | -3.6% | $158.25 | -1.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 1916 | 49.9 | 49.6 | $-846.86 | -4.4% | $153.14 | -1.9 | done | can't tell from luck |
| trend_filter | 1344 | 49.9 | 50.8 | $-937.95 | -7.0% | $62.05 | -2.6 | done | losing for real |
| value_ev5 | 1578 | 39.8 | 41.0 | $-1067.89 | -6.8% | $-67.89 | -2.3 | done | losing for real |
| reversal_60m_0.30pct | 1916 | 50.1 | 51.1 | $-1361.17 | -7.1% | $-361.17 | -3.2 | done | losing for real |
| coinflip | 3311 | 50.3 | 50.3 | $-1405.51 | -4.2% | $-405.51 | -2.5 | done | losing for real |
| momentum_15m_0.10pct | 2325 | 49.0 | 50.2 | $-1470.66 | -6.3% | $-470.66 | -3.1 | done | losing for real |
| momentum_5m_0.00pct | 3311 | 51.3 | 51.6 | $-1529.63 | -4.6% | $-529.63 | -2.7 | done | losing for real |
| always_up | 3311 | 47.3 | 49.6 | $-2981.88 | -9.0% | $-1981.88 | -5.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5180 | 48.2 | 49.1 | $-3195.94 |
| ETH | 5677 | 48.1 | 48.5 | $-3833.11 |
| SOL | 5950 | 48.3 | 48.6 | $-3410.20 |
| XRP | 5994 | 48.4 | 48.5 | $-3218.63 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
