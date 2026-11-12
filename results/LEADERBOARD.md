# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 12, 2:35 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 132 windows, 3326 settled trades, 39 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 237 | 62.4 | 53.1 | $+357.74 | +15.1% | $1357.74 | +2.5 | done | real edge? (z>=2) |
| reversal_15m_0.10pct | 319 | 57.4 | 52.2 | $+236.58 | +7.4% | $1236.58 | +1.4 | done | can't tell from luck |
| momentum_5m_0.00pct | 520 | 52.1 | 50.9 | $-104.47 | -2.0% | $895.53 | -0.5 | done | can't tell from luck |
| value_ev20 | 61 | 26.2 | 36.4 | $-182.65 | -29.9% | $817.35 | -1.9 | Sun 10:15 AM | too few trades (61/200) |
| coinflip | 520 | 51.5 | 51.1 | $-203.81 | -3.9% | $796.19 | -0.9 | done | can't tell from luck |
| value_ev10 | 174 | 36.8 | 40.5 | $-232.46 | -13.4% | $767.54 | -1.5 | Thu 7:30 AM | too few trades (174/200) |
| trend_filter | 170 | 40.6 | 48.9 | $-341.43 | -20.1% | $658.57 | -2.6 | Thu 8:30 AM | too few trades (170/200) |
| value_ev5 | 249 | 36.9 | 42.0 | $-394.45 | -15.8% | $605.55 | -2.2 | done | losing for real |
| momentum_15m_0.10pct | 319 | 42.6 | 50.0 | $-561.26 | -17.6% | $438.74 | -3.2 | done | losing for real |
| momentum_60m_0.30pct | 237 | 37.6 | 49.1 | $-607.49 | -25.6% | $392.51 | -4.0 | done | losing for real |
| always_up | 520 | 46.2 | 50.3 | $-657.75 | -12.6% | $342.25 | -3.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 712 | 45.1 | 49.6 | $-834.97 |
| ETH | 823 | 45.0 | 48.7 | $-958.03 |
| SOL | 882 | 48.6 | 48.7 | $-571.58 |
| XRP | 909 | 50.2 | 49.1 | $-326.86 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
