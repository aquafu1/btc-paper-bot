# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 16, 1:05 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 548 windows, 15213 settled trades, 47 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1303 | 51.5 | 49.7 | $-188.15 | -1.4% | $811.85 | -0.5 | done | can't tell from luck |
| value_ev20 | 299 | 33.1 | 35.2 | $-344.01 | -11.5% | $655.99 | -1.5 | done | can't tell from luck |
| trend_filter | 888 | 50.7 | 51.0 | $-459.63 | -5.2% | $540.37 | -1.6 | done | can't tell from luck |
| momentum_15m_0.10pct | 1538 | 49.7 | 49.8 | $-698.38 | -4.5% | $301.62 | -1.8 | done | can't tell from luck |
| value_ev10 | 719 | 36.9 | 39.4 | $-791.10 | -11.0% | $208.90 | -2.5 | done | losing for real |
| value_ev5 | 1070 | 39.3 | 41.2 | $-978.20 | -9.1% | $21.80 | -2.6 | done | losing for real |
| reversal_15m_0.10pct | 1538 | 50.3 | 51.2 | $-1054.47 | -6.9% | $-54.47 | -2.8 | done | losing for real |
| coinflip | 2185 | 49.8 | 50.5 | $-1289.28 | -5.9% | $-289.28 | -2.8 | done | losing for real |
| reversal_60m_0.30pct | 1303 | 48.5 | 51.2 | $-1346.30 | -10.3% | $-346.30 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 2185 | 50.1 | 51.8 | $-1626.28 | -7.4% | $-626.28 | -3.6 | done | losing for real |
| always_up | 2185 | 46.7 | 50.0 | $-2440.13 | -11.2% | $-1440.13 | -5.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3441 | 47.4 | 49.2 | $-2856.81 |
| ETH | 3792 | 47.8 | 48.6 | $-2782.49 |
| SOL | 3967 | 47.6 | 48.7 | $-3123.76 |
| XRP | 4013 | 48.4 | 48.6 | $-2452.89 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
