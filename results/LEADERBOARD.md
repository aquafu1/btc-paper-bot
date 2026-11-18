# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 17, 11:35 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 686 windows, 18977 settled trades, 58 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 359 | 34.5 | 35.0 | $-203.12 | -5.7% | $796.88 | -0.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 1602 | 50.4 | 49.5 | $-433.85 | -2.7% | $566.15 | -1.1 | done | can't tell from luck |
| value_ev10 | 876 | 38.6 | 39.2 | $-469.28 | -5.4% | $530.72 | -1.3 | done | can't tell from luck |
| reversal_15m_0.10pct | 1952 | 51.5 | 50.9 | $-568.51 | -2.9% | $431.49 | -1.3 | done | can't tell from luck |
| value_ev5 | 1318 | 40.9 | 41.1 | $-584.58 | -4.4% | $415.42 | -1.4 | done | can't tell from luck |
| trend_filter | 1105 | 50.2 | 50.9 | $-606.29 | -5.5% | $393.71 | -1.9 | done | can't tell from luck |
| coinflip | 2737 | 50.2 | 50.3 | $-1154.96 | -4.2% | $-154.96 | -2.2 | done | losing for real |
| reversal_60m_0.30pct | 1602 | 49.6 | 51.3 | $-1243.87 | -7.8% | $-243.87 | -3.2 | done | losing for real |
| momentum_15m_0.10pct | 1952 | 48.5 | 49.9 | $-1304.03 | -6.7% | $-304.03 | -2.9 | done | losing for real |
| momentum_5m_0.00pct | 2737 | 50.7 | 51.8 | $-1531.85 | -5.6% | $-531.85 | -3.0 | done | losing for real |
| always_up | 2737 | 47.5 | 49.6 | $-2287.03 | -8.4% | $-1287.03 | -4.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4320 | 48.3 | 49.1 | $-2460.57 |
| ETH | 4725 | 48.3 | 48.6 | $-2771.57 |
| SOL | 4945 | 48.1 | 48.6 | $-2865.82 |
| XRP | 4987 | 48.6 | 48.4 | $-2289.40 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
