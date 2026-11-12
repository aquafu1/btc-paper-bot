# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 12, 12:45 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 173 windows, 4430 settled trades, 55 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 433 | 58.2 | 52.6 | $+339.79 | +7.8% | $1339.79 | +1.7 | done | can't tell from luck |
| reversal_60m_0.30pct | 327 | 59.6 | 53.1 | $+313.96 | +9.6% | $1313.96 | +1.9 | done | can't tell from luck |
| value_ev20 | 82 | 34.1 | 37.1 | $-121.99 | -14.9% | $878.01 | -1.1 | Sun 5:45 AM | too few trades (82/200) |
| momentum_5m_0.00pct | 684 | 51.3 | 51.1 | $-253.50 | -3.7% | $746.50 | -1.0 | done | can't tell from luck |
| value_ev10 | 222 | 37.4 | 40.8 | $-291.47 | -13.1% | $708.53 | -1.7 | done | can't tell from luck |
| trend_filter | 226 | 41.2 | 49.1 | $-427.69 | -18.9% | $572.31 | -2.8 | done | losing for real |
| value_ev5 | 328 | 38.7 | 42.5 | $-432.86 | -13.2% | $567.14 | -2.1 | done | losing for real |
| coinflip | 684 | 49.6 | 50.9 | $-479.83 | -7.0% | $520.17 | -1.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 327 | 40.4 | 49.1 | $-683.35 | -20.9% | $316.65 | -3.8 | done | losing for real |
| always_up | 684 | 46.9 | 50.1 | $-732.40 | -10.7% | $267.60 | -2.9 | done | losing for real |
| momentum_15m_0.10pct | 433 | 41.8 | 49.6 | $-815.07 | -18.8% | $184.93 | -4.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 962 | 46.0 | 49.5 | $-904.29 |
| ETH | 1105 | 45.9 | 48.9 | $-1220.88 |
| SOL | 1161 | 47.7 | 49.0 | $-979.55 |
| XRP | 1202 | 49.8 | 49.0 | $-479.70 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
