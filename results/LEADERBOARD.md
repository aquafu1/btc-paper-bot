# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 15, 2:30 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 410 windows, 11230 settled trades, 67 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 202 | 36.1 | 36.5 | $-86.95 | -4.3% | $913.05 | -0.5 | done | can't tell from luck |
| momentum_60m_0.30pct | 959 | 51.1 | 50.0 | $-184.67 | -1.9% | $815.33 | -0.6 | done | can't tell from luck |
| value_ev10 | 526 | 40.1 | 40.5 | $-223.49 | -4.2% | $776.51 | -0.8 | done | can't tell from luck |
| trend_filter | 634 | 50.2 | 50.7 | $-313.07 | -4.9% | $686.93 | -1.3 | done | can't tell from luck |
| value_ev5 | 792 | 41.9 | 42.2 | $-332.64 | -4.2% | $667.36 | -1.0 | done | can't tell from luck |
| momentum_15m_0.10pct | 1131 | 49.3 | 49.9 | $-523.69 | -4.6% | $476.31 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 1131 | 50.7 | 51.9 | $-713.75 | -6.3% | $286.25 | -2.2 | done | losing for real |
| coinflip | 1632 | 50.2 | 50.9 | $-816.60 | -5.0% | $183.40 | -2.1 | done | losing for real |
| reversal_60m_0.30pct | 959 | 48.9 | 51.9 | $-912.07 | -9.5% | $87.93 | -3.1 | done | losing for real |
| momentum_5m_0.00pct | 1632 | 49.8 | 51.6 | $-1111.68 | -6.8% | $-111.68 | -2.8 | done | losing for real |
| always_up | 1632 | 45.6 | 50.6 | $-2165.78 | -13.3% | $-1165.78 | -5.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2536 | 47.6 | 49.5 | $-1841.04 |
| ETH | 2823 | 47.9 | 49.0 | $-1766.72 |
| SOL | 2905 | 47.9 | 49.5 | $-2249.82 |
| XRP | 2966 | 48.9 | 49.3 | $-1526.82 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
