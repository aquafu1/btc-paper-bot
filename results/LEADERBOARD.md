# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 19, 1:35 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 838 windows, 23042 settled trades, 43 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 423 | 33.1 | 34.9 | $-400.80 | -9.5% | $599.20 | -1.5 | done | can't tell from luck |
| value_ev10 | 1049 | 37.3 | 39.1 | $-869.14 | -8.3% | $130.86 | -2.2 | done | losing for real |
| reversal_15m_0.10pct | 2354 | 50.9 | 50.6 | $-879.33 | -3.7% | $120.67 | -1.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 1939 | 49.8 | 49.6 | $-933.55 | -4.8% | $66.45 | -2.1 | done | losing for real |
| trend_filter | 1357 | 49.7 | 50.8 | $-980.66 | -7.2% | $19.34 | -2.7 | done | losing for real |
| value_ev5 | 1589 | 39.6 | 41.1 | $-1153.24 | -7.3% | $-153.24 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 1939 | 50.2 | 51.2 | $-1323.75 | -6.8% | $-323.75 | -3.1 | done | losing for real |
| coinflip | 3346 | 50.3 | 50.3 | $-1455.65 | -4.4% | $-455.65 | -2.5 | done | losing for real |
| momentum_15m_0.10pct | 2354 | 49.1 | 50.3 | $-1479.24 | -6.3% | $-479.24 | -3.1 | done | losing for real |
| momentum_5m_0.00pct | 3346 | 51.3 | 51.7 | $-1560.75 | -4.7% | $-560.75 | -2.8 | done | losing for real |
| always_up | 3346 | 47.2 | 49.6 | $-3099.56 | -9.3% | $-2099.56 | -5.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5233 | 48.1 | 49.1 | $-3342.40 |
| ETH | 5738 | 48.0 | 48.5 | $-3916.69 |
| SOL | 6014 | 48.2 | 48.6 | $-3513.92 |
| XRP | 6057 | 48.4 | 48.5 | $-3362.66 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
