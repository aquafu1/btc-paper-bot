# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 13, 7:00 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 236 windows, 6161 settled trades, 42 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 605 | 56.4 | 52.6 | $+232.40 | +3.8% | $1232.40 | +1.0 | done | can't tell from luck |
| reversal_60m_0.30pct | 483 | 54.2 | 52.3 | $+5.50 | +0.1% | $1005.50 | +0.0 | done | can't tell from luck |
| value_ev20 | 113 | 34.5 | 36.6 | $-110.27 | -9.8% | $889.73 | -0.8 | Sun 7:45 AM | too few trades (113/200) |
| value_ev10 | 301 | 37.9 | 40.8 | $-325.09 | -10.8% | $674.91 | -1.6 | done | can't tell from luck |
| trend_filter | 325 | 44.9 | 50.1 | $-458.44 | -14.1% | $541.56 | -2.6 | done | losing for real |
| value_ev5 | 438 | 39.5 | 42.5 | $-472.65 | -10.8% | $527.35 | -2.0 | done | can't tell from luck |
| momentum_60m_0.30pct | 483 | 45.8 | 49.8 | $-583.00 | -12.1% | $417.00 | -2.7 | done | losing for real |
| coinflip | 936 | 49.6 | 50.9 | $-627.48 | -6.7% | $372.52 | -2.1 | done | losing for real |
| momentum_5m_0.00pct | 936 | 49.8 | 51.4 | $-663.35 | -7.1% | $336.65 | -2.3 | done | losing for real |
| always_up | 936 | 47.6 | 50.5 | $-916.18 | -9.8% | $83.82 | -3.1 | done | losing for real |
| momentum_15m_0.10pct | 605 | 43.6 | 49.7 | $-940.37 | -15.5% | $59.63 | -3.9 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1378 | 46.4 | 49.7 | $-1408.04 |
| ETH | 1534 | 46.7 | 49.0 | $-1518.20 |
| SOL | 1592 | 48.2 | 49.3 | $-1202.45 |
| XRP | 1657 | 49.0 | 49.2 | $-730.25 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
