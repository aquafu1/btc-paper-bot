# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 11, 10:35 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 78 windows, 1958 settled trades, 52 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_5m_0.00pct | 305 | 57.0 | 50.9 | $+258.10 | +8.5% | $1258.10 | +1.5 | done | can't tell from luck |
| reversal_60m_0.30pct | 141 | 60.3 | 52.6 | $+167.77 | +11.9% | $1167.77 | +1.5 | Wed 6:45 PM | too few trades (141/200) |
| reversal_15m_0.10pct | 183 | 57.4 | 52.0 | $+142.41 | +7.8% | $1142.41 | +1.1 | Wed 12:30 PM | too few trades (183/200) |
| value_ev10 | 105 | 41.0 | 39.8 | $-30.48 | -2.9% | $969.52 | -0.2 | Thu 4:00 AM | too few trades (105/200) |
| value_ev20 | 43 | 32.6 | 35.9 | $-53.85 | -12.5% | $946.15 | -0.6 | Sat 9:00 AM | too few trades (43/200) |
| trend_filter | 103 | 46.6 | 48.7 | $-80.77 | -7.8% | $919.23 | -0.8 | Thu 4:45 AM | too few trades (103/200) |
| value_ev5 | 144 | 39.6 | 41.3 | $-128.07 | -8.9% | $871.93 | -0.9 | Wed 6:00 PM | too few trades (144/200) |
| coinflip | 305 | 50.2 | 51.6 | $-191.05 | -6.3% | $808.95 | -1.1 | done | can't tell from luck |
| momentum_60m_0.30pct | 141 | 39.7 | 48.6 | $-294.29 | -20.9% | $705.71 | -2.5 | Wed 6:45 PM | too few trades (141/200) |
| momentum_15m_0.10pct | 183 | 42.6 | 49.4 | $-305.57 | -16.7% | $694.42 | -2.3 | Wed 12:30 PM | too few trades (183/200) |
| always_up | 305 | 44.9 | 50.2 | $-423.86 | -13.9% | $576.14 | -2.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 412 | 47.3 | 49.8 | $-161.14 |
| ETH | 468 | 46.6 | 48.6 | $-293.81 |
| SOL | 534 | 49.3 | 48.3 | $-269.00 |
| XRP | 544 | 50.4 | 48.3 | $-215.71 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
