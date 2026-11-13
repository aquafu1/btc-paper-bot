# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 13, 12:35 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 210 windows, 5458 settled trades, 59 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 537 | 57.5 | 52.7 | $+327.21 | +6.1% | $1327.21 | +1.5 | done | can't tell from luck |
| reversal_60m_0.30pct | 418 | 55.7 | 52.7 | $+119.98 | +2.9% | $1119.98 | +0.6 | done | can't tell from luck |
| value_ev20 | 104 | 33.7 | 36.9 | $-137.53 | -13.2% | $862.47 | -1.1 | Sun 5:00 AM | too few trades (104/200) |
| value_ev10 | 271 | 36.9 | 40.8 | $-360.93 | -13.3% | $639.07 | -1.9 | done | can't tell from luck |
| coinflip | 832 | 50.4 | 51.0 | $-448.82 | -5.4% | $551.18 | -1.6 | done | can't tell from luck |
| trend_filter | 282 | 43.3 | 49.9 | $-464.12 | -16.5% | $535.88 | -2.8 | done | losing for real |
| value_ev5 | 395 | 39.0 | 42.5 | $-481.97 | -12.2% | $518.03 | -2.2 | done | losing for real |
| momentum_5m_0.00pct | 832 | 50.1 | 51.5 | $-539.38 | -6.5% | $460.62 | -1.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 418 | 44.3 | 49.5 | $-592.85 | -14.2% | $407.15 | -2.9 | done | losing for real |
| momentum_15m_0.10pct | 537 | 42.5 | 49.6 | $-945.21 | -17.6% | $54.79 | -4.1 | done | losing for real |
| always_up | 832 | 45.8 | 50.1 | $-1054.45 | -12.7% | $-54.45 | -3.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1211 | 45.9 | 49.7 | $-1287.59 |
| ETH | 1363 | 46.4 | 48.8 | $-1310.84 |
| SOL | 1408 | 47.4 | 49.3 | $-1293.49 |
| XRP | 1476 | 49.3 | 49.2 | $-686.16 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
