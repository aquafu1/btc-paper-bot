# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 15, 4:20 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 417 windows, 11492 settled trades, 30 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 209 | 34.9 | 36.4 | $-156.95 | -7.5% | $843.05 | -0.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 987 | 50.8 | 50.1 | $-278.78 | -2.8% | $721.22 | -0.9 | done | can't tell from luck |
| value_ev10 | 536 | 39.7 | 40.4 | $-281.49 | -5.3% | $718.51 | -1.0 | done | can't tell from luck |
| value_ev5 | 806 | 41.8 | 42.1 | $-368.73 | -4.6% | $631.27 | -1.1 | done | can't tell from luck |
| trend_filter | 660 | 49.7 | 50.8 | $-402.59 | -6.1% | $597.41 | -1.6 | done | can't tell from luck |
| momentum_15m_0.10pct | 1159 | 49.4 | 50.0 | $-539.17 | -4.7% | $460.83 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 1159 | 50.6 | 51.8 | $-761.79 | -6.6% | $238.21 | -2.4 | done | losing for real |
| coinflip | 1663 | 50.3 | 50.9 | $-823.99 | -5.0% | $176.01 | -2.1 | done | losing for real |
| reversal_60m_0.30pct | 987 | 49.2 | 51.8 | $-885.63 | -9.0% | $114.37 | -3.0 | done | losing for real |
| momentum_5m_0.00pct | 1663 | 49.5 | 51.6 | $-1231.90 | -7.4% | $-231.90 | -3.1 | done | losing for real |
| always_up | 1663 | 45.8 | 50.7 | $-2168.96 | -13.0% | $-1168.96 | -5.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2596 | 47.7 | 49.4 | $-1905.65 |
| ETH | 2892 | 47.9 | 49.0 | $-1855.78 |
| SOL | 2979 | 47.6 | 49.5 | $-2498.90 |
| XRP | 3025 | 48.8 | 49.3 | $-1639.65 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
