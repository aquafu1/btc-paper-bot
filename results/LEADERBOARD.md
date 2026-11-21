# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 21, 5:00 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1044 windows, 28964 settled trades, 65 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 541 | 34.6 | 35.1 | $-305.47 | -5.6% | $694.53 | -1.0 | done | can't tell from luck |
| reversal_15m_0.10pct | 2939 | 51.2 | 50.4 | $-782.15 | -2.7% | $217.85 | -1.4 | done | can't tell from luck |
| value_ev10 | 1339 | 37.4 | 39.2 | $-1019.40 | -7.6% | $-19.40 | -2.3 | done | losing for real |
| momentum_60m_0.30pct | 2473 | 49.7 | 49.6 | $-1138.12 | -4.6% | $-138.12 | -2.3 | done | losing for real |
| trend_filter | 1729 | 49.3 | 50.7 | $-1335.88 | -7.7% | $-335.88 | -3.3 | done | losing for real |
| value_ev5 | 2027 | 39.4 | 41.0 | $-1457.23 | -7.2% | $-457.23 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 2473 | 50.3 | 51.0 | $-1596.09 | -6.5% | $-596.09 | -3.3 | done | losing for real |
| coinflip | 4168 | 50.5 | 50.3 | $-1684.80 | -4.0% | $-684.80 | -2.6 | done | losing for real |
| momentum_15m_0.10pct | 2939 | 48.8 | 50.3 | $-2065.14 | -7.0% | $-1065.14 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 4168 | 50.8 | 51.5 | $-2258.09 | -5.4% | $-1258.09 | -3.6 | done | losing for real |
| always_up | 4168 | 47.3 | 49.4 | $-3665.97 | -8.8% | $-2665.97 | -5.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6601 | 48.3 | 49.0 | $-3553.88 |
| ETH | 7173 | 48.1 | 48.5 | $-4440.38 |
| SOL | 7565 | 48.1 | 48.5 | $-4500.52 |
| XRP | 7625 | 48.1 | 48.3 | $-4813.55 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
