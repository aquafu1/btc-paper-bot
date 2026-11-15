# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 15, 3:35 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 462 windows, 12693 settled trades, 45 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 236 | 34.7 | 35.9 | $-162.48 | -6.9% | $837.52 | -0.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 1074 | 50.9 | 50.0 | $-263.64 | -2.5% | $736.36 | -0.8 | done | can't tell from luck |
| value_ev10 | 600 | 39.2 | 40.1 | $-353.68 | -5.9% | $646.32 | -1.2 | done | can't tell from luck |
| trend_filter | 734 | 49.7 | 50.7 | $-435.98 | -5.9% | $564.02 | -1.6 | done | can't tell from luck |
| value_ev5 | 886 | 41.2 | 41.8 | $-467.06 | -5.3% | $532.94 | -1.4 | done | can't tell from luck |
| momentum_15m_0.10pct | 1283 | 49.8 | 50.0 | $-502.84 | -3.9% | $497.16 | -1.4 | done | can't tell from luck |
| reversal_15m_0.10pct | 1283 | 50.2 | 51.6 | $-903.46 | -7.0% | $96.54 | -2.6 | done | losing for real |
| coinflip | 1841 | 50.1 | 50.8 | $-963.01 | -5.2% | $36.99 | -2.3 | done | losing for real |
| reversal_60m_0.30pct | 1074 | 49.1 | 51.8 | $-1026.20 | -9.6% | $-26.20 | -3.3 | done | losing for real |
| momentum_5m_0.00pct | 1841 | 49.7 | 51.6 | $-1329.92 | -7.2% | $-329.92 | -3.2 | done | losing for real |
| always_up | 1841 | 46.2 | 50.4 | $-2260.72 | -12.3% | $-1260.72 | -5.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2872 | 47.5 | 49.2 | $-2232.45 |
| ETH | 3189 | 48.1 | 48.8 | $-2042.16 |
| SOL | 3301 | 47.7 | 49.3 | $-2564.91 |
| XRP | 3331 | 48.6 | 49.2 | $-1829.47 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
