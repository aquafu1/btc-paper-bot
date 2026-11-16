# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 16, 11:30 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 542 windows, 15014 settled trades, 71 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1285 | 51.5 | 49.8 | $-152.34 | -1.2% | $847.66 | -0.4 | done | can't tell from luck |
| value_ev20 | 287 | 33.8 | 35.5 | $-282.64 | -9.8% | $717.36 | -1.3 | done | can't tell from luck |
| trend_filter | 875 | 50.6 | 50.9 | $-425.56 | -4.9% | $574.44 | -1.5 | done | can't tell from luck |
| momentum_15m_0.10pct | 1524 | 49.7 | 49.7 | $-669.72 | -4.4% | $330.28 | -1.7 | done | can't tell from luck |
| value_ev10 | 704 | 37.2 | 39.7 | $-720.63 | -10.2% | $279.37 | -2.3 | done | losing for real |
| value_ev5 | 1050 | 39.4 | 41.4 | $-934.23 | -8.9% | $65.77 | -2.5 | done | losing for real |
| reversal_15m_0.10pct | 1524 | 50.3 | 51.4 | $-1064.54 | -7.0% | $-64.54 | -2.8 | done | losing for real |
| coinflip | 2160 | 49.8 | 50.6 | $-1275.31 | -5.9% | $-275.31 | -2.8 | done | losing for real |
| reversal_60m_0.30pct | 1285 | 48.5 | 51.3 | $-1319.77 | -10.3% | $-319.77 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 2160 | 50.0 | 51.7 | $-1552.75 | -7.2% | $-552.75 | -3.5 | done | losing for real |
| always_up | 2160 | 46.7 | 50.1 | $-2429.43 | -11.2% | $-1429.43 | -5.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3403 | 47.5 | 49.2 | $-2819.97 |
| ETH | 3748 | 47.9 | 48.6 | $-2660.23 |
| SOL | 3916 | 47.7 | 48.9 | $-3013.75 |
| XRP | 3947 | 48.5 | 48.8 | $-2332.97 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
