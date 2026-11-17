# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 17, 8:15 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 625 windows, 17270 settled trades, 56 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1461 | 51.3 | 49.5 | $-127.87 | -0.9% | $872.13 | -0.3 | done | can't tell from luck |
| value_ev20 | 329 | 34.0 | 35.3 | $-264.70 | -8.0% | $735.30 | -1.1 | done | can't tell from luck |
| trend_filter | 1000 | 50.3 | 50.8 | $-531.18 | -5.3% | $468.82 | -1.7 | done | can't tell from luck |
| value_ev10 | 799 | 38.3 | 39.5 | $-574.31 | -7.2% | $425.69 | -1.7 | done | can't tell from luck |
| value_ev5 | 1208 | 40.6 | 41.4 | $-725.77 | -6.0% | $274.23 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 1768 | 50.8 | 51.0 | $-838.12 | -4.7% | $161.88 | -2.0 | done | losing for real |
| momentum_15m_0.10pct | 1768 | 49.2 | 49.9 | $-954.04 | -5.4% | $45.96 | -2.3 | done | losing for real |
| coinflip | 2492 | 50.0 | 50.5 | $-1226.57 | -4.9% | $-226.57 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 1461 | 48.7 | 51.4 | $-1445.88 | -9.9% | $-445.88 | -3.9 | done | losing for real |
| momentum_5m_0.00pct | 2492 | 50.4 | 51.7 | $-1540.18 | -6.2% | $-540.18 | -3.2 | done | losing for real |
| always_up | 2492 | 47.5 | 49.7 | $-2097.50 | -8.4% | $-1097.50 | -4.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3921 | 48.2 | 49.2 | $-2412.16 |
| ETH | 4322 | 48.2 | 48.6 | $-2593.96 |
| SOL | 4487 | 47.9 | 48.8 | $-3007.06 |
| XRP | 4540 | 48.5 | 48.5 | $-2312.95 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
