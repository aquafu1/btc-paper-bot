# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 12, 7:50 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 191 windows, 4897 settled trades, 40 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 477 | 58.3 | 52.5 | $+370.40 | +7.8% | $1370.40 | +1.8 | done | can't tell from luck |
| reversal_60m_0.30pct | 357 | 59.9 | 53.1 | $+347.19 | +9.7% | $1347.19 | +2.0 | done | can't tell from luck |
| value_ev20 | 95 | 31.6 | 37.0 | $-198.58 | -20.9% | $801.42 | -1.7 | Sun 6:00 AM | too few trades (95/200) |
| momentum_5m_0.00pct | 758 | 51.8 | 51.4 | $-251.21 | -3.3% | $748.79 | -0.9 | done | can't tell from luck |
| coinflip | 758 | 50.5 | 51.0 | $-411.43 | -5.4% | $588.57 | -1.6 | done | can't tell from luck |
| value_ev10 | 250 | 36.0 | 40.8 | $-413.19 | -16.5% | $586.81 | -2.3 | done | losing for real |
| trend_filter | 243 | 41.6 | 49.4 | $-457.37 | -18.8% | $542.63 | -2.9 | done | losing for real |
| value_ev5 | 367 | 38.4 | 42.6 | $-520.29 | -14.2% | $479.71 | -2.5 | done | losing for real |
| momentum_60m_0.30pct | 357 | 40.1 | 49.0 | $-778.37 | -21.8% | $221.63 | -4.2 | done | losing for real |
| momentum_15m_0.10pct | 477 | 41.7 | 49.7 | $-923.22 | -19.4% | $76.78 | -4.3 | done | losing for real |
| always_up | 758 | 46.3 | 50.2 | $-938.35 | -12.4% | $61.65 | -3.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1078 | 45.8 | 49.5 | $-1154.80 |
| ETH | 1214 | 46.0 | 48.8 | $-1360.44 |
| SOL | 1272 | 47.7 | 49.1 | $-1111.81 |
| XRP | 1333 | 49.7 | 49.2 | $-547.37 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
