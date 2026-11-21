# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 20, 11:45 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 975 windows, 27053 settled trades, 68 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 496 | 34.7 | 34.8 | $-219.50 | -4.4% | $780.50 | -0.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 2763 | 51.2 | 50.5 | $-735.75 | -2.7% | $264.25 | -1.4 | done | can't tell from luck |
| value_ev10 | 1234 | 37.9 | 39.1 | $-748.71 | -6.1% | $251.29 | -1.7 | done | can't tell from luck |
| momentum_60m_0.30pct | 2314 | 50.2 | 49.8 | $-875.34 | -3.8% | $124.66 | -1.8 | done | can't tell from luck |
| value_ev5 | 1872 | 39.9 | 41.0 | $-1097.45 | -5.9% | $-97.45 | -2.1 | done | losing for real |
| trend_filter | 1621 | 49.8 | 50.9 | $-1132.26 | -7.0% | $-132.26 | -2.9 | done | losing for real |
| reversal_60m_0.30pct | 2314 | 49.8 | 50.9 | $-1665.25 | -7.2% | $-665.25 | -3.5 | done | losing for real |
| coinflip | 3892 | 50.1 | 50.3 | $-1831.70 | -4.7% | $-831.70 | -3.0 | done | losing for real |
| momentum_15m_0.10pct | 2763 | 48.8 | 50.3 | $-1964.61 | -7.1% | $-964.61 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 3892 | 50.7 | 51.5 | $-2125.17 | -5.5% | $-1125.17 | -3.5 | done | losing for real |
| always_up | 3892 | 46.8 | 49.6 | $-3887.20 | -10.0% | $-2887.20 | -6.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6165 | 48.2 | 49.1 | $-3533.16 |
| ETH | 6726 | 48.0 | 48.5 | $-4347.79 |
| SOL | 7067 | 48.1 | 48.6 | $-4045.54 |
| XRP | 7095 | 48.2 | 48.4 | $-4356.45 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
