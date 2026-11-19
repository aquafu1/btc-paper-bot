# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 19, 3:35 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 798 windows, 21962 settled trades, 40 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 408 | 33.6 | 34.9 | $-322.61 | -7.9% | $677.39 | -1.2 | done | can't tell from luck |
| value_ev10 | 1005 | 37.9 | 39.2 | $-658.72 | -6.6% | $341.28 | -1.7 | done | can't tell from luck |
| momentum_60m_0.30pct | 1851 | 50.2 | 49.6 | $-678.05 | -3.7% | $321.95 | -1.6 | done | can't tell from luck |
| trend_filter | 1287 | 50.3 | 50.8 | $-727.79 | -5.7% | $272.21 | -2.1 | done | losing for real |
| value_ev5 | 1515 | 40.1 | 41.1 | $-864.44 | -5.7% | $135.56 | -1.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 2245 | 50.8 | 50.6 | $-866.93 | -3.9% | $133.07 | -1.8 | done | can't tell from luck |
| momentum_15m_0.10pct | 2245 | 49.2 | 50.2 | $-1290.55 | -5.7% | $-290.55 | -2.7 | done | losing for real |
| coinflip | 3185 | 50.2 | 50.3 | $-1342.79 | -4.2% | $-342.79 | -2.4 | done | losing for real |
| momentum_5m_0.00pct | 3185 | 51.3 | 51.6 | $-1346.48 | -4.2% | $-346.48 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 1851 | 49.8 | 51.2 | $-1364.97 | -7.4% | $-364.97 | -3.2 | done | losing for real |
| always_up | 3185 | 47.5 | 49.6 | $-2682.85 | -8.4% | $-1682.85 | -4.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4992 | 48.4 | 49.1 | $-2749.03 |
| ETH | 5473 | 48.2 | 48.5 | $-3423.23 |
| SOL | 5722 | 48.3 | 48.6 | $-3178.37 |
| XRP | 5775 | 48.5 | 48.5 | $-2795.56 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
