# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 12, 3:30 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 136 windows, 3404 settled trades, 66 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 238 | 62.6 | 53.1 | $+365.16 | +15.3% | $1365.16 | +2.6 | done | real edge? (z>=2) |
| reversal_15m_0.10pct | 325 | 57.2 | 52.2 | $+233.09 | +7.2% | $1233.09 | +1.3 | done | can't tell from luck |
| momentum_5m_0.00pct | 536 | 51.9 | 51.1 | $-149.69 | -2.8% | $850.31 | -0.7 | done | can't tell from luck |
| value_ev20 | 63 | 27.0 | 36.4 | $-173.77 | -27.6% | $826.23 | -1.8 | Sun 9:45 AM | too few trades (63/200) |
| coinflip | 536 | 51.7 | 51.0 | $-182.88 | -3.4% | $817.12 | -0.8 | done | can't tell from luck |
| value_ev10 | 179 | 36.3 | 40.4 | $-253.58 | -14.2% | $746.42 | -1.6 | Thu 7:30 AM | too few trades (179/200) |
| trend_filter | 171 | 40.4 | 48.9 | $-351.43 | -20.6% | $648.57 | -2.7 | Thu 9:30 AM | too few trades (171/200) |
| value_ev5 | 257 | 37.4 | 42.0 | $-383.94 | -14.9% | $616.06 | -2.1 | done | losing for real |
| momentum_15m_0.10pct | 325 | 42.8 | 50.0 | $-553.92 | -17.0% | $446.08 | -3.1 | done | losing for real |
| momentum_60m_0.30pct | 238 | 37.4 | 49.1 | $-617.49 | -25.9% | $382.51 | -4.1 | done | losing for real |
| always_up | 536 | 46.3 | 50.1 | $-644.38 | -12.0% | $355.62 | -2.9 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 728 | 45.2 | 49.5 | $-835.97 |
| ETH | 843 | 44.7 | 48.7 | $-1022.96 |
| SOL | 899 | 48.7 | 48.7 | $-569.30 |
| XRP | 934 | 50.2 | 49.0 | $-284.59 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
