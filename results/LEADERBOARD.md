# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 15, 3:05 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 460 windows, 12637 settled trades, 51 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 232 | 34.5 | 35.9 | $-179.55 | -7.7% | $820.45 | -0.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 1074 | 50.9 | 50.0 | $-263.64 | -2.5% | $736.36 | -0.8 | done | can't tell from luck |
| value_ev10 | 595 | 39.2 | 40.1 | $-360.75 | -6.1% | $639.25 | -1.2 | done | can't tell from luck |
| trend_filter | 733 | 49.8 | 50.7 | $-425.98 | -5.8% | $574.02 | -1.6 | done | can't tell from luck |
| value_ev5 | 881 | 41.2 | 41.8 | $-474.13 | -5.4% | $525.87 | -1.4 | done | can't tell from luck |
| momentum_15m_0.10pct | 1276 | 49.9 | 50.0 | $-482.05 | -3.8% | $517.95 | -1.4 | done | can't tell from luck |
| reversal_15m_0.10pct | 1276 | 50.1 | 51.6 | $-921.14 | -7.2% | $78.86 | -2.7 | done | losing for real |
| coinflip | 1832 | 49.9 | 50.8 | $-1011.03 | -5.5% | $-11.03 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 1074 | 49.1 | 51.8 | $-1026.20 | -9.6% | $-26.20 | -3.3 | done | losing for real |
| momentum_5m_0.00pct | 1832 | 49.6 | 51.5 | $-1335.19 | -7.3% | $-335.19 | -3.2 | done | losing for real |
| always_up | 1832 | 46.3 | 50.5 | $-2227.79 | -12.2% | $-1227.79 | -5.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2858 | 47.5 | 49.3 | $-2298.14 |
| ETH | 3173 | 48.1 | 48.8 | $-2016.74 |
| SOL | 3290 | 47.8 | 49.3 | $-2514.81 |
| XRP | 3316 | 48.6 | 49.2 | $-1877.77 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
