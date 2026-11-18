# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 18, 2:00 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 744 windows, 20512 settled trades, 65 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 385 | 33.2 | 34.9 | $-352.66 | -9.2% | $647.34 | -1.4 | done | can't tell from luck |
| reversal_15m_0.10pct | 2100 | 51.7 | 50.7 | $-450.32 | -2.1% | $549.68 | -1.0 | done | can't tell from luck |
| momentum_60m_0.30pct | 1731 | 49.9 | 49.5 | $-660.51 | -3.8% | $339.49 | -1.6 | done | can't tell from luck |
| value_ev10 | 938 | 37.7 | 39.1 | $-676.01 | -7.2% | $323.99 | -1.8 | done | can't tell from luck |
| trend_filter | 1206 | 49.8 | 50.9 | $-808.38 | -6.7% | $191.62 | -2.4 | done | losing for real |
| value_ev5 | 1417 | 40.2 | 41.1 | $-839.23 | -5.9% | $160.77 | -1.9 | done | can't tell from luck |
| reversal_60m_0.30pct | 1731 | 50.1 | 51.3 | $-1203.64 | -7.0% | $-203.64 | -3.0 | done | losing for real |
| coinflip | 2968 | 50.3 | 50.3 | $-1211.73 | -4.1% | $-211.73 | -2.2 | done | losing for real |
| momentum_15m_0.10pct | 2100 | 48.3 | 50.1 | $-1579.40 | -7.5% | $-579.40 | -3.5 | done | losing for real |
| momentum_5m_0.00pct | 2968 | 50.8 | 51.8 | $-1681.75 | -5.7% | $-681.75 | -3.2 | done | losing for real |
| always_up | 2968 | 47.0 | 49.6 | $-2786.46 | -9.4% | $-1786.46 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4648 | 48.1 | 49.1 | $-2972.93 |
| ETH | 5112 | 48.0 | 48.5 | $-3354.18 |
| SOL | 5344 | 48.0 | 48.6 | $-3269.89 |
| XRP | 5408 | 48.5 | 48.5 | $-2653.09 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
