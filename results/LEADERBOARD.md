# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 13, 6:30 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 234 windows, 6106 settled trades, 55 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 597 | 55.9 | 52.6 | $+180.48 | +3.0% | $1180.48 | +0.8 | done | can't tell from luck |
| reversal_60m_0.30pct | 479 | 53.9 | 52.3 | $-34.57 | -0.7% | $965.43 | -0.2 | done | can't tell from luck |
| value_ev20 | 113 | 34.5 | 36.6 | $-110.27 | -9.8% | $889.73 | -0.8 | Sun 7:00 AM | too few trades (113/200) |
| value_ev10 | 300 | 37.7 | 40.7 | $-336.93 | -11.2% | $663.07 | -1.7 | done | can't tell from luck |
| trend_filter | 321 | 45.2 | 50.1 | $-436.22 | -13.6% | $563.78 | -2.5 | done | losing for real |
| value_ev5 | 436 | 39.4 | 42.5 | $-474.49 | -10.9% | $525.51 | -2.0 | done | losing for real |
| momentum_60m_0.30pct | 479 | 46.1 | 49.8 | $-543.00 | -11.3% | $457.00 | -2.5 | done | losing for real |
| coinflip | 928 | 49.6 | 50.9 | $-620.45 | -6.7% | $379.55 | -2.1 | done | losing for real |
| momentum_5m_0.00pct | 928 | 49.8 | 51.4 | $-658.29 | -7.1% | $341.71 | -2.2 | done | losing for real |
| momentum_15m_0.10pct | 597 | 44.1 | 49.6 | $-878.95 | -14.7% | $121.05 | -3.6 | done | losing for real |
| always_up | 928 | 47.7 | 50.4 | $-887.31 | -9.6% | $112.69 | -3.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1367 | 46.5 | 49.6 | $-1384.28 |
| ETH | 1520 | 46.8 | 49.0 | $-1465.93 |
| SOL | 1577 | 48.0 | 49.3 | $-1272.36 |
| XRP | 1642 | 49.1 | 49.1 | $-677.43 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
