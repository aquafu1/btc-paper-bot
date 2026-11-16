# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 16, 7:00 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 524 windows, 14450 settled trades, 74 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1232 | 51.2 | 49.8 | $-163.12 | -1.3% | $836.88 | -0.5 | done | can't tell from luck |
| value_ev20 | 269 | 34.6 | 35.6 | $-184.33 | -6.9% | $815.67 | -0.9 | done | can't tell from luck |
| momentum_15m_0.10pct | 1465 | 49.9 | 49.6 | $-523.74 | -3.6% | $476.26 | -1.4 | done | can't tell from luck |
| value_ev10 | 671 | 38.0 | 39.7 | $-526.39 | -7.8% | $473.61 | -1.7 | done | can't tell from luck |
| trend_filter | 851 | 49.5 | 50.7 | $-551.72 | -6.5% | $448.28 | -1.9 | done | can't tell from luck |
| value_ev5 | 1001 | 40.1 | 41.5 | $-700.00 | -7.0% | $300.00 | -1.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 1465 | 50.1 | 51.5 | $-1021.01 | -7.0% | $-21.01 | -2.7 | done | losing for real |
| coinflip | 2088 | 50.0 | 50.7 | $-1104.72 | -5.3% | $-104.72 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 1232 | 48.8 | 51.4 | $-1138.92 | -9.2% | $-138.92 | -3.3 | done | losing for real |
| momentum_5m_0.00pct | 2088 | 49.4 | 51.6 | $-1641.30 | -7.9% | $-641.30 | -3.7 | done | losing for real |
| always_up | 2088 | 46.4 | 50.1 | $-2379.83 | -11.4% | $-1379.83 | -5.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3271 | 47.4 | 49.2 | $-2611.47 |
| ETH | 3604 | 47.9 | 48.7 | $-2374.74 |
| SOL | 3768 | 47.6 | 49.0 | $-2724.90 |
| XRP | 3807 | 48.3 | 48.8 | $-2223.99 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
