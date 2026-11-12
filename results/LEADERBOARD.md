# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 12, 7:05 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 150 windows, 3808 settled trades, 30 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 269 | 59.9 | 53.0 | $+275.86 | +10.3% | $1275.86 | +1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 367 | 56.9 | 52.3 | $+226.52 | +6.2% | $1226.52 | +1.2 | done | can't tell from luck |
| momentum_5m_0.00pct | 593 | 52.4 | 51.3 | $-126.77 | -2.1% | $873.23 | -0.5 | done | can't tell from luck |
| value_ev20 | 74 | 32.4 | 37.2 | $-143.54 | -19.4% | $856.46 | -1.4 | Sun 2:45 AM | too few trades (74/200) |
| coinflip | 593 | 51.1 | 50.9 | $-261.55 | -4.4% | $738.45 | -1.1 | done | can't tell from luck |
| value_ev10 | 199 | 36.7 | 40.7 | $-292.43 | -14.7% | $707.57 | -1.8 | Thu 7:15 AM | too few trades (199/200) |
| trend_filter | 194 | 41.8 | 49.2 | $-359.11 | -18.5% | $640.89 | -2.6 | Thu 8:15 AM | too few trades (194/200) |
| value_ev5 | 290 | 37.9 | 42.4 | $-429.73 | -14.8% | $570.27 | -2.3 | done | losing for real |
| momentum_60m_0.30pct | 269 | 40.1 | 49.3 | $-573.36 | -21.3% | $426.64 | -3.5 | done | losing for real |
| momentum_15m_0.10pct | 367 | 43.1 | 50.0 | $-620.91 | -16.9% | $379.09 | -3.3 | done | losing for real |
| always_up | 593 | 46.2 | 50.0 | $-718.02 | -12.1% | $281.98 | -3.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 815 | 45.8 | 49.6 | $-858.75 |
| ETH | 940 | 45.4 | 48.8 | $-1051.28 |
| SOL | 1007 | 48.4 | 48.8 | $-741.91 |
| XRP | 1046 | 50.2 | 49.1 | $-371.10 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
