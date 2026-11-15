# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 15, 3:45 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 463 windows, 12716 settled trades, 44 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 236 | 34.7 | 35.9 | $-162.48 | -6.9% | $837.52 | -0.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 1077 | 50.8 | 50.0 | $-293.64 | -2.7% | $706.36 | -0.9 | done | can't tell from luck |
| value_ev10 | 602 | 39.0 | 40.1 | $-373.68 | -6.2% | $626.32 | -1.3 | done | can't tell from luck |
| trend_filter | 734 | 49.7 | 50.7 | $-435.98 | -5.9% | $564.02 | -1.6 | done | can't tell from luck |
| momentum_15m_0.10pct | 1285 | 49.9 | 50.0 | $-486.49 | -3.8% | $513.51 | -1.4 | done | can't tell from luck |
| value_ev5 | 888 | 41.1 | 41.8 | $-487.06 | -5.5% | $512.94 | -1.4 | done | can't tell from luck |
| reversal_15m_0.10pct | 1285 | 50.1 | 51.6 | $-923.46 | -7.2% | $76.54 | -2.7 | done | losing for real |
| coinflip | 1844 | 50.0 | 50.8 | $-993.01 | -5.4% | $6.99 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 1077 | 49.2 | 51.8 | $-1004.14 | -9.3% | $-4.14 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 1844 | 49.8 | 51.6 | $-1307.87 | -7.1% | $-307.87 | -3.2 | done | losing for real |
| always_up | 1844 | 46.1 | 50.4 | $-2290.72 | -12.4% | $-1290.72 | -5.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2879 | 47.5 | 49.2 | $-2242.23 |
| ETH | 3189 | 48.1 | 48.8 | $-2042.16 |
| SOL | 3310 | 47.7 | 49.3 | $-2606.08 |
| XRP | 3338 | 48.5 | 49.1 | $-1868.07 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
