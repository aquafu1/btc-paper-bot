# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 12, 12:35 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 172 windows, 4407 settled trades, 42 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 323 | 60.4 | 53.1 | $+353.96 | +11.0% | $1353.96 | +2.1 | done | real edge? (z>=2) |
| reversal_15m_0.10pct | 433 | 58.2 | 52.6 | $+339.79 | +7.8% | $1339.79 | +1.7 | done | can't tell from luck |
| value_ev20 | 82 | 34.1 | 37.1 | $-121.99 | -14.9% | $878.01 | -1.1 | Sun 5:15 AM | too few trades (82/200) |
| momentum_5m_0.00pct | 680 | 51.2 | 51.1 | $-268.50 | -3.9% | $731.50 | -1.1 | done | can't tell from luck |
| value_ev10 | 222 | 37.4 | 40.8 | $-291.47 | -13.1% | $708.53 | -1.7 | done | can't tell from luck |
| value_ev5 | 328 | 38.7 | 42.5 | $-432.86 | -13.2% | $567.14 | -2.1 | done | losing for real |
| trend_filter | 223 | 40.4 | 49.1 | $-452.69 | -20.3% | $547.31 | -3.0 | done | losing for real |
| coinflip | 680 | 49.6 | 50.9 | $-476.74 | -7.0% | $523.26 | -1.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 323 | 39.6 | 49.0 | $-716.60 | -22.2% | $283.40 | -4.0 | done | losing for real |
| always_up | 680 | 46.6 | 50.1 | $-765.65 | -11.3% | $234.35 | -3.0 | done | losing for real |
| momentum_15m_0.10pct | 433 | 41.8 | 49.6 | $-815.07 | -18.8% | $184.93 | -4.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 956 | 45.8 | 49.5 | $-940.79 |
| ETH | 1099 | 45.7 | 48.9 | $-1248.93 |
| SOL | 1156 | 47.8 | 49.0 | $-966.04 |
| XRP | 1196 | 49.7 | 49.0 | $-492.07 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
