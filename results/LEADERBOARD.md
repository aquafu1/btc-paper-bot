# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 20, 10:30 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 970 windows, 26893 settled trades, 63 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 496 | 34.7 | 34.8 | $-219.50 | -4.4% | $780.50 | -0.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 2745 | 51.3 | 50.5 | $-695.34 | -2.5% | $304.66 | -1.3 | done | can't tell from luck |
| value_ev10 | 1228 | 37.9 | 39.1 | $-734.80 | -6.0% | $265.20 | -1.7 | done | can't tell from luck |
| momentum_60m_0.30pct | 2296 | 50.3 | 49.8 | $-829.75 | -3.6% | $170.25 | -1.7 | done | can't tell from luck |
| trend_filter | 1608 | 50.0 | 50.9 | $-1067.85 | -6.6% | $-67.85 | -2.7 | done | losing for real |
| value_ev5 | 1863 | 39.9 | 40.9 | $-1078.05 | -5.8% | $-78.05 | -2.1 | done | losing for real |
| reversal_60m_0.30pct | 2296 | 49.7 | 50.9 | $-1687.28 | -7.3% | $-687.28 | -3.6 | done | losing for real |
| coinflip | 3872 | 50.2 | 50.3 | $-1794.78 | -4.6% | $-794.78 | -2.9 | done | losing for real |
| momentum_15m_0.10pct | 2745 | 48.7 | 50.3 | $-1979.98 | -7.2% | $-979.98 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 3872 | 50.8 | 51.6 | $-2050.82 | -5.3% | $-1050.82 | -3.4 | done | losing for real |
| always_up | 3872 | 46.8 | 49.6 | $-3877.42 | -10.0% | $-2877.42 | -6.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6125 | 48.2 | 49.1 | $-3456.46 |
| ETH | 6682 | 48.0 | 48.5 | $-4237.28 |
| SOL | 7024 | 48.2 | 48.6 | $-3931.49 |
| XRP | 7062 | 48.1 | 48.4 | $-4390.33 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
