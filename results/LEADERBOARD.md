# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 17, 10:35 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 682 windows, 18873 settled trades, 36 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 356 | 34.3 | 35.0 | $-234.96 | -6.6% | $765.04 | -0.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 1599 | 50.3 | 49.5 | $-438.83 | -2.7% | $561.17 | -1.1 | done | can't tell from luck |
| value_ev10 | 872 | 38.4 | 39.2 | $-516.96 | -5.9% | $483.04 | -1.4 | done | can't tell from luck |
| trend_filter | 1098 | 50.4 | 50.9 | $-571.27 | -5.2% | $428.73 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 1938 | 51.5 | 50.9 | $-606.06 | -3.1% | $393.94 | -1.4 | done | can't tell from luck |
| value_ev5 | 1310 | 40.6 | 41.1 | $-674.28 | -5.1% | $325.72 | -1.6 | done | can't tell from luck |
| coinflip | 2721 | 50.1 | 50.4 | $-1218.13 | -4.5% | $-218.13 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 1599 | 49.7 | 51.4 | $-1238.41 | -7.7% | $-238.41 | -3.2 | done | losing for real |
| momentum_15m_0.10pct | 1938 | 48.5 | 49.9 | $-1296.03 | -6.7% | $-296.03 | -2.9 | done | losing for real |
| momentum_5m_0.00pct | 2721 | 50.8 | 51.8 | $-1462.81 | -5.4% | $-462.81 | -2.9 | done | losing for real |
| always_up | 2721 | 47.3 | 49.7 | $-2409.29 | -8.9% | $-1409.29 | -4.6 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4290 | 48.3 | 49.2 | $-2534.83 |
| ETH | 4701 | 48.3 | 48.6 | $-2807.72 |
| SOL | 4922 | 48.1 | 48.6 | $-2966.88 |
| XRP | 4960 | 48.5 | 48.4 | $-2357.60 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
