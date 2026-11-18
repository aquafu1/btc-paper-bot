# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 18, 11:50 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 735 windows, 20282 settled trades, 28 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 383 | 33.4 | 34.9 | $-332.66 | -8.7% | $667.34 | -1.3 | done | can't tell from luck |
| reversal_15m_0.10pct | 2080 | 51.7 | 50.7 | $-446.84 | -2.1% | $553.16 | -1.0 | done | can't tell from luck |
| value_ev10 | 927 | 38.0 | 39.1 | $-616.66 | -6.7% | $383.34 | -1.7 | done | can't tell from luck |
| momentum_60m_0.30pct | 1706 | 50.0 | 49.5 | $-616.90 | -3.6% | $383.10 | -1.5 | done | can't tell from luck |
| value_ev5 | 1399 | 40.5 | 41.1 | $-751.72 | -5.4% | $248.28 | -1.7 | done | can't tell from luck |
| trend_filter | 1193 | 49.9 | 50.9 | $-770.04 | -6.5% | $229.96 | -2.3 | done | losing for real |
| coinflip | 2936 | 50.3 | 50.3 | $-1186.43 | -4.0% | $-186.43 | -2.2 | done | losing for real |
| reversal_60m_0.30pct | 1706 | 50.0 | 51.3 | $-1198.52 | -7.0% | $-198.52 | -3.0 | done | losing for real |
| momentum_15m_0.10pct | 2080 | 48.3 | 50.1 | $-1526.04 | -7.3% | $-526.04 | -3.4 | done | losing for real |
| momentum_5m_0.00pct | 2936 | 50.8 | 51.8 | $-1630.93 | -5.6% | $-630.93 | -3.1 | done | losing for real |
| always_up | 2936 | 47.0 | 49.6 | $-2689.07 | -9.2% | $-1689.07 | -4.9 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4595 | 48.1 | 49.1 | $-2902.95 |
| ETH | 5055 | 48.1 | 48.6 | $-3130.81 |
| SOL | 5281 | 48.1 | 48.7 | $-3082.72 |
| XRP | 5351 | 48.5 | 48.5 | $-2649.33 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
