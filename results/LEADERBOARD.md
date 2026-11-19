# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 19, 3:50 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 847 windows, 23331 settled trades, 69 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 431 | 33.6 | 34.9 | $-327.48 | -7.6% | $672.52 | -1.2 | done | can't tell from luck |
| momentum_60m_0.30pct | 1970 | 50.3 | 49.7 | $-772.19 | -3.9% | $227.81 | -1.7 | done | can't tell from luck |
| value_ev10 | 1064 | 37.6 | 39.1 | $-783.87 | -7.4% | $216.13 | -2.0 | done | can't tell from luck |
| trend_filter | 1375 | 50.1 | 50.9 | $-898.59 | -6.5% | $101.41 | -2.5 | done | losing for real |
| reversal_15m_0.10pct | 2384 | 50.8 | 50.5 | $-910.61 | -3.8% | $89.39 | -1.9 | done | can't tell from luck |
| value_ev5 | 1610 | 39.8 | 41.1 | $-1086.42 | -6.7% | $-86.42 | -2.3 | done | losing for real |
| momentum_15m_0.10pct | 2384 | 49.2 | 50.3 | $-1435.34 | -6.0% | $-435.34 | -3.0 | done | losing for real |
| reversal_60m_0.30pct | 1970 | 49.7 | 51.1 | $-1486.96 | -7.5% | $-486.96 | -3.4 | done | losing for real |
| coinflip | 3381 | 50.2 | 50.3 | $-1512.31 | -4.5% | $-512.31 | -2.6 | done | losing for real |
| momentum_5m_0.00pct | 3381 | 51.2 | 51.7 | $-1593.00 | -4.7% | $-593.00 | -2.8 | done | losing for real |
| always_up | 3381 | 46.9 | 49.5 | $-3278.82 | -9.7% | $-2278.82 | -5.6 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5308 | 48.2 | 49.1 | $-3153.47 |
| ETH | 5817 | 48.0 | 48.5 | $-3993.75 |
| SOL | 6081 | 48.2 | 48.6 | $-3621.77 |
| XRP | 6125 | 48.4 | 48.5 | $-3316.61 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
