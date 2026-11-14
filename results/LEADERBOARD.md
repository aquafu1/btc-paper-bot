# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 14, 7:50 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 335 windows, 8938 settled trades, 68 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 180 | 37.8 | 36.7 | $-22.79 | -1.3% | $977.21 | -0.1 | Sat 5:30 PM | too few trades (180/200) |
| reversal_60m_0.30pct | 713 | 52.9 | 51.8 | $-135.73 | -1.9% | $864.27 | -0.5 | done | can't tell from luck |
| reversal_15m_0.10pct | 883 | 52.5 | 52.0 | $-269.39 | -3.1% | $730.61 | -1.0 | done | can't tell from luck |
| value_ev10 | 436 | 39.2 | 40.3 | $-273.09 | -6.3% | $726.91 | -1.1 | done | can't tell from luck |
| value_ev5 | 647 | 41.0 | 42.0 | $-407.54 | -6.3% | $592.46 | -1.4 | done | can't tell from luck |
| trend_filter | 487 | 45.4 | 50.3 | $-683.95 | -14.0% | $316.05 | -3.2 | done | losing for real |
| momentum_60m_0.30pct | 713 | 47.1 | 49.8 | $-702.69 | -9.9% | $297.31 | -2.7 | done | losing for real |
| coinflip | 1332 | 50.2 | 50.9 | $-712.05 | -5.3% | $287.95 | -2.0 | done | can't tell from luck |
| momentum_15m_0.10pct | 883 | 47.5 | 49.8 | $-765.56 | -8.7% | $234.44 | -2.6 | done | losing for real |
| momentum_5m_0.00pct | 1332 | 48.4 | 51.2 | $-1230.56 | -9.2% | $-230.56 | -3.5 | done | losing for real |
| always_up | 1332 | 47.3 | 50.4 | $-1319.62 | -9.9% | $-319.62 | -3.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1995 | 46.8 | 49.3 | $-1723.04 |
| ETH | 2244 | 47.3 | 48.7 | $-1736.92 |
| SOL | 2330 | 47.9 | 49.3 | $-1821.09 |
| XRP | 2369 | 48.7 | 49.0 | $-1241.93 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
