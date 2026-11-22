# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 21, 7:30 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1054 windows, 29189 settled trades, 48 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 544 | 34.6 | 35.1 | $-308.54 | -5.7% | $691.46 | -1.0 | done | can't tell from luck |
| reversal_15m_0.10pct | 2956 | 51.3 | 50.4 | $-769.64 | -2.6% | $230.36 | -1.4 | done | can't tell from luck |
| value_ev10 | 1352 | 37.6 | 39.2 | $-973.39 | -7.2% | $26.61 | -2.2 | done | losing for real |
| momentum_60m_0.30pct | 2485 | 49.7 | 49.6 | $-1178.14 | -4.7% | $-178.14 | -2.4 | done | losing for real |
| trend_filter | 1739 | 49.3 | 50.7 | $-1363.92 | -7.8% | $-363.92 | -3.4 | done | losing for real |
| value_ev5 | 2048 | 39.5 | 41.0 | $-1427.51 | -7.0% | $-427.51 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 2485 | 50.3 | 51.0 | $-1556.08 | -6.3% | $-556.08 | -3.2 | done | losing for real |
| coinflip | 4208 | 50.5 | 50.3 | $-1721.06 | -4.1% | $-721.06 | -2.7 | done | losing for real |
| momentum_15m_0.10pct | 2956 | 48.7 | 50.3 | $-2073.67 | -7.0% | $-1073.67 | -3.9 | done | losing for real |
| momentum_5m_0.00pct | 4208 | 50.8 | 51.5 | $-2220.65 | -5.3% | $-1220.65 | -3.5 | done | losing for real |
| always_up | 4208 | 47.3 | 49.4 | $-3624.09 | -8.6% | $-2624.09 | -5.6 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6651 | 48.3 | 49.0 | $-3496.94 |
| ETH | 7224 | 48.1 | 48.5 | $-4616.80 |
| SOL | 7621 | 48.1 | 48.5 | $-4418.01 |
| XRP | 7693 | 48.2 | 48.3 | $-4684.95 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
