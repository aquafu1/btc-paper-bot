# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 15, 11:50 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 495 windows, 13612 settled trades, 58 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 251 | 34.3 | 35.8 | $-189.21 | -7.5% | $810.79 | -0.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 1158 | 51.0 | 49.9 | $-225.41 | -1.9% | $774.59 | -0.7 | done | can't tell from luck |
| value_ev10 | 639 | 38.3 | 40.0 | $-470.56 | -7.4% | $529.44 | -1.5 | done | can't tell from luck |
| trend_filter | 801 | 49.7 | 50.8 | $-534.70 | -6.7% | $465.30 | -1.9 | done | can't tell from luck |
| momentum_15m_0.10pct | 1372 | 49.8 | 49.9 | $-548.77 | -4.0% | $451.23 | -1.5 | done | can't tell from luck |
| value_ev5 | 945 | 40.5 | 41.7 | $-596.78 | -6.3% | $403.22 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 1372 | 50.2 | 51.5 | $-916.76 | -6.7% | $83.24 | -2.5 | done | losing for real |
| coinflip | 1972 | 50.1 | 50.8 | $-1020.02 | -5.2% | $-20.02 | -2.3 | done | losing for real |
| reversal_60m_0.30pct | 1158 | 49.0 | 51.4 | $-1055.31 | -9.1% | $-55.31 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 1972 | 49.8 | 51.7 | $-1417.25 | -7.2% | $-417.25 | -3.3 | done | losing for real |
| always_up | 1972 | 46.3 | 50.3 | $-2318.52 | -11.8% | $-1318.52 | -5.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3068 | 47.4 | 49.3 | $-2491.58 |
| ETH | 3411 | 48.1 | 48.8 | $-2236.26 |
| SOL | 3551 | 47.8 | 49.2 | $-2597.34 |
| XRP | 3582 | 48.5 | 48.9 | $-1968.10 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
