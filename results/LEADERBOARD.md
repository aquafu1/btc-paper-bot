# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 12, 7:30 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 190 windows, 4850 settled trades, 63 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 472 | 57.8 | 52.4 | $+339.08 | +7.2% | $1339.08 | +1.6 | done | can't tell from luck |
| reversal_60m_0.30pct | 355 | 59.7 | 53.1 | $+335.29 | +9.4% | $1335.29 | +1.9 | done | can't tell from luck |
| value_ev20 | 92 | 32.6 | 36.9 | $-168.58 | -18.3% | $831.42 | -1.5 | Sun 8:30 AM | too few trades (92/200) |
| momentum_5m_0.00pct | 752 | 51.7 | 51.4 | $-254.29 | -3.4% | $745.71 | -1.0 | done | can't tell from luck |
| value_ev10 | 244 | 36.9 | 40.8 | $-353.19 | -14.5% | $646.81 | -2.0 | done | can't tell from luck |
| coinflip | 752 | 50.3 | 50.9 | $-430.97 | -5.7% | $569.03 | -1.6 | done | can't tell from luck |
| trend_filter | 243 | 41.6 | 49.4 | $-457.37 | -18.8% | $542.63 | -2.9 | done | losing for real |
| value_ev5 | 361 | 39.1 | 42.6 | $-460.29 | -12.8% | $539.71 | -2.2 | done | losing for real |
| momentum_60m_0.30pct | 355 | 40.3 | 49.0 | $-758.37 | -21.4% | $241.63 | -4.1 | done | losing for real |
| momentum_15m_0.10pct | 472 | 42.2 | 49.7 | $-873.22 | -18.5% | $126.78 | -4.1 | done | losing for real |
| always_up | 752 | 46.1 | 50.2 | $-941.43 | -12.5% | $58.57 | -3.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1062 | 46.0 | 49.5 | $-1092.81 |
| ETH | 1208 | 46.0 | 48.8 | $-1346.13 |
| SOL | 1257 | 47.8 | 49.1 | $-1058.52 |
| XRP | 1323 | 49.7 | 49.2 | $-525.87 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
