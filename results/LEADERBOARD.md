# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 18, 12:35 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 738 windows, 20377 settled trades, 27 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 385 | 33.2 | 34.9 | $-352.66 | -9.2% | $647.34 | -1.4 | done | can't tell from luck |
| reversal_15m_0.10pct | 2087 | 51.7 | 50.7 | $-457.08 | -2.2% | $542.92 | -1.0 | done | can't tell from luck |
| momentum_60m_0.30pct | 1718 | 50.0 | 49.6 | $-631.97 | -3.7% | $368.03 | -1.5 | done | can't tell from luck |
| value_ev10 | 933 | 37.8 | 39.1 | $-649.20 | -7.0% | $350.80 | -1.7 | done | can't tell from luck |
| value_ev5 | 1407 | 40.4 | 41.1 | $-762.43 | -5.4% | $237.57 | -1.7 | done | can't tell from luck |
| trend_filter | 1198 | 49.9 | 51.0 | $-767.67 | -6.4% | $232.33 | -2.3 | done | losing for real |
| coinflip | 2948 | 50.4 | 50.3 | $-1135.95 | -3.9% | $-135.95 | -2.1 | done | losing for real |
| reversal_60m_0.30pct | 1718 | 50.0 | 51.2 | $-1205.82 | -7.0% | $-205.82 | -3.0 | done | losing for real |
| momentum_15m_0.10pct | 2087 | 48.3 | 50.1 | $-1527.00 | -7.3% | $-527.00 | -3.4 | done | losing for real |
| momentum_5m_0.00pct | 2948 | 50.8 | 51.8 | $-1629.52 | -5.5% | $-629.52 | -3.1 | done | losing for real |
| always_up | 2948 | 47.0 | 49.6 | $-2704.14 | -9.2% | $-1704.14 | -5.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4617 | 48.1 | 49.1 | $-2916.76 |
| ETH | 5080 | 48.1 | 48.6 | $-3252.21 |
| SOL | 5306 | 48.2 | 48.7 | $-3062.96 |
| XRP | 5374 | 48.5 | 48.5 | $-2591.53 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
