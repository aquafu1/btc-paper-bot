# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 20, 1:20 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 885 windows, 24435 settled trades, 46 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 461 | 35.6 | 34.9 | $-99.37 | -2.2% | $900.63 | -0.3 | done | can't tell from luck |
| value_ev10 | 1122 | 38.2 | 39.1 | $-607.55 | -5.4% | $392.45 | -1.5 | done | can't tell from luck |
| momentum_60m_0.30pct | 2068 | 50.0 | 49.8 | $-890.72 | -4.3% | $109.28 | -2.0 | done | can't tell from luck |
| trend_filter | 1438 | 50.3 | 50.9 | $-901.24 | -6.3% | $98.76 | -2.4 | done | losing for real |
| reversal_15m_0.10pct | 2492 | 50.5 | 50.4 | $-1027.52 | -4.1% | $-27.52 | -2.1 | done | losing for real |
| value_ev5 | 1695 | 39.8 | 41.0 | $-1054.77 | -6.2% | $-54.77 | -2.2 | done | losing for real |
| momentum_15m_0.10pct | 2492 | 49.5 | 50.4 | $-1378.04 | -5.5% | $-378.04 | -2.8 | done | losing for real |
| reversal_60m_0.30pct | 2068 | 50.0 | 50.9 | $-1394.64 | -6.7% | $-394.64 | -3.1 | done | losing for real |
| momentum_5m_0.00pct | 3533 | 51.4 | 51.7 | $-1516.80 | -4.3% | $-516.80 | -2.6 | done | losing for real |
| coinflip | 3533 | 50.2 | 50.3 | $-1549.17 | -4.4% | $-549.17 | -2.6 | done | losing for real |
| always_up | 3533 | 46.9 | 49.6 | $-3452.16 | -9.8% | $-2452.16 | -5.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5574 | 48.3 | 49.1 | $-3040.18 |
| ETH | 6081 | 48.2 | 48.5 | $-3745.10 |
| SOL | 6376 | 48.3 | 48.5 | $-3554.34 |
| XRP | 6404 | 48.4 | 48.5 | $-3532.37 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
