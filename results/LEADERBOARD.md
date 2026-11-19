# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 19, 2:30 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 842 windows, 23147 settled trades, 84 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 424 | 33.0 | 34.9 | $-410.80 | -9.7% | $589.20 | -1.5 | done | can't tell from luck |
| momentum_60m_0.30pct | 1951 | 50.0 | 49.7 | $-873.57 | -4.5% | $126.43 | -2.0 | done | can't tell from luck |
| value_ev10 | 1054 | 37.3 | 39.2 | $-882.88 | -8.4% | $117.12 | -2.2 | done | losing for real |
| reversal_15m_0.10pct | 2364 | 50.8 | 50.6 | $-904.63 | -3.8% | $95.37 | -1.9 | done | can't tell from luck |
| trend_filter | 1361 | 49.9 | 50.9 | $-955.35 | -7.0% | $44.65 | -2.7 | done | losing for real |
| value_ev5 | 1598 | 39.6 | 41.1 | $-1165.42 | -7.3% | $-165.42 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 1951 | 50.0 | 51.1 | $-1422.83 | -7.3% | $-422.83 | -3.3 | done | losing for real |
| momentum_15m_0.10pct | 2364 | 49.2 | 50.3 | $-1476.17 | -6.2% | $-476.17 | -3.1 | done | losing for real |
| coinflip | 3360 | 50.3 | 50.3 | $-1494.54 | -4.4% | $-494.54 | -2.6 | done | losing for real |
| momentum_5m_0.00pct | 3360 | 51.2 | 51.7 | $-1599.06 | -4.8% | $-599.06 | -2.9 | done | losing for real |
| always_up | 3360 | 47.1 | 49.6 | $-3194.69 | -9.5% | $-2194.69 | -5.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5266 | 48.1 | 49.1 | $-3395.70 |
| ETH | 5764 | 48.0 | 48.5 | $-4007.01 |
| SOL | 6036 | 48.2 | 48.6 | $-3621.26 |
| XRP | 6081 | 48.4 | 48.5 | $-3355.96 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
