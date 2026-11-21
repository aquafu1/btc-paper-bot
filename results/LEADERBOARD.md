# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 20, 11:50 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 975 windows, 27064 settled trades, 57 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 497 | 34.6 | 34.8 | $-229.50 | -4.6% | $770.50 | -0.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 2764 | 51.3 | 50.5 | $-729.15 | -2.6% | $270.85 | -1.4 | done | can't tell from luck |
| value_ev10 | 1235 | 37.9 | 39.1 | $-758.71 | -6.1% | $241.29 | -1.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 2315 | 50.2 | 49.7 | $-885.34 | -3.8% | $114.66 | -1.8 | done | can't tell from luck |
| value_ev5 | 1873 | 39.8 | 41.0 | $-1107.45 | -5.9% | $-107.45 | -2.2 | done | losing for real |
| trend_filter | 1622 | 49.8 | 50.9 | $-1142.26 | -7.0% | $-142.26 | -2.9 | done | losing for real |
| reversal_60m_0.30pct | 2315 | 49.8 | 50.9 | $-1658.65 | -7.2% | $-658.65 | -3.5 | done | losing for real |
| coinflip | 3893 | 50.1 | 50.3 | $-1825.10 | -4.7% | $-825.10 | -3.0 | done | losing for real |
| momentum_15m_0.10pct | 2764 | 48.7 | 50.3 | $-1974.61 | -7.1% | $-974.61 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 3893 | 50.7 | 51.5 | $-2135.17 | -5.5% | $-1135.17 | -3.5 | done | losing for real |
| always_up | 3893 | 46.8 | 49.6 | $-3897.20 | -10.0% | $-2897.20 | -6.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6165 | 48.2 | 49.1 | $-3533.16 |
| ETH | 6737 | 48.0 | 48.5 | $-4407.99 |
| SOL | 7067 | 48.1 | 48.6 | $-4045.54 |
| XRP | 7095 | 48.2 | 48.4 | $-4356.45 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
