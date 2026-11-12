# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 12, 6:15 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 147 windows, 3708 settled trades, 58 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 256 | 59.8 | 53.2 | $+252.92 | +9.9% | $1252.92 | +1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 357 | 55.7 | 52.2 | $+146.43 | +4.1% | $1146.43 | +0.8 | done | can't tell from luck |
| momentum_5m_0.00pct | 580 | 52.9 | 51.4 | $-78.78 | -1.4% | $921.22 | -0.3 | done | can't tell from luck |
| value_ev20 | 74 | 32.4 | 37.2 | $-143.54 | -19.4% | $856.46 | -1.4 | Sun 12:00 AM | too few trades (74/200) |
| coinflip | 580 | 51.4 | 50.9 | $-228.70 | -3.9% | $771.30 | -1.0 | done | can't tell from luck |
| value_ev10 | 195 | 37.4 | 40.7 | $-252.43 | -12.9% | $747.57 | -1.6 | Thu 7:00 AM | too few trades (195/200) |
| trend_filter | 189 | 42.3 | 49.3 | $-327.78 | -17.3% | $672.22 | -2.4 | Thu 8:30 AM | too few trades (189/200) |
| value_ev5 | 284 | 38.7 | 42.3 | $-369.73 | -13.0% | $630.27 | -2.0 | done | can't tell from luck |
| momentum_15m_0.10pct | 357 | 44.3 | 50.0 | $-520.91 | -14.6% | $479.09 | -2.8 | done | losing for real |
| momentum_60m_0.30pct | 256 | 40.2 | 49.2 | $-530.07 | -20.7% | $469.93 | -3.3 | done | losing for real |
| always_up | 580 | 45.9 | 50.0 | $-740.96 | -12.8% | $259.04 | -3.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 792 | 45.8 | 49.6 | $-823.67 |
| ETH | 916 | 45.5 | 48.8 | $-1000.11 |
| SOL | 977 | 48.5 | 48.8 | $-684.64 |
| XRP | 1023 | 50.5 | 49.1 | $-285.16 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
