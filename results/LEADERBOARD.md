# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 23, 2:15 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1177 windows, 32532 settled trades, 59 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 628 | 34.9 | 35.3 | $-355.19 | -5.7% | $644.81 | -1.1 | done | can't tell from luck |
| value_ev10 | 1538 | 38.6 | 39.2 | $-792.98 | -5.2% | $207.02 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 3263 | 50.8 | 50.4 | $-1050.39 | -3.2% | $-50.39 | -1.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 2744 | 49.6 | 49.4 | $-1200.88 | -4.4% | $-200.88 | -2.3 | done | losing for real |
| value_ev5 | 2328 | 40.3 | 41.1 | $-1251.69 | -5.4% | $-251.69 | -2.2 | done | losing for real |
| trend_filter | 1924 | 48.9 | 50.5 | $-1553.80 | -8.1% | $-553.80 | -3.6 | done | losing for real |
| reversal_60m_0.30pct | 2744 | 50.4 | 51.1 | $-1698.32 | -6.2% | $-698.32 | -3.3 | done | losing for real |
| momentum_15m_0.10pct | 3263 | 49.2 | 50.2 | $-1975.04 | -6.1% | $-975.04 | -3.5 | done | losing for real |
| coinflip | 4700 | 50.0 | 50.2 | $-2153.85 | -4.6% | $-1153.85 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 4700 | 50.1 | 51.4 | $-2981.22 | -6.3% | $-1981.22 | -4.5 | done | losing for real |
| always_up | 4700 | 47.8 | 49.3 | $-3468.82 | -7.4% | $-2468.82 | -5.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7463 | 48.2 | 49.0 | $-4015.57 |
| ETH | 8068 | 48.1 | 48.4 | $-4858.98 |
| SOL | 8462 | 48.1 | 48.4 | $-4517.74 |
| XRP | 8539 | 48.1 | 48.2 | $-5089.89 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
