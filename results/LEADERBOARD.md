# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 15, 10:20 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 489 windows, 13446 settled trades, 42 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 249 | 34.5 | 35.8 | $-169.21 | -6.8% | $830.79 | -0.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 1143 | 51.0 | 49.8 | $-209.48 | -1.8% | $790.52 | -0.6 | done | can't tell from luck |
| value_ev10 | 633 | 38.7 | 40.0 | $-410.56 | -6.5% | $589.44 | -1.3 | done | can't tell from luck |
| momentum_15m_0.10pct | 1353 | 50.1 | 49.9 | $-438.56 | -3.2% | $561.44 | -1.2 | done | can't tell from luck |
| value_ev5 | 936 | 40.9 | 41.8 | $-506.78 | -5.4% | $493.22 | -1.4 | done | can't tell from luck |
| trend_filter | 789 | 49.4 | 50.7 | $-540.26 | -6.8% | $459.74 | -2.0 | done | can't tell from luck |
| reversal_15m_0.10pct | 1353 | 49.9 | 51.5 | $-958.17 | -7.1% | $41.83 | -2.7 | done | losing for real |
| coinflip | 1949 | 50.0 | 50.8 | $-1006.38 | -5.2% | $-6.38 | -2.3 | done | losing for real |
| reversal_60m_0.30pct | 1143 | 49.0 | 51.4 | $-1020.14 | -8.9% | $-20.14 | -3.1 | done | losing for real |
| momentum_5m_0.00pct | 1949 | 49.6 | 51.6 | $-1437.57 | -7.4% | $-437.57 | -3.4 | done | losing for real |
| always_up | 1949 | 46.5 | 50.4 | $-2219.97 | -11.4% | $-1219.97 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3029 | 47.4 | 49.3 | $-2419.66 |
| ETH | 3368 | 48.1 | 48.8 | $-2122.20 |
| SOL | 3512 | 47.8 | 49.2 | $-2497.20 |
| XRP | 3537 | 48.5 | 48.9 | $-1878.02 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
