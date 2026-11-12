# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 12, 3:50 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 137 windows, 3451 settled trades, 37 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 241 | 62.7 | 53.1 | $+373.39 | +15.5% | $1373.39 | +2.6 | done | real edge? (z>=2) |
| reversal_15m_0.10pct | 330 | 57.6 | 52.2 | $+261.39 | +7.9% | $1261.39 | +1.5 | done | can't tell from luck |
| value_ev20 | 67 | 31.3 | 37.0 | $-135.47 | -20.2% | $864.53 | -1.4 | Sun 4:15 AM | too few trades (67/200) |
| momentum_5m_0.00pct | 541 | 51.8 | 51.1 | $-163.38 | -3.0% | $836.62 | -0.7 | done | can't tell from luck |
| coinflip | 541 | 51.6 | 51.1 | $-196.56 | -3.6% | $803.44 | -0.9 | done | can't tell from luck |
| value_ev10 | 183 | 37.7 | 40.6 | $-215.28 | -11.8% | $784.72 | -1.4 | Thu 7:15 AM | too few trades (183/200) |
| value_ev5 | 261 | 38.3 | 42.1 | $-345.63 | -13.2% | $654.37 | -1.9 | done | can't tell from luck |
| trend_filter | 175 | 40.0 | 49.1 | $-374.41 | -21.4% | $625.59 | -2.8 | Thu 9:00 AM | too few trades (175/200) |
| momentum_15m_0.10pct | 330 | 42.4 | 50.0 | $-586.90 | -17.8% | $413.10 | -3.3 | done | losing for real |
| always_up | 541 | 46.8 | 50.1 | $-599.07 | -11.1% | $400.93 | -2.6 | done | losing for real |
| momentum_60m_0.30pct | 241 | 37.3 | 49.1 | $-630.47 | -26.2% | $369.53 | -4.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 739 | 45.5 | 49.6 | $-810.87 |
| ETH | 854 | 44.8 | 48.8 | $-1019.35 |
| SOL | 908 | 48.8 | 48.7 | $-555.47 |
| XRP | 950 | 50.6 | 49.1 | $-226.69 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
