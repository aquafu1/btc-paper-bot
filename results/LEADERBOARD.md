# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 12, 7:30 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 152 windows, 3838 settled trades, 57 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 271 | 59.8 | 53.0 | $+275.93 | +10.2% | $1275.93 | +1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 368 | 57.1 | 52.3 | $+238.51 | +6.5% | $1238.51 | +1.3 | done | can't tell from luck |
| momentum_5m_0.00pct | 600 | 52.7 | 51.3 | $-98.23 | -1.6% | $901.77 | -0.4 | done | can't tell from luck |
| value_ev20 | 74 | 32.4 | 37.2 | $-143.54 | -19.4% | $856.46 | -1.4 | Sun 3:30 AM | too few trades (74/200) |
| coinflip | 600 | 51.2 | 50.9 | $-249.85 | -4.2% | $750.15 | -1.1 | done | can't tell from luck |
| value_ev10 | 199 | 36.7 | 40.7 | $-292.43 | -14.7% | $707.57 | -1.8 | Thu 7:30 AM | too few trades (199/200) |
| trend_filter | 196 | 41.8 | 49.2 | $-358.62 | -18.3% | $641.38 | -2.6 | Thu 8:15 AM | too few trades (196/200) |
| value_ev5 | 291 | 38.1 | 42.4 | $-419.24 | -14.4% | $580.76 | -2.2 | done | losing for real |
| momentum_60m_0.30pct | 271 | 40.2 | 49.4 | $-572.87 | -21.1% | $427.13 | -3.5 | done | losing for real |
| momentum_15m_0.10pct | 368 | 42.9 | 50.0 | $-630.91 | -17.1% | $369.09 | -3.4 | done | losing for real |
| always_up | 600 | 45.8 | 50.0 | $-767.95 | -12.8% | $232.05 | -3.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 822 | 45.7 | 49.6 | $-869.86 |
| ETH | 949 | 45.5 | 48.8 | $-1043.15 |
| SOL | 1013 | 48.4 | 48.8 | $-740.45 |
| XRP | 1054 | 50.2 | 49.1 | $-365.76 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
