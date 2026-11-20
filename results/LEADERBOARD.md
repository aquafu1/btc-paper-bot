# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 19, 8:50 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 867 windows, 23911 settled trades, 41 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 448 | 35.0 | 34.9 | $-178.27 | -4.0% | $821.73 | -0.6 | done | can't tell from luck |
| value_ev10 | 1096 | 38.2 | 39.1 | $-627.29 | -5.7% | $372.71 | -1.5 | done | can't tell from luck |
| momentum_60m_0.30pct | 2019 | 50.2 | 49.7 | $-765.96 | -3.8% | $234.04 | -1.7 | done | can't tell from luck |
| trend_filter | 1401 | 50.2 | 50.9 | $-892.42 | -6.4% | $107.58 | -2.5 | done | losing for real |
| reversal_15m_0.10pct | 2441 | 50.6 | 50.5 | $-978.49 | -4.0% | $21.51 | -2.0 | done | can't tell from luck |
| value_ev5 | 1657 | 40.0 | 41.0 | $-979.69 | -5.9% | $20.31 | -2.0 | done | losing for real |
| momentum_15m_0.10pct | 2441 | 49.4 | 50.4 | $-1374.92 | -5.6% | $-374.92 | -2.8 | done | losing for real |
| reversal_60m_0.30pct | 2019 | 49.8 | 51.1 | $-1472.40 | -7.3% | $-472.40 | -3.4 | done | losing for real |
| coinflip | 3463 | 50.1 | 50.3 | $-1559.80 | -4.5% | $-559.80 | -2.7 | done | losing for real |
| momentum_5m_0.00pct | 3463 | 51.3 | 51.7 | $-1576.97 | -4.6% | $-576.97 | -2.8 | done | losing for real |
| always_up | 3463 | 46.9 | 49.6 | $-3372.79 | -9.7% | $-2372.79 | -5.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5455 | 48.3 | 49.1 | $-2972.76 |
| ETH | 5950 | 48.1 | 48.5 | $-3860.38 |
| SOL | 6233 | 48.3 | 48.6 | $-3492.31 |
| XRP | 6273 | 48.3 | 48.5 | $-3453.54 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
