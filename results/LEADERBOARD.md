# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 26, 11:20 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1549 windows, 38081 settled trades, 395 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 784 | 34.1 | 35.3 | $-673.27 | -8.6% | $326.73 | -1.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 3775 | 50.9 | 50.0 | $-976.02 | -2.6% | $23.98 | -1.6 | done | can't tell from luck |
| value_ev10 | 1874 | 38.3 | 39.1 | $-1093.92 | -5.8% | $-93.92 | -2.1 | done | losing for real |
| value_ev5 | 2819 | 40.4 | 41.1 | $-1497.57 | -5.3% | $-497.57 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 3168 | 51.0 | 51.0 | $-1534.76 | -4.8% | $-534.76 | -2.8 | done | losing for real |
| momentum_60m_0.30pct | 3168 | 49.0 | 49.2 | $-1669.28 | -5.3% | $-669.28 | -3.0 | done | losing for real |
| trend_filter | 2248 | 48.6 | 50.3 | $-1927.37 | -8.6% | $-927.37 | -4.2 | done | losing for real |
| momentum_15m_0.10pct | 3775 | 49.1 | 50.2 | $-2375.64 | -6.3% | $-1375.64 | -3.9 | done | losing for real |
| coinflip | 5490 | 49.9 | 49.9 | $-2477.58 | -4.5% | $-1477.58 | -3.4 | done | losing for real |
| momentum_5m_0.00pct | 5490 | 50.2 | 51.3 | $-3412.89 | -6.2% | $-2412.89 | -4.7 | done | losing for real |
| always_up | 5490 | 48.1 | 49.2 | $-3578.04 | -6.5% | $-2578.04 | -4.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 9998 | 47.9 | 48.7 | $-5802.48 |
| ETH | 10773 | 48.0 | 47.8 | $-5829.61 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
