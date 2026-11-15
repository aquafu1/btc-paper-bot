# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 15, 2:20 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 409 windows, 11216 settled trades, 47 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 202 | 36.1 | 36.5 | $-86.95 | -4.3% | $913.05 | -0.5 | done | can't tell from luck |
| momentum_60m_0.30pct | 957 | 51.1 | 50.0 | $-179.68 | -1.9% | $820.32 | -0.6 | done | can't tell from luck |
| value_ev10 | 526 | 40.1 | 40.5 | $-223.49 | -4.2% | $776.51 | -0.8 | done | can't tell from luck |
| trend_filter | 634 | 50.2 | 50.7 | $-313.07 | -4.9% | $686.93 | -1.3 | done | can't tell from luck |
| value_ev5 | 792 | 41.9 | 42.2 | $-332.64 | -4.2% | $667.36 | -1.0 | done | can't tell from luck |
| momentum_15m_0.10pct | 1129 | 49.3 | 49.9 | $-526.43 | -4.7% | $473.57 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 1129 | 50.7 | 51.9 | $-708.76 | -6.3% | $291.24 | -2.2 | done | losing for real |
| coinflip | 1630 | 50.2 | 50.9 | $-811.61 | -5.0% | $188.39 | -2.1 | done | losing for real |
| reversal_60m_0.30pct | 957 | 48.9 | 51.9 | $-914.80 | -9.6% | $85.20 | -3.1 | done | losing for real |
| momentum_5m_0.00pct | 1630 | 49.8 | 51.6 | $-1114.42 | -6.8% | $-114.42 | -2.9 | done | losing for real |
| always_up | 1630 | 45.6 | 50.7 | $-2168.52 | -13.3% | $-1168.52 | -5.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2529 | 47.6 | 49.5 | $-1816.06 |
| ETH | 2823 | 47.9 | 49.0 | $-1766.72 |
| SOL | 2905 | 47.9 | 49.5 | $-2249.82 |
| XRP | 2959 | 48.9 | 49.3 | $-1547.76 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
