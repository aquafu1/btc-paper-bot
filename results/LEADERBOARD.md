# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 14, 9:30 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 390 windows, 10663 settled trades, 61 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 196 | 37.2 | 36.6 | $-26.95 | -1.4% | $973.05 | -0.1 | Sat 11:30 PM | too few trades (196/200) |
| value_ev10 | 509 | 40.3 | 40.5 | $-184.20 | -3.6% | $815.80 | -0.7 | done | can't tell from luck |
| momentum_60m_0.30pct | 901 | 50.7 | 49.8 | $-205.62 | -2.3% | $794.38 | -0.7 | done | can't tell from luck |
| value_ev5 | 752 | 42.0 | 42.1 | $-280.65 | -3.7% | $719.35 | -0.9 | done | can't tell from luck |
| trend_filter | 604 | 49.8 | 50.5 | $-318.06 | -5.3% | $681.94 | -1.3 | done | can't tell from luck |
| momentum_15m_0.10pct | 1072 | 49.5 | 49.7 | $-415.87 | -3.9% | $584.13 | -1.3 | done | can't tell from luck |
| reversal_15m_0.10pct | 1072 | 50.5 | 52.1 | $-754.18 | -7.0% | $245.82 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 901 | 49.3 | 52.1 | $-828.17 | -9.2% | $171.83 | -2.9 | done | losing for real |
| coinflip | 1552 | 49.9 | 50.8 | $-841.21 | -5.4% | $158.79 | -2.2 | done | losing for real |
| momentum_5m_0.00pct | 1552 | 49.9 | 51.5 | $-1020.15 | -6.6% | $-20.15 | -2.7 | done | losing for real |
| always_up | 1552 | 46.3 | 50.7 | $-1872.47 | -12.1% | $-872.47 | -4.9 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2411 | 47.8 | 49.4 | $-1625.35 |
| ETH | 2679 | 47.9 | 48.9 | $-1697.10 |
| SOL | 2760 | 48.0 | 49.5 | $-1999.99 |
| XRP | 2813 | 48.8 | 49.2 | $-1425.08 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
