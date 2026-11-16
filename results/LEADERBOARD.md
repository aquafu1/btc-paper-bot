# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 15, 8:00 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 480 windows, 13172 settled trades, 56 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 240 | 35.4 | 35.9 | $-102.29 | -4.3% | $897.71 | -0.5 | done | can't tell from luck |
| momentum_60m_0.30pct | 1117 | 51.1 | 49.8 | $-148.99 | -1.3% | $851.01 | -0.4 | done | can't tell from luck |
| value_ev10 | 620 | 39.2 | 40.1 | $-322.51 | -5.2% | $677.49 | -1.1 | done | can't tell from luck |
| momentum_15m_0.10pct | 1329 | 50.1 | 50.0 | $-420.20 | -3.2% | $579.80 | -1.1 | done | can't tell from luck |
| value_ev5 | 917 | 41.1 | 41.8 | $-450.05 | -4.9% | $549.95 | -1.3 | done | can't tell from luck |
| trend_filter | 767 | 49.7 | 50.8 | $-469.83 | -6.1% | $530.17 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 1329 | 49.9 | 51.5 | $-936.32 | -7.0% | $63.68 | -2.6 | done | losing for real |
| coinflip | 1912 | 49.9 | 50.8 | $-997.28 | -5.2% | $2.72 | -2.3 | done | losing for real |
| reversal_60m_0.30pct | 1117 | 48.9 | 51.5 | $-1029.39 | -9.2% | $-29.39 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 1912 | 49.6 | 51.7 | $-1431.15 | -7.5% | $-431.15 | -3.4 | done | losing for real |
| always_up | 1912 | 46.3 | 50.5 | $-2263.96 | -11.8% | $-1263.96 | -5.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2970 | 47.4 | 49.3 | $-2356.70 |
| ETH | 3302 | 48.1 | 48.8 | $-2098.17 |
| SOL | 3430 | 47.8 | 49.3 | $-2421.58 |
| XRP | 3470 | 48.6 | 49.0 | $-1695.51 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
