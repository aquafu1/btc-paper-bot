# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 19, 6:20 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 809 windows, 22220 settled trades, 34 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 412 | 33.5 | 35.0 | $-331.28 | -8.0% | $668.72 | -1.2 | done | can't tell from luck |
| value_ev10 | 1016 | 37.8 | 39.2 | $-694.51 | -6.8% | $305.49 | -1.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 1862 | 50.1 | 49.6 | $-736.58 | -4.0% | $263.42 | -1.7 | done | can't tell from luck |
| trend_filter | 1300 | 50.2 | 50.8 | $-791.06 | -6.1% | $208.94 | -2.3 | done | losing for real |
| reversal_15m_0.10pct | 2269 | 50.9 | 50.6 | $-822.42 | -3.6% | $177.58 | -1.7 | done | can't tell from luck |
| value_ev5 | 1537 | 40.0 | 41.1 | $-926.63 | -6.0% | $73.37 | -2.0 | done | can't tell from luck |
| reversal_60m_0.30pct | 1862 | 49.9 | 51.2 | $-1326.70 | -7.1% | $-326.70 | -3.1 | done | losing for real |
| momentum_5m_0.00pct | 3231 | 51.3 | 51.6 | $-1356.68 | -4.2% | $-356.68 | -2.5 | done | losing for real |
| momentum_15m_0.10pct | 2269 | 49.1 | 50.2 | $-1368.55 | -6.0% | $-368.55 | -2.9 | done | losing for real |
| coinflip | 3231 | 50.2 | 50.3 | $-1412.46 | -4.4% | $-412.46 | -2.5 | done | losing for real |
| always_up | 3231 | 47.4 | 49.7 | $-2801.12 | -8.7% | $-1801.12 | -4.9 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5045 | 48.3 | 49.1 | $-2828.24 |
| ETH | 5532 | 48.2 | 48.5 | $-3505.51 |
| SOL | 5792 | 48.2 | 48.6 | $-3284.42 |
| XRP | 5851 | 48.5 | 48.5 | $-2949.81 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
