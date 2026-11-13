# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 12, 9:00 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 196 windows, 5027 settled trades, 79 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 490 | 58.6 | 52.6 | $+393.80 | +8.0% | $1393.80 | +1.9 | done | can't tell from luck |
| reversal_60m_0.30pct | 368 | 59.0 | 52.9 | $+292.94 | +8.0% | $1292.94 | +1.6 | done | can't tell from luck |
| value_ev20 | 96 | 31.2 | 37.1 | $-208.58 | -21.7% | $791.42 | -1.8 | Sun 6:45 AM | too few trades (96/200) |
| momentum_5m_0.00pct | 776 | 51.4 | 51.3 | $-324.60 | -4.2% | $675.40 | -1.2 | done | can't tell from luck |
| trend_filter | 251 | 42.2 | 49.5 | $-453.59 | -18.1% | $546.41 | -2.9 | done | losing for real |
| value_ev10 | 259 | 35.5 | 40.9 | $-461.04 | -17.8% | $538.96 | -2.5 | done | losing for real |
| coinflip | 776 | 50.3 | 51.0 | $-469.17 | -6.0% | $530.83 | -1.8 | done | can't tell from luck |
| value_ev5 | 377 | 37.9 | 42.6 | $-578.15 | -15.3% | $421.85 | -2.7 | done | losing for real |
| momentum_60m_0.30pct | 368 | 41.0 | 49.2 | $-754.69 | -20.5% | $245.31 | -4.0 | done | losing for real |
| momentum_15m_0.10pct | 490 | 41.4 | 49.6 | $-980.54 | -20.0% | $19.46 | -4.5 | done | losing for real |
| always_up | 776 | 46.0 | 50.2 | $-1015.47 | -13.1% | $-15.47 | -3.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1106 | 45.8 | 49.5 | $-1233.24 |
| ETH | 1249 | 46.0 | 48.9 | $-1442.78 |
| SOL | 1304 | 47.8 | 49.1 | $-1138.97 |
| XRP | 1368 | 49.1 | 49.2 | $-744.11 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
