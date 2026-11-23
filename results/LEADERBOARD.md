# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 22, 6:00 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1144 windows, 31611 settled trades, 51 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 610 | 34.4 | 35.2 | $-412.50 | -6.8% | $587.50 | -1.3 | done | can't tell from luck |
| reversal_15m_0.10pct | 3177 | 50.9 | 50.4 | $-986.31 | -3.1% | $13.69 | -1.8 | done | can't tell from luck |
| value_ev10 | 1485 | 38.0 | 39.2 | $-986.39 | -6.6% | $13.61 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 2668 | 49.7 | 49.5 | $-1174.93 | -4.4% | $-174.93 | -2.3 | done | losing for real |
| value_ev5 | 2244 | 40.0 | 41.1 | $-1369.10 | -6.1% | $-369.10 | -2.5 | done | losing for real |
| trend_filter | 1878 | 49.0 | 50.5 | $-1506.54 | -8.0% | $-506.54 | -3.6 | done | losing for real |
| reversal_60m_0.30pct | 2668 | 50.3 | 51.1 | $-1660.98 | -6.2% | $-660.98 | -3.3 | done | losing for real |
| coinflip | 4568 | 50.3 | 50.2 | $-1888.49 | -4.1% | $-888.49 | -2.8 | done | losing for real |
| momentum_15m_0.10pct | 3177 | 49.1 | 50.2 | $-1984.61 | -6.2% | $-984.61 | -3.6 | done | losing for real |
| momentum_5m_0.00pct | 4568 | 50.2 | 51.4 | $-2854.01 | -6.2% | $-1854.01 | -4.4 | done | losing for real |
| always_up | 4568 | 47.9 | 49.4 | $-3366.55 | -7.4% | $-2366.55 | -5.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7243 | 48.3 | 49.0 | $-3825.51 |
| ETH | 7833 | 48.1 | 48.4 | $-4680.18 |
| SOL | 8230 | 48.1 | 48.4 | $-4608.46 |
| XRP | 8305 | 48.1 | 48.2 | $-5076.25 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
