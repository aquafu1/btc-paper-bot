# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 14, 1:15 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 357 windows, 9626 settled trades, 59 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 186 | 37.1 | 36.6 | $-58.35 | -3.1% | $941.65 | -0.3 | Sat 8:15 PM | too few trades (186/200) |
| value_ev10 | 464 | 40.1 | 40.3 | $-201.42 | -4.3% | $798.58 | -0.8 | done | can't tell from luck |
| value_ev5 | 689 | 41.7 | 42.0 | $-330.39 | -4.8% | $669.61 | -1.1 | done | can't tell from luck |
| reversal_15m_0.10pct | 956 | 52.0 | 52.0 | $-404.93 | -4.2% | $595.07 | -1.4 | done | can't tell from luck |
| reversal_60m_0.30pct | 791 | 51.1 | 52.0 | $-454.80 | -5.7% | $545.20 | -1.7 | done | can't tell from luck |
| trend_filter | 533 | 48.2 | 50.5 | $-471.18 | -8.8% | $528.82 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 791 | 48.9 | 49.7 | $-479.59 | -6.1% | $520.41 | -1.7 | done | can't tell from luck |
| momentum_15m_0.10pct | 956 | 48.0 | 49.8 | $-722.95 | -7.6% | $277.05 | -2.4 | done | losing for real |
| coinflip | 1420 | 50.1 | 50.8 | $-756.12 | -5.3% | $243.88 | -2.1 | done | losing for real |
| momentum_5m_0.00pct | 1420 | 49.4 | 51.5 | $-1098.57 | -7.7% | $-98.57 | -3.0 | done | losing for real |
| always_up | 1420 | 46.3 | 50.6 | $-1750.27 | -12.3% | $-750.27 | -4.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2157 | 47.3 | 49.3 | $-1764.38 |
| ETH | 2422 | 47.6 | 48.8 | $-1756.48 |
| SOL | 2497 | 48.0 | 49.4 | $-1883.89 |
| XRP | 2550 | 48.8 | 49.1 | $-1323.81 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
