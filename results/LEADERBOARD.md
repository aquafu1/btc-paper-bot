# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 18, 6:35 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 762 windows, 21032 settled trades, 36 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 395 | 33.7 | 34.9 | $-301.45 | -7.6% | $698.55 | -1.1 | done | can't tell from luck |
| reversal_15m_0.10pct | 2150 | 51.4 | 50.6 | $-540.14 | -2.5% | $459.86 | -1.2 | done | can't tell from luck |
| value_ev10 | 961 | 37.9 | 39.1 | $-637.58 | -6.6% | $362.42 | -1.7 | done | can't tell from luck |
| momentum_60m_0.30pct | 1780 | 49.9 | 49.6 | $-714.67 | -4.0% | $285.33 | -1.7 | done | can't tell from luck |
| trend_filter | 1238 | 49.8 | 50.9 | $-811.64 | -6.6% | $188.36 | -2.4 | done | losing for real |
| value_ev5 | 1452 | 40.1 | 41.1 | $-876.64 | -6.0% | $123.36 | -1.9 | done | can't tell from luck |
| coinflip | 3042 | 50.4 | 50.3 | $-1168.43 | -3.8% | $-168.43 | -2.1 | done | losing for real |
| reversal_60m_0.30pct | 1780 | 50.1 | 51.2 | $-1215.67 | -6.8% | $-215.67 | -2.9 | done | losing for real |
| momentum_15m_0.10pct | 2150 | 48.6 | 50.2 | $-1562.81 | -7.3% | $-562.81 | -3.4 | done | losing for real |
| momentum_5m_0.00pct | 3042 | 50.9 | 51.7 | $-1624.32 | -5.3% | $-624.32 | -3.0 | done | losing for real |
| always_up | 3042 | 47.0 | 49.6 | $-2893.46 | -9.5% | $-1893.46 | -5.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4767 | 48.2 | 49.1 | $-2946.25 |
| ETH | 5241 | 48.0 | 48.6 | $-3521.70 |
| SOL | 5479 | 48.0 | 48.6 | $-3323.53 |
| XRP | 5545 | 48.6 | 48.5 | $-2555.33 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
