# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 15, 4:45 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 467 windows, 12808 settled trades, 53 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 237 | 35.0 | 35.9 | $-136.40 | -5.8% | $863.60 | -0.7 | done | can't tell from luck |
| momentum_60m_0.30pct | 1083 | 50.9 | 49.9 | $-252.41 | -2.3% | $747.59 | -0.8 | done | can't tell from luck |
| value_ev10 | 606 | 39.1 | 40.1 | $-353.06 | -5.8% | $646.94 | -1.2 | done | can't tell from luck |
| trend_filter | 739 | 49.8 | 50.7 | $-424.19 | -5.7% | $575.81 | -1.6 | done | can't tell from luck |
| momentum_15m_0.10pct | 1292 | 50.0 | 50.0 | $-458.91 | -3.6% | $541.09 | -1.3 | done | can't tell from luck |
| value_ev5 | 896 | 41.1 | 41.8 | $-475.95 | -5.3% | $524.05 | -1.4 | done | can't tell from luck |
| reversal_15m_0.10pct | 1292 | 50.0 | 51.6 | $-950.61 | -7.4% | $49.39 | -2.8 | done | losing for real |
| reversal_60m_0.30pct | 1083 | 49.1 | 51.8 | $-1022.08 | -9.4% | $-22.08 | -3.3 | done | losing for real |
| coinflip | 1860 | 49.9 | 50.8 | $-1023.63 | -5.5% | $-23.63 | -2.4 | done | losing for real |
| momentum_5m_0.00pct | 1860 | 49.8 | 51.6 | $-1296.35 | -7.0% | $-296.35 | -3.1 | done | losing for real |
| always_up | 1860 | 46.5 | 50.4 | $-2110.72 | -11.3% | $-1110.72 | -5.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2897 | 47.6 | 49.3 | $-2186.21 |
| ETH | 3212 | 48.1 | 48.8 | $-2052.96 |
| SOL | 3335 | 47.7 | 49.3 | $-2564.97 |
| XRP | 3364 | 48.6 | 49.1 | $-1700.18 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
