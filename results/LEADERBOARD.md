# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 22, 5:35 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1142 windows, 31567 settled trades, 44 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 607 | 34.6 | 35.2 | $-382.50 | -6.3% | $617.50 | -1.2 | done | can't tell from luck |
| value_ev10 | 1480 | 38.1 | 39.2 | $-936.39 | -6.3% | $63.61 | -2.0 | done | can't tell from luck |
| reversal_15m_0.10pct | 3174 | 50.9 | 50.4 | $-972.38 | -3.1% | $27.62 | -1.7 | done | can't tell from luck |
| momentum_60m_0.30pct | 2664 | 49.6 | 49.4 | $-1193.41 | -4.5% | $-193.41 | -2.3 | done | losing for real |
| value_ev5 | 2239 | 40.1 | 41.1 | $-1319.10 | -5.9% | $-319.10 | -2.4 | done | losing for real |
| trend_filter | 1876 | 48.9 | 50.5 | $-1515.23 | -8.1% | $-515.23 | -3.6 | done | losing for real |
| reversal_60m_0.30pct | 2664 | 50.4 | 51.1 | $-1620.98 | -6.1% | $-620.98 | -3.2 | done | losing for real |
| coinflip | 4563 | 50.3 | 50.2 | $-1883.93 | -4.1% | $-883.93 | -2.8 | done | losing for real |
| momentum_15m_0.10pct | 3174 | 49.1 | 50.2 | $-1983.53 | -6.2% | $-983.53 | -3.6 | done | losing for real |
| momentum_5m_0.00pct | 4563 | 50.2 | 51.4 | $-2848.78 | -6.2% | $-1848.78 | -4.4 | done | losing for real |
| always_up | 4563 | 47.8 | 49.3 | $-3391.10 | -7.4% | $-2391.10 | -5.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7229 | 48.3 | 49.0 | $-3795.15 |
| ETH | 7823 | 48.2 | 48.4 | $-4624.22 |
| SOL | 8219 | 48.1 | 48.4 | $-4583.92 |
| XRP | 8296 | 48.1 | 48.3 | $-5044.05 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
