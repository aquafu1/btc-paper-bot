# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 12, 7:45 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 153 windows, 3868 settled trades, 56 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 275 | 60.0 | 53.1 | $+287.36 | +10.4% | $1287.36 | +1.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 372 | 57.3 | 52.3 | $+249.94 | +6.7% | $1249.94 | +1.4 | done | can't tell from luck |
| momentum_5m_0.00pct | 604 | 52.8 | 51.3 | $-86.81 | -1.4% | $913.19 | -0.4 | done | can't tell from luck |
| value_ev20 | 74 | 32.4 | 37.2 | $-143.54 | -19.4% | $856.46 | -1.4 | Sun 4:15 AM | too few trades (74/200) |
| coinflip | 604 | 51.2 | 50.9 | $-254.62 | -4.2% | $745.38 | -1.1 | done | can't tell from luck |
| value_ev10 | 200 | 37.0 | 40.8 | $-285.12 | -14.3% | $714.88 | -1.8 | done | can't tell from luck |
| trend_filter | 196 | 41.8 | 49.2 | $-358.62 | -18.3% | $641.38 | -2.6 | Thu 8:30 AM | too few trades (196/200) |
| value_ev5 | 292 | 38.4 | 42.4 | $-411.94 | -14.1% | $588.06 | -2.2 | done | losing for real |
| momentum_60m_0.30pct | 275 | 40.0 | 49.3 | $-591.30 | -21.5% | $408.70 | -3.6 | done | losing for real |
| momentum_15m_0.10pct | 372 | 42.7 | 50.0 | $-649.34 | -17.5% | $350.66 | -3.4 | done | losing for real |
| always_up | 604 | 46.0 | 50.1 | $-756.52 | -12.5% | $243.48 | -3.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 831 | 46.1 | 49.7 | $-838.71 |
| ETH | 956 | 45.6 | 48.9 | $-1048.35 |
| SOL | 1020 | 48.2 | 48.9 | $-767.30 |
| XRP | 1061 | 50.3 | 49.1 | $-346.15 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
