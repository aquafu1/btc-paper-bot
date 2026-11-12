# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 12, 4:30 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 140 windows, 3510 settled trades, 59 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 243 | 62.1 | 53.1 | $+353.39 | +14.5% | $1353.39 | +2.4 | done | real edge? (z>=2) |
| reversal_15m_0.10pct | 337 | 57.0 | 52.1 | $+231.90 | +6.9% | $1231.90 | +1.3 | done | can't tell from luck |
| value_ev20 | 67 | 31.3 | 37.0 | $-135.47 | -20.2% | $864.53 | -1.4 | Sun 5:45 AM | too few trades (67/200) |
| momentum_5m_0.00pct | 552 | 51.8 | 51.2 | $-163.45 | -3.0% | $836.55 | -0.7 | done | can't tell from luck |
| coinflip | 552 | 51.8 | 51.0 | $-164.15 | -3.0% | $835.85 | -0.7 | done | can't tell from luck |
| value_ev10 | 184 | 37.5 | 40.6 | $-225.28 | -12.2% | $774.72 | -1.4 | Thu 7:30 AM | too few trades (184/200) |
| value_ev5 | 266 | 38.7 | 42.2 | $-334.16 | -12.6% | $665.84 | -1.8 | done | can't tell from luck |
| trend_filter | 177 | 40.1 | 49.2 | $-376.47 | -21.3% | $623.53 | -2.8 | Thu 9:15 AM | too few trades (177/200) |
| always_up | 552 | 47.3 | 50.2 | $-554.97 | -10.1% | $445.03 | -2.4 | done | losing for real |
| momentum_15m_0.10pct | 337 | 43.0 | 50.1 | $-567.03 | -16.8% | $432.97 | -3.1 | done | losing for real |
| momentum_60m_0.30pct | 243 | 37.9 | 49.2 | $-610.69 | -25.1% | $389.31 | -4.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 754 | 45.6 | 49.6 | $-805.73 |
| ETH | 868 | 44.9 | 48.8 | $-1024.17 |
| SOL | 923 | 49.0 | 48.8 | $-534.81 |
| XRP | 965 | 50.9 | 49.1 | $-181.66 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
