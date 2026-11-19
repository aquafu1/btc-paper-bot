# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 19, 10:00 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 824 windows, 22624 settled trades, 62 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 419 | 33.4 | 34.9 | $-360.80 | -8.6% | $639.20 | -1.3 | done | can't tell from luck |
| momentum_60m_0.30pct | 1894 | 50.1 | 49.7 | $-789.00 | -4.2% | $211.00 | -1.8 | done | can't tell from luck |
| value_ev10 | 1037 | 37.5 | 39.1 | $-796.63 | -7.7% | $203.37 | -2.0 | done | losing for real |
| reversal_15m_0.10pct | 2307 | 50.8 | 50.6 | $-877.39 | -3.8% | $122.61 | -1.8 | done | can't tell from luck |
| trend_filter | 1333 | 50.0 | 50.9 | $-900.38 | -6.8% | $99.62 | -2.5 | done | losing for real |
| value_ev5 | 1569 | 39.8 | 41.1 | $-1060.83 | -6.8% | $-60.83 | -2.3 | done | losing for real |
| reversal_60m_0.30pct | 1894 | 49.9 | 51.1 | $-1362.43 | -7.2% | $-362.43 | -3.2 | done | losing for real |
| momentum_15m_0.10pct | 2307 | 49.2 | 50.3 | $-1397.30 | -6.1% | $-397.30 | -2.9 | done | losing for real |
| momentum_5m_0.00pct | 3288 | 51.3 | 51.7 | $-1491.34 | -4.5% | $-491.34 | -2.7 | done | losing for real |
| coinflip | 3288 | 50.1 | 50.3 | $-1507.05 | -4.6% | $-507.05 | -2.6 | done | losing for real |
| always_up | 3288 | 47.4 | 49.6 | $-2925.88 | -8.9% | $-1925.88 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5135 | 48.1 | 49.1 | $-3176.71 |
| ETH | 5630 | 48.0 | 48.5 | $-3797.49 |
| SOL | 5901 | 48.2 | 48.6 | $-3340.98 |
| XRP | 5958 | 48.5 | 48.5 | $-3153.84 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
