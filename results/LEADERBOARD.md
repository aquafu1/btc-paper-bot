# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 13, 6:15 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 233 windows, 6089 settled trades, 48 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 597 | 55.9 | 52.6 | $+180.48 | +3.0% | $1180.48 | +0.8 | done | can't tell from luck |
| reversal_60m_0.30pct | 478 | 54.0 | 52.4 | $-24.57 | -0.5% | $975.43 | -0.1 | done | can't tell from luck |
| value_ev20 | 113 | 34.5 | 36.6 | $-110.27 | -9.8% | $889.73 | -0.8 | Sun 6:30 AM | too few trades (113/200) |
| value_ev10 | 299 | 37.8 | 40.8 | $-326.93 | -10.9% | $673.07 | -1.6 | done | can't tell from luck |
| trend_filter | 321 | 45.2 | 50.1 | $-436.22 | -13.6% | $563.78 | -2.5 | done | losing for real |
| value_ev5 | 434 | 39.6 | 42.5 | $-454.49 | -10.5% | $545.51 | -1.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 478 | 46.0 | 49.8 | $-548.08 | -11.5% | $451.92 | -2.5 | done | losing for real |
| coinflip | 924 | 49.7 | 50.9 | $-594.83 | -6.4% | $405.17 | -2.0 | done | losing for real |
| momentum_5m_0.00pct | 924 | 50.0 | 51.5 | $-618.29 | -6.7% | $381.71 | -2.1 | done | losing for real |
| momentum_15m_0.10pct | 597 | 44.1 | 49.6 | $-878.95 | -14.7% | $121.05 | -3.6 | done | losing for real |
| always_up | 924 | 47.5 | 50.4 | $-906.78 | -9.8% | $93.22 | -3.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1364 | 46.5 | 49.7 | $-1369.29 |
| ETH | 1515 | 46.8 | 49.0 | $-1446.09 |
| SOL | 1573 | 48.1 | 49.3 | $-1247.37 |
| XRP | 1637 | 49.2 | 49.1 | $-656.18 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
