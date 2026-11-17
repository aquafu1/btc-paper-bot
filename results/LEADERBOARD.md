# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 17, 1:15 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 645 windows, 17825 settled trades, 55 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 334 | 34.1 | 35.3 | $-256.80 | -7.7% | $743.20 | -1.1 | done | can't tell from luck |
| momentum_60m_0.30pct | 1504 | 50.8 | 49.6 | $-283.57 | -1.9% | $716.43 | -0.7 | done | can't tell from luck |
| trend_filter | 1030 | 50.2 | 50.8 | $-568.76 | -5.5% | $431.24 | -1.8 | done | can't tell from luck |
| value_ev10 | 822 | 38.3 | 39.5 | $-584.07 | -7.1% | $415.93 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 1836 | 51.5 | 51.0 | $-598.09 | -3.3% | $401.91 | -1.4 | done | can't tell from luck |
| value_ev5 | 1243 | 40.8 | 41.4 | $-679.18 | -5.5% | $320.82 | -1.6 | done | can't tell from luck |
| coinflip | 2572 | 50.2 | 50.5 | $-1153.28 | -4.5% | $-153.28 | -2.3 | done | losing for real |
| momentum_15m_0.10pct | 1836 | 48.5 | 50.0 | $-1240.30 | -6.8% | $-240.30 | -2.9 | done | losing for real |
| reversal_60m_0.30pct | 1504 | 49.2 | 51.4 | $-1313.37 | -8.7% | $-313.37 | -3.5 | done | losing for real |
| momentum_5m_0.00pct | 2572 | 50.6 | 51.7 | $-1448.47 | -5.6% | $-448.47 | -3.0 | done | losing for real |
| always_up | 2572 | 47.3 | 49.7 | $-2269.71 | -8.8% | $-1269.71 | -4.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4047 | 48.3 | 49.3 | $-2430.10 |
| ETH | 4456 | 48.2 | 48.7 | $-2702.26 |
| SOL | 4629 | 48.0 | 48.8 | $-2933.78 |
| XRP | 4693 | 48.5 | 48.5 | $-2329.46 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
