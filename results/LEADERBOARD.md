# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 12, 4:00 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 138 windows, 3470 settled trades, 40 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 241 | 62.7 | 53.1 | $+373.39 | +15.5% | $1373.39 | +2.6 | done | real edge? (z>=2) |
| reversal_15m_0.10pct | 333 | 57.1 | 52.1 | $+231.39 | +6.9% | $1231.39 | +1.3 | done | can't tell from luck |
| value_ev20 | 67 | 31.3 | 37.0 | $-135.47 | -20.2% | $864.53 | -1.4 | Sun 4:15 AM | too few trades (67/200) |
| momentum_5m_0.00pct | 544 | 52.0 | 51.1 | $-143.29 | -2.6% | $856.71 | -0.6 | done | can't tell from luck |
| coinflip | 544 | 51.5 | 51.0 | $-209.73 | -3.9% | $790.27 | -0.9 | done | can't tell from luck |
| value_ev10 | 184 | 37.5 | 40.6 | $-225.28 | -12.2% | $774.72 | -1.4 | Thu 7:00 AM | too few trades (184/200) |
| value_ev5 | 264 | 38.3 | 42.2 | $-358.33 | -13.6% | $641.67 | -2.0 | done | can't tell from luck |
| trend_filter | 175 | 40.0 | 49.1 | $-374.41 | -21.4% | $625.59 | -2.8 | Thu 9:00 AM | too few trades (175/200) |
| momentum_15m_0.10pct | 333 | 42.9 | 50.1 | $-566.81 | -17.0% | $433.19 | -3.2 | done | losing for real |
| always_up | 544 | 47.1 | 50.2 | $-578.98 | -10.6% | $421.02 | -2.5 | done | losing for real |
| momentum_60m_0.30pct | 241 | 37.3 | 49.1 | $-630.47 | -26.2% | $369.53 | -4.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 745 | 45.6 | 49.6 | $-801.64 |
| ETH | 861 | 44.8 | 48.8 | $-1041.51 |
| SOL | 914 | 48.9 | 48.7 | $-548.14 |
| XRP | 950 | 50.6 | 49.1 | $-226.69 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
