# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 12, 2:50 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 133 windows, 3345 settled trades, 41 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 237 | 62.4 | 53.1 | $+357.74 | +15.1% | $1357.74 | +2.5 | done | real edge? (z>=2) |
| reversal_15m_0.10pct | 320 | 57.2 | 52.2 | $+226.58 | +7.1% | $1226.58 | +1.3 | done | can't tell from luck |
| momentum_5m_0.00pct | 524 | 52.5 | 50.9 | $-79.48 | -1.5% | $920.52 | -0.4 | done | can't tell from luck |
| value_ev20 | 62 | 25.8 | 36.4 | $-192.65 | -31.1% | $807.35 | -2.1 | Sun 9:00 AM | too few trades (62/200) |
| coinflip | 524 | 51.5 | 51.1 | $-210.71 | -4.0% | $789.29 | -1.0 | done | can't tell from luck |
| value_ev10 | 176 | 36.4 | 40.5 | $-252.46 | -14.3% | $747.54 | -1.6 | Thu 7:30 AM | too few trades (176/200) |
| trend_filter | 170 | 40.6 | 48.9 | $-341.43 | -20.1% | $658.57 | -2.6 | Thu 8:45 AM | too few trades (170/200) |
| value_ev5 | 251 | 36.7 | 42.0 | $-414.45 | -16.5% | $585.55 | -2.3 | done | losing for real |
| momentum_15m_0.10pct | 320 | 42.8 | 50.0 | $-554.16 | -17.3% | $445.84 | -3.2 | done | losing for real |
| momentum_60m_0.30pct | 237 | 37.6 | 49.1 | $-607.49 | -25.6% | $392.51 | -4.0 | done | losing for real |
| always_up | 524 | 45.8 | 50.2 | $-697.75 | -13.3% | $302.25 | -3.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 717 | 45.0 | 49.6 | $-852.57 |
| ETH | 829 | 44.8 | 48.7 | $-1003.24 |
| SOL | 887 | 48.6 | 48.7 | $-587.39 |
| XRP | 912 | 50.2 | 49.1 | $-323.07 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
