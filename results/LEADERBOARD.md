# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 15, 2:50 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 459 windows, 12618 settled trades, 50 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 232 | 34.5 | 35.9 | $-179.55 | -7.7% | $820.45 | -0.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 1074 | 50.9 | 50.0 | $-263.64 | -2.5% | $736.36 | -0.8 | done | can't tell from luck |
| value_ev10 | 594 | 39.1 | 40.1 | $-373.59 | -6.3% | $626.41 | -1.3 | done | can't tell from luck |
| trend_filter | 733 | 49.8 | 50.7 | $-425.98 | -5.8% | $574.02 | -1.6 | done | can't tell from luck |
| value_ev5 | 878 | 41.0 | 41.8 | $-508.28 | -5.8% | $491.72 | -1.5 | done | can't tell from luck |
| momentum_15m_0.10pct | 1273 | 49.8 | 50.0 | $-516.19 | -4.1% | $483.81 | -1.4 | done | can't tell from luck |
| reversal_15m_0.10pct | 1273 | 50.2 | 51.6 | $-891.14 | -7.0% | $108.86 | -2.6 | done | losing for real |
| coinflip | 1829 | 50.0 | 50.8 | $-1000.86 | -5.5% | $-0.86 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 1074 | 49.1 | 51.8 | $-1026.20 | -9.6% | $-26.20 | -3.3 | done | losing for real |
| momentum_5m_0.00pct | 1829 | 49.6 | 51.5 | $-1347.87 | -7.4% | $-347.87 | -3.3 | done | losing for real |
| always_up | 1829 | 46.2 | 50.5 | $-2261.94 | -12.4% | $-1261.94 | -5.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2858 | 47.5 | 49.3 | $-2298.14 |
| ETH | 3166 | 48.0 | 48.8 | $-2060.95 |
| SOL | 3284 | 47.7 | 49.3 | $-2553.97 |
| XRP | 3310 | 48.5 | 49.2 | $-1882.17 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
