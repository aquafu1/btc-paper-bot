# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 17, 3:15 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 605 windows, 16707 settled trades, 67 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1411 | 51.1 | 49.6 | $-226.19 | -1.6% | $773.81 | -0.6 | done | can't tell from luck |
| value_ev20 | 326 | 34.4 | 35.2 | $-234.70 | -7.2% | $765.30 | -1.0 | done | can't tell from luck |
| value_ev10 | 779 | 38.1 | 39.3 | $-560.78 | -7.2% | $439.22 | -1.7 | done | can't tell from luck |
| trend_filter | 962 | 50.1 | 51.0 | $-576.82 | -6.0% | $423.18 | -1.9 | done | can't tell from luck |
| value_ev5 | 1170 | 40.4 | 41.2 | $-691.30 | -5.9% | $308.70 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 1706 | 50.8 | 50.9 | $-792.00 | -4.6% | $208.00 | -1.9 | done | can't tell from luck |
| momentum_15m_0.10pct | 1706 | 49.2 | 50.0 | $-963.14 | -5.6% | $36.86 | -2.3 | done | losing for real |
| coinflip | 2412 | 50.0 | 50.5 | $-1194.17 | -5.0% | $-194.17 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 1411 | 48.9 | 51.3 | $-1317.97 | -9.3% | $-317.97 | -3.6 | done | losing for real |
| momentum_5m_0.00pct | 2412 | 50.2 | 51.8 | $-1620.55 | -6.7% | $-620.55 | -3.4 | done | losing for real |
| always_up | 2412 | 47.1 | 49.8 | $-2300.25 | -9.5% | $-1300.25 | -4.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3798 | 48.0 | 49.2 | $-2531.96 |
| ETH | 4165 | 47.9 | 48.6 | $-2760.92 |
| SOL | 4345 | 47.9 | 48.7 | $-2934.47 |
| XRP | 4399 | 48.5 | 48.6 | $-2250.51 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
