# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 12, 7:15 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 151 windows, 3822 settled trades, 46 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 270 | 60.0 | 53.0 | $+285.93 | +10.6% | $1285.93 | +1.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 368 | 57.1 | 52.3 | $+238.51 | +6.5% | $1238.51 | +1.3 | done | can't tell from luck |
| momentum_5m_0.00pct | 596 | 52.3 | 51.3 | $-138.85 | -2.3% | $861.15 | -0.6 | done | can't tell from luck |
| value_ev20 | 74 | 32.4 | 37.2 | $-143.54 | -19.4% | $856.46 | -1.4 | Sun 2:45 AM | too few trades (74/200) |
| coinflip | 596 | 51.2 | 50.9 | $-249.49 | -4.2% | $750.51 | -1.1 | done | can't tell from luck |
| value_ev10 | 199 | 36.7 | 40.7 | $-292.43 | -14.7% | $707.57 | -1.8 | Thu 7:15 AM | too few trades (199/200) |
| trend_filter | 195 | 41.5 | 49.3 | $-369.11 | -18.9% | $630.89 | -2.7 | Thu 8:15 AM | too few trades (195/200) |
| value_ev5 | 290 | 37.9 | 42.4 | $-429.73 | -14.8% | $570.27 | -2.3 | done | losing for real |
| momentum_60m_0.30pct | 270 | 40.0 | 49.4 | $-583.36 | -21.6% | $416.64 | -3.6 | done | losing for real |
| momentum_15m_0.10pct | 368 | 42.9 | 50.0 | $-630.91 | -17.1% | $369.09 | -3.4 | done | losing for real |
| always_up | 596 | 46.1 | 50.0 | $-727.95 | -12.2% | $272.05 | -3.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 818 | 45.7 | 49.6 | $-870.83 |
| ETH | 946 | 45.5 | 48.8 | $-1051.06 |
| SOL | 1007 | 48.4 | 48.8 | $-741.91 |
| XRP | 1051 | 50.1 | 49.1 | $-377.13 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
