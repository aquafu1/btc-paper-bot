# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 18, 1:45 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 743 windows, 20489 settled trades, 53 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 385 | 33.2 | 34.9 | $-352.66 | -9.2% | $647.34 | -1.4 | done | can't tell from luck |
| reversal_15m_0.10pct | 2100 | 51.7 | 50.7 | $-450.32 | -2.1% | $549.68 | -1.0 | done | can't tell from luck |
| value_ev10 | 938 | 37.7 | 39.1 | $-676.01 | -7.2% | $323.99 | -1.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 1727 | 49.8 | 49.5 | $-698.77 | -4.0% | $301.23 | -1.7 | done | can't tell from luck |
| trend_filter | 1204 | 49.7 | 50.9 | $-827.67 | -6.9% | $172.33 | -2.4 | done | losing for real |
| value_ev5 | 1416 | 40.3 | 41.1 | $-829.23 | -5.9% | $170.77 | -1.9 | done | can't tell from luck |
| reversal_60m_0.30pct | 1727 | 50.2 | 51.3 | $-1163.64 | -6.7% | $-163.64 | -2.9 | done | losing for real |
| coinflip | 2964 | 50.3 | 50.3 | $-1193.10 | -4.0% | $-193.10 | -2.2 | done | losing for real |
| momentum_15m_0.10pct | 2100 | 48.3 | 50.1 | $-1579.40 | -7.5% | $-579.40 | -3.5 | done | losing for real |
| momentum_5m_0.00pct | 2964 | 50.8 | 51.8 | $-1681.04 | -5.7% | $-681.04 | -3.2 | done | losing for real |
| always_up | 2964 | 47.0 | 49.6 | $-2746.46 | -9.3% | $-1746.46 | -5.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4642 | 48.1 | 49.1 | $-2998.40 |
| ETH | 5107 | 48.0 | 48.5 | $-3325.54 |
| SOL | 5338 | 48.1 | 48.6 | $-3227.50 |
| XRP | 5402 | 48.5 | 48.5 | $-2646.86 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
