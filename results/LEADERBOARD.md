# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 19, 11:15 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 877 windows, 24205 settled trades, 61 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 455 | 35.6 | 34.9 | $-103.64 | -2.3% | $896.36 | -0.4 | done | can't tell from luck |
| value_ev10 | 1108 | 38.4 | 39.1 | $-559.03 | -5.0% | $440.97 | -1.4 | done | can't tell from luck |
| momentum_60m_0.30pct | 2047 | 50.1 | 49.8 | $-843.44 | -4.1% | $156.56 | -1.9 | done | can't tell from luck |
| trend_filter | 1425 | 50.2 | 51.0 | $-944.70 | -6.6% | $55.30 | -2.6 | done | losing for real |
| value_ev5 | 1675 | 40.1 | 41.0 | $-946.25 | -5.6% | $53.75 | -1.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 2474 | 50.5 | 50.4 | $-984.79 | -4.0% | $15.21 | -2.0 | done | can't tell from luck |
| momentum_15m_0.10pct | 2474 | 49.5 | 50.4 | $-1384.66 | -5.6% | $-384.66 | -2.8 | done | losing for real |
| reversal_60m_0.30pct | 2047 | 49.9 | 50.9 | $-1414.40 | -6.9% | $-414.40 | -3.2 | done | losing for real |
| coinflip | 3500 | 50.1 | 50.3 | $-1569.83 | -4.5% | $-569.83 | -2.7 | done | losing for real |
| momentum_5m_0.00pct | 3500 | 51.3 | 51.7 | $-1608.31 | -4.6% | $-608.31 | -2.8 | done | losing for real |
| always_up | 3500 | 46.9 | 49.6 | $-3438.16 | -9.8% | $-2438.16 | -5.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5524 | 48.3 | 49.1 | $-2994.27 |
| ETH | 6019 | 48.1 | 48.6 | $-3795.16 |
| SOL | 6317 | 48.2 | 48.5 | $-3650.16 |
| XRP | 6345 | 48.4 | 48.5 | $-3357.62 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
