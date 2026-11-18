# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 18, 1:15 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 741 windows, 20428 settled trades, 61 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 385 | 33.2 | 34.9 | $-352.66 | -9.2% | $647.34 | -1.4 | done | can't tell from luck |
| reversal_15m_0.10pct | 2092 | 51.8 | 50.7 | $-419.73 | -2.0% | $580.27 | -0.9 | done | can't tell from luck |
| value_ev10 | 933 | 37.8 | 39.1 | $-649.20 | -7.0% | $350.80 | -1.7 | done | can't tell from luck |
| momentum_60m_0.30pct | 1723 | 49.9 | 49.6 | $-681.97 | -4.0% | $318.03 | -1.6 | done | can't tell from luck |
| value_ev5 | 1409 | 40.4 | 41.1 | $-782.43 | -5.6% | $217.57 | -1.8 | done | can't tell from luck |
| trend_filter | 1203 | 49.7 | 50.9 | $-817.67 | -6.8% | $182.33 | -2.4 | done | losing for real |
| coinflip | 2956 | 50.4 | 50.3 | $-1145.78 | -3.9% | $-145.78 | -2.1 | done | losing for real |
| reversal_60m_0.30pct | 1723 | 50.1 | 51.3 | $-1170.38 | -6.8% | $-170.38 | -2.9 | done | losing for real |
| momentum_15m_0.10pct | 2092 | 48.2 | 50.1 | $-1577.00 | -7.5% | $-577.00 | -3.5 | done | losing for real |
| momentum_5m_0.00pct | 2956 | 50.7 | 51.8 | $-1691.60 | -5.7% | $-691.60 | -3.2 | done | losing for real |
| always_up | 2956 | 47.1 | 49.6 | $-2715.88 | -9.2% | $-1715.88 | -5.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4628 | 48.1 | 49.1 | $-2954.09 |
| ETH | 5092 | 48.0 | 48.6 | $-3284.77 |
| SOL | 5321 | 48.1 | 48.7 | $-3147.82 |
| XRP | 5387 | 48.5 | 48.5 | $-2617.62 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
