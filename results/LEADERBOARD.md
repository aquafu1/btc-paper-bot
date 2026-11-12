# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 12, 3:20 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 135 windows, 3386 settled trades, 57 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 238 | 62.6 | 53.1 | $+365.16 | +15.3% | $1365.16 | +2.6 | done | real edge? (z>=2) |
| reversal_15m_0.10pct | 324 | 57.1 | 52.2 | $+226.63 | +7.0% | $1226.63 | +1.3 | done | can't tell from luck |
| momentum_5m_0.00pct | 532 | 51.7 | 51.0 | $-159.48 | -3.0% | $840.52 | -0.7 | done | can't tell from luck |
| value_ev20 | 63 | 27.0 | 36.4 | $-173.77 | -27.6% | $826.23 | -1.8 | Sun 8:45 AM | too few trades (63/200) |
| coinflip | 532 | 51.7 | 51.0 | $-175.27 | -3.3% | $824.73 | -0.8 | done | can't tell from luck |
| value_ev10 | 177 | 36.7 | 40.4 | $-233.58 | -13.2% | $766.42 | -1.5 | Thu 7:45 AM | too few trades (177/200) |
| trend_filter | 171 | 40.4 | 48.9 | $-351.43 | -20.6% | $648.57 | -2.7 | Thu 9:15 AM | too few trades (171/200) |
| value_ev5 | 255 | 37.6 | 42.0 | $-363.94 | -14.3% | $636.06 | -2.0 | done | losing for real |
| momentum_15m_0.10pct | 324 | 42.9 | 50.0 | $-543.92 | -16.8% | $456.08 | -3.1 | done | losing for real |
| always_up | 532 | 46.6 | 50.2 | $-604.38 | -11.4% | $395.62 | -2.7 | done | losing for real |
| momentum_60m_0.30pct | 238 | 37.4 | 49.1 | $-617.49 | -25.9% | $382.51 | -4.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 725 | 45.2 | 49.5 | $-821.92 |
| ETH | 840 | 44.8 | 48.7 | $-1010.89 |
| SOL | 894 | 48.8 | 48.7 | $-551.15 |
| XRP | 927 | 50.4 | 49.0 | $-247.51 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
