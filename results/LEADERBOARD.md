# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 12, 7:35 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 152 windows, 3854 settled trades, 41 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 273 | 59.7 | 53.0 | $+273.24 | +10.0% | $1273.24 | +1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 370 | 57.0 | 52.3 | $+235.81 | +6.4% | $1235.81 | +1.3 | done | can't tell from luck |
| momentum_5m_0.00pct | 602 | 52.7 | 51.3 | $-100.93 | -1.7% | $899.07 | -0.4 | done | can't tell from luck |
| value_ev20 | 74 | 32.4 | 37.2 | $-143.54 | -19.4% | $856.46 | -1.4 | Sun 4:15 AM | too few trades (74/200) |
| coinflip | 602 | 51.2 | 50.9 | $-252.54 | -4.2% | $747.46 | -1.1 | done | can't tell from luck |
| value_ev10 | 200 | 37.0 | 40.8 | $-285.12 | -14.3% | $714.88 | -1.8 | done | can't tell from luck |
| trend_filter | 196 | 41.8 | 49.2 | $-358.62 | -18.3% | $641.38 | -2.6 | Thu 8:30 AM | too few trades (196/200) |
| value_ev5 | 292 | 38.4 | 42.4 | $-411.94 | -14.1% | $588.06 | -2.2 | done | losing for real |
| momentum_60m_0.30pct | 273 | 40.3 | 49.3 | $-571.30 | -20.9% | $428.70 | -3.5 | done | losing for real |
| momentum_15m_0.10pct | 370 | 43.0 | 50.0 | $-629.34 | -17.0% | $370.66 | -3.3 | done | losing for real |
| always_up | 602 | 45.8 | 50.0 | $-770.64 | -12.8% | $229.36 | -3.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 831 | 46.1 | 49.7 | $-838.71 |
| ETH | 949 | 45.5 | 48.8 | $-1043.15 |
| SOL | 1020 | 48.2 | 48.9 | $-767.30 |
| XRP | 1054 | 50.2 | 49.1 | $-365.76 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
