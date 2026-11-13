# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 13, 6:05 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 232 windows, 6065 settled trades, 41 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 594 | 55.9 | 52.6 | $+169.71 | +2.9% | $1169.71 | +0.7 | done | can't tell from luck |
| reversal_60m_0.30pct | 476 | 53.8 | 52.4 | $-45.34 | -1.0% | $954.66 | -0.2 | done | can't tell from luck |
| value_ev20 | 113 | 34.5 | 36.6 | $-110.27 | -9.8% | $889.73 | -0.8 | Sun 6:00 AM | too few trades (113/200) |
| value_ev10 | 299 | 37.8 | 40.8 | $-326.93 | -10.9% | $673.07 | -1.6 | done | can't tell from luck |
| trend_filter | 319 | 45.5 | 50.1 | $-416.22 | -13.0% | $583.78 | -2.4 | done | losing for real |
| value_ev5 | 434 | 39.6 | 42.5 | $-454.49 | -10.5% | $545.51 | -1.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 476 | 46.2 | 49.7 | $-528.08 | -11.1% | $471.92 | -2.5 | done | losing for real |
| coinflip | 920 | 49.7 | 50.9 | $-595.60 | -6.5% | $404.40 | -2.0 | done | losing for real |
| momentum_5m_0.00pct | 920 | 50.0 | 51.5 | $-612.05 | -6.7% | $387.95 | -2.1 | done | losing for real |
| momentum_15m_0.10pct | 594 | 44.1 | 49.6 | $-866.26 | -14.6% | $133.74 | -3.6 | done | losing for real |
| always_up | 920 | 47.5 | 50.3 | $-900.55 | -9.8% | $99.45 | -3.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1361 | 46.4 | 49.7 | $-1372.21 |
| ETH | 1507 | 46.8 | 49.0 | $-1422.90 |
| SOL | 1565 | 48.1 | 49.3 | $-1232.88 |
| XRP | 1632 | 49.1 | 49.1 | $-658.10 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
