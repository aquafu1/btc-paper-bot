# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 20, 10:20 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 969 windows, 26885 settled trades, 39 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 496 | 34.7 | 34.8 | $-219.50 | -4.4% | $780.50 | -0.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 2744 | 51.3 | 50.5 | $-709.01 | -2.6% | $290.99 | -1.4 | done | can't tell from luck |
| value_ev10 | 1228 | 37.9 | 39.1 | $-734.80 | -6.0% | $265.20 | -1.7 | done | can't tell from luck |
| momentum_60m_0.30pct | 2295 | 50.3 | 49.8 | $-843.42 | -3.7% | $156.58 | -1.8 | done | can't tell from luck |
| trend_filter | 1608 | 50.0 | 50.9 | $-1067.85 | -6.6% | $-67.85 | -2.7 | done | losing for real |
| value_ev5 | 1862 | 39.8 | 40.9 | $-1091.73 | -5.9% | $-91.73 | -2.1 | done | losing for real |
| reversal_60m_0.30pct | 2295 | 49.7 | 50.9 | $-1677.28 | -7.3% | $-677.28 | -3.6 | done | losing for real |
| coinflip | 3871 | 50.2 | 50.3 | $-1784.78 | -4.6% | $-784.78 | -2.9 | done | losing for real |
| momentum_15m_0.10pct | 2744 | 48.7 | 50.3 | $-1969.98 | -7.2% | $-969.98 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 3871 | 50.8 | 51.6 | $-2040.82 | -5.3% | $-1040.82 | -3.4 | done | losing for real |
| always_up | 3871 | 46.8 | 49.6 | $-3867.42 | -10.0% | $-2867.42 | -6.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6125 | 48.2 | 49.1 | $-3456.46 |
| ETH | 6682 | 48.0 | 48.5 | $-4237.28 |
| SOL | 7016 | 48.2 | 48.6 | $-3922.51 |
| XRP | 7062 | 48.1 | 48.4 | $-4390.33 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
