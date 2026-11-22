# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 21, 8:45 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1059 windows, 29291 settled trades, 60 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 547 | 34.6 | 35.1 | $-310.90 | -5.7% | $689.10 | -1.0 | done | can't tell from luck |
| reversal_15m_0.10pct | 2964 | 51.3 | 50.4 | $-749.81 | -2.5% | $250.19 | -1.4 | done | can't tell from luck |
| value_ev10 | 1356 | 37.6 | 39.2 | $-963.14 | -7.1% | $36.86 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 2488 | 49.6 | 49.6 | $-1192.80 | -4.8% | $-192.80 | -2.4 | done | losing for real |
| trend_filter | 1742 | 49.3 | 50.7 | $-1361.97 | -7.8% | $-361.97 | -3.4 | done | losing for real |
| value_ev5 | 2058 | 39.6 | 41.0 | $-1368.73 | -6.7% | $-368.73 | -2.6 | done | losing for real |
| reversal_60m_0.30pct | 2488 | 50.4 | 51.0 | $-1548.08 | -6.2% | $-548.08 | -3.2 | done | losing for real |
| coinflip | 4228 | 50.5 | 50.3 | $-1708.89 | -4.0% | $-708.89 | -2.7 | done | losing for real |
| momentum_15m_0.10pct | 2964 | 48.7 | 50.3 | $-2105.50 | -7.1% | $-1105.50 | -3.9 | done | losing for real |
| momentum_5m_0.00pct | 4228 | 50.8 | 51.5 | $-2246.02 | -5.3% | $-1246.02 | -3.6 | done | losing for real |
| always_up | 4228 | 47.3 | 49.4 | $-3671.17 | -8.7% | $-2671.17 | -5.6 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6680 | 48.4 | 49.0 | $-3443.28 |
| ETH | 7245 | 48.1 | 48.5 | $-4615.49 |
| SOL | 7645 | 48.0 | 48.5 | $-4501.80 |
| XRP | 7721 | 48.2 | 48.3 | $-4666.43 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
