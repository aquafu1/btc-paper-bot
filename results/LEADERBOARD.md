# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 22, 9:15 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1157 windows, 31968 settled trades, 61 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 615 | 34.5 | 35.3 | $-407.85 | -6.6% | $592.15 | -1.2 | done | can't tell from luck |
| value_ev10 | 1507 | 38.2 | 39.2 | $-901.63 | -6.0% | $98.37 | -1.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 3209 | 50.8 | 50.4 | $-1038.55 | -3.2% | $-38.55 | -1.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 2697 | 49.8 | 49.5 | $-1165.95 | -4.3% | $-165.95 | -2.2 | done | losing for real |
| value_ev5 | 2279 | 40.1 | 41.1 | $-1300.59 | -5.7% | $-300.59 | -2.3 | done | losing for real |
| trend_filter | 1895 | 49.0 | 50.5 | $-1537.05 | -8.1% | $-537.05 | -3.6 | done | losing for real |
| reversal_60m_0.30pct | 2697 | 50.2 | 51.0 | $-1707.81 | -6.3% | $-707.81 | -3.4 | done | losing for real |
| momentum_15m_0.10pct | 3209 | 49.2 | 50.2 | $-1963.02 | -6.1% | $-963.02 | -3.5 | done | losing for real |
| coinflip | 4620 | 50.2 | 50.2 | $-1969.82 | -4.3% | $-969.82 | -2.9 | done | losing for real |
| momentum_5m_0.00pct | 4620 | 50.1 | 51.4 | $-2976.07 | -6.4% | $-1976.07 | -4.5 | done | losing for real |
| always_up | 4620 | 47.7 | 49.3 | $-3524.40 | -7.6% | $-2524.40 | -5.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7326 | 48.2 | 49.0 | $-3926.10 |
| ETH | 7924 | 48.1 | 48.4 | $-4745.20 |
| SOL | 8320 | 48.0 | 48.4 | $-4702.94 |
| XRP | 8398 | 48.0 | 48.2 | $-5118.50 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
