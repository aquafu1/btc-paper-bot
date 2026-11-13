# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 12, 6:45 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 187 windows, 4756 settled trades, 63 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 348 | 59.8 | 53.0 | $+341.49 | +9.8% | $1341.49 | +2.0 | done | can't tell from luck |
| reversal_15m_0.10pct | 462 | 57.4 | 52.4 | $+294.69 | +6.4% | $1294.69 | +1.4 | done | can't tell from luck |
| value_ev20 | 89 | 33.7 | 36.7 | $-138.58 | -15.6% | $861.42 | -1.2 | Sun 10:30 AM | too few trades (89/200) |
| momentum_5m_0.00pct | 740 | 51.8 | 51.4 | $-243.78 | -3.3% | $756.22 | -0.9 | done | can't tell from luck |
| value_ev10 | 239 | 37.2 | 40.7 | $-325.34 | -13.6% | $674.66 | -1.8 | done | can't tell from luck |
| coinflip | 740 | 50.5 | 50.9 | $-378.13 | -5.1% | $621.87 | -1.4 | done | can't tell from luck |
| trend_filter | 237 | 41.4 | 49.4 | $-454.73 | -19.2% | $545.27 | -3.0 | done | losing for real |
| value_ev5 | 351 | 38.7 | 42.5 | $-460.83 | -13.1% | $539.17 | -2.2 | done | losing for real |
| momentum_60m_0.30pct | 348 | 40.2 | 49.1 | $-746.81 | -21.5% | $253.19 | -4.1 | done | losing for real |
| momentum_15m_0.10pct | 462 | 42.6 | 49.7 | $-807.18 | -17.5% | $192.82 | -3.8 | done | losing for real |
| always_up | 740 | 46.4 | 50.1 | $-885.23 | -12.0% | $114.77 | -3.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1041 | 45.9 | 49.5 | $-1061.45 |
| ETH | 1181 | 46.1 | 48.8 | $-1292.13 |
| SOL | 1235 | 47.9 | 49.1 | $-1008.92 |
| XRP | 1299 | 50.0 | 49.1 | $-441.93 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
