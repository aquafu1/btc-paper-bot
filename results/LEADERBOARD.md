# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 16, 3:20 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 557 windows, 15465 settled trades, 24 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1314 | 51.1 | 49.7 | $-282.47 | -2.1% | $717.53 | -0.8 | done | can't tell from luck |
| value_ev20 | 306 | 33.0 | 35.2 | $-355.92 | -11.6% | $644.08 | -1.6 | done | can't tell from luck |
| trend_filter | 897 | 50.4 | 51.1 | $-516.64 | -5.8% | $483.36 | -1.8 | done | can't tell from luck |
| value_ev10 | 733 | 37.0 | 39.3 | $-772.65 | -10.5% | $227.35 | -2.4 | done | losing for real |
| momentum_15m_0.10pct | 1570 | 49.3 | 49.8 | $-853.33 | -5.4% | $146.67 | -2.2 | done | losing for real |
| reversal_15m_0.10pct | 1570 | 50.7 | 51.1 | $-902.94 | -5.8% | $97.06 | -2.3 | done | losing for real |
| value_ev5 | 1092 | 39.4 | 41.2 | $-947.77 | -8.7% | $52.23 | -2.5 | done | losing for real |
| coinflip | 2223 | 49.9 | 50.5 | $-1234.68 | -5.6% | $-234.68 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 1314 | 48.9 | 51.2 | $-1267.13 | -9.6% | $-267.13 | -3.6 | done | losing for real |
| momentum_5m_0.00pct | 2223 | 50.3 | 51.8 | $-1559.28 | -7.0% | $-559.28 | -3.5 | done | losing for real |
| always_up | 2223 | 46.9 | 49.9 | $-2359.71 | -10.6% | $-1359.71 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3493 | 47.5 | 49.2 | $-2807.40 |
| ETH | 3854 | 47.8 | 48.6 | $-2811.29 |
| SOL | 4036 | 47.7 | 48.7 | $-3103.55 |
| XRP | 4082 | 48.5 | 48.6 | $-2330.27 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
