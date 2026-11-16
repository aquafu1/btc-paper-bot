# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 15, 8:15 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 481 windows, 13198 settled trades, 60 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 241 | 35.3 | 35.9 | $-112.29 | -4.7% | $887.71 | -0.5 | done | can't tell from luck |
| momentum_60m_0.30pct | 1118 | 51.1 | 49.8 | $-158.99 | -1.4% | $841.01 | -0.5 | done | can't tell from luck |
| value_ev10 | 621 | 39.1 | 40.1 | $-332.51 | -5.4% | $667.49 | -1.1 | done | can't tell from luck |
| momentum_15m_0.10pct | 1333 | 50.2 | 50.0 | $-403.55 | -3.0% | $596.45 | -1.1 | done | can't tell from luck |
| value_ev5 | 918 | 41.1 | 41.8 | $-460.05 | -5.0% | $539.95 | -1.3 | done | can't tell from luck |
| trend_filter | 768 | 49.6 | 50.8 | $-479.83 | -6.2% | $520.17 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 1333 | 49.8 | 51.5 | $-956.64 | -7.2% | $43.36 | -2.7 | done | losing for real |
| coinflip | 1916 | 49.9 | 50.8 | $-1016.79 | -5.3% | $-16.79 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 1118 | 48.9 | 51.5 | $-1019.71 | -9.1% | $-19.71 | -3.1 | done | losing for real |
| momentum_5m_0.00pct | 1916 | 49.6 | 51.7 | $-1414.50 | -7.4% | $-414.50 | -3.4 | done | losing for real |
| always_up | 1916 | 46.2 | 50.5 | $-2284.28 | -11.9% | $-1284.28 | -5.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2975 | 47.4 | 49.3 | $-2365.78 |
| ETH | 3307 | 48.1 | 48.8 | $-2086.71 |
| SOL | 3438 | 47.8 | 49.3 | $-2442.54 |
| XRP | 3478 | 48.5 | 49.0 | $-1744.11 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
