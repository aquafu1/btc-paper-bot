# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 19, 8:20 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 865 windows, 23843 settled trades, 44 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 445 | 34.6 | 34.8 | $-223.90 | -5.0% | $776.10 | -0.8 | done | can't tell from luck |
| value_ev10 | 1091 | 38.0 | 39.1 | $-678.09 | -6.2% | $321.91 | -1.7 | done | can't tell from luck |
| momentum_60m_0.30pct | 2011 | 50.2 | 49.7 | $-786.76 | -3.9% | $213.24 | -1.8 | done | can't tell from luck |
| trend_filter | 1398 | 50.3 | 50.9 | $-862.42 | -6.2% | $137.58 | -2.4 | done | losing for real |
| reversal_15m_0.10pct | 2435 | 50.6 | 50.5 | $-998.59 | -4.1% | $1.41 | -2.0 | done | losing for real |
| value_ev5 | 1652 | 39.9 | 41.0 | $-1030.49 | -6.2% | $-30.49 | -2.1 | done | losing for real |
| momentum_15m_0.10pct | 2435 | 49.4 | 50.4 | $-1364.01 | -5.6% | $-364.01 | -2.8 | done | losing for real |
| reversal_60m_0.30pct | 2011 | 49.8 | 51.0 | $-1472.50 | -7.3% | $-472.50 | -3.4 | done | losing for real |
| momentum_5m_0.00pct | 3455 | 51.3 | 51.7 | $-1514.89 | -4.4% | $-514.89 | -2.7 | done | losing for real |
| coinflip | 3455 | 50.1 | 50.3 | $-1569.28 | -4.5% | $-569.28 | -2.7 | done | losing for real |
| always_up | 3455 | 46.9 | 49.6 | $-3372.90 | -9.8% | $-2372.90 | -5.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5440 | 48.3 | 49.0 | $-2983.68 |
| ETH | 5925 | 48.1 | 48.5 | $-3893.47 |
| SOL | 6223 | 48.3 | 48.6 | $-3539.59 |
| XRP | 6255 | 48.3 | 48.5 | $-3457.08 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
