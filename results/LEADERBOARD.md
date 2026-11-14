# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 14, 8:15 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 337 windows, 9006 settled trades, 60 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 183 | 37.2 | 36.6 | $-52.79 | -2.9% | $947.21 | -0.3 | Sat 4:15 PM | too few trades (183/200) |
| reversal_60m_0.30pct | 719 | 53.3 | 51.9 | $-105.46 | -1.5% | $894.54 | -0.4 | done | can't tell from luck |
| reversal_15m_0.10pct | 891 | 52.5 | 51.9 | $-286.72 | -3.2% | $713.28 | -1.0 | done | can't tell from luck |
| value_ev10 | 441 | 38.8 | 40.2 | $-323.09 | -7.3% | $676.91 | -1.3 | done | can't tell from luck |
| value_ev5 | 655 | 40.5 | 41.9 | $-487.54 | -7.4% | $512.46 | -1.7 | done | can't tell from luck |
| trend_filter | 487 | 45.4 | 50.3 | $-683.95 | -14.0% | $316.05 | -3.2 | done | losing for real |
| coinflip | 1340 | 50.0 | 50.8 | $-762.24 | -5.7% | $237.76 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 719 | 46.7 | 49.7 | $-762.69 | -10.6% | $237.31 | -2.9 | done | losing for real |
| momentum_15m_0.10pct | 891 | 47.5 | 49.8 | $-790.45 | -8.9% | $209.55 | -2.7 | done | losing for real |
| momentum_5m_0.00pct | 1340 | 48.7 | 51.3 | $-1192.77 | -8.9% | $-192.77 | -3.4 | done | losing for real |
| always_up | 1340 | 47.6 | 50.4 | $-1281.84 | -9.6% | $-281.84 | -3.6 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2013 | 46.8 | 49.2 | $-1786.92 |
| ETH | 2262 | 47.3 | 48.6 | $-1799.87 |
| SOL | 2346 | 47.9 | 49.2 | $-1857.74 |
| XRP | 2385 | 48.7 | 49.0 | $-1285.02 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
