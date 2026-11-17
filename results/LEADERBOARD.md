# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 16, 10:05 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 584 windows, 16180 settled trades, 38 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1375 | 51.3 | 49.6 | $-207.15 | -1.5% | $792.85 | -0.6 | done | can't tell from luck |
| value_ev20 | 317 | 33.1 | 35.3 | $-362.24 | -11.4% | $637.76 | -1.6 | done | can't tell from luck |
| trend_filter | 938 | 50.5 | 50.9 | $-482.40 | -5.1% | $517.60 | -1.6 | done | can't tell from luck |
| value_ev10 | 760 | 37.4 | 39.4 | $-744.69 | -9.8% | $255.31 | -2.3 | done | losing for real |
| reversal_15m_0.10pct | 1643 | 50.8 | 51.0 | $-829.56 | -5.0% | $170.44 | -2.1 | done | losing for real |
| value_ev5 | 1136 | 40.1 | 41.3 | $-843.28 | -7.4% | $156.72 | -2.2 | done | losing for real |
| momentum_15m_0.10pct | 1643 | 49.2 | 49.9 | $-942.32 | -5.7% | $57.68 | -2.3 | done | losing for real |
| coinflip | 2331 | 49.9 | 50.5 | $-1227.78 | -5.3% | $-227.78 | -2.6 | done | losing for real |
| reversal_60m_0.30pct | 1375 | 48.7 | 51.3 | $-1359.11 | -9.9% | $-359.11 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 2331 | 50.2 | 51.8 | $-1618.19 | -6.9% | $-618.19 | -3.5 | done | losing for real |
| always_up | 2331 | 47.3 | 49.9 | $-2207.16 | -9.5% | $-1207.16 | -4.6 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3676 | 47.8 | 49.2 | $-2695.61 |
| ETH | 4032 | 48.0 | 48.6 | $-2715.86 |
| SOL | 4205 | 47.8 | 48.8 | $-3126.51 |
| XRP | 4267 | 48.5 | 48.6 | $-2285.87 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
