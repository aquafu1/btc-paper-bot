# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 19, 6:00 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 808 windows, 22180 settled trades, 48 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 412 | 33.5 | 35.0 | $-331.28 | -8.0% | $668.72 | -1.2 | done | can't tell from luck |
| value_ev10 | 1015 | 37.8 | 39.2 | $-684.51 | -6.7% | $315.49 | -1.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 1859 | 50.1 | 49.6 | $-706.58 | -3.8% | $293.42 | -1.6 | done | can't tell from luck |
| trend_filter | 1297 | 50.3 | 50.9 | $-761.06 | -5.9% | $238.94 | -2.2 | done | losing for real |
| reversal_15m_0.10pct | 2266 | 50.8 | 50.6 | $-851.42 | -3.8% | $148.58 | -1.8 | done | can't tell from luck |
| value_ev5 | 1534 | 40.1 | 41.1 | $-896.63 | -5.8% | $103.37 | -1.9 | done | can't tell from luck |
| momentum_5m_0.00pct | 3224 | 51.4 | 51.6 | $-1315.25 | -4.1% | $-315.25 | -2.4 | done | losing for real |
| momentum_15m_0.10pct | 2266 | 49.2 | 50.2 | $-1338.55 | -5.9% | $-338.55 | -2.8 | done | losing for real |
| reversal_60m_0.30pct | 1859 | 49.9 | 51.2 | $-1348.51 | -7.3% | $-348.51 | -3.2 | done | losing for real |
| coinflip | 3224 | 50.2 | 50.3 | $-1374.49 | -4.3% | $-374.49 | -2.4 | done | losing for real |
| always_up | 3224 | 47.5 | 49.7 | $-2731.12 | -8.5% | $-1731.12 | -4.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5037 | 48.4 | 49.1 | $-2783.18 |
| ETH | 5523 | 48.2 | 48.5 | $-3462.54 |
| SOL | 5778 | 48.3 | 48.6 | $-3195.27 |
| XRP | 5842 | 48.5 | 48.5 | $-2898.41 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
