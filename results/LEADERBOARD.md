# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 18, 3:45 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 703 windows, 19419 settled trades, 37 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 372 | 34.1 | 34.9 | $-244.03 | -6.6% | $755.97 | -0.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 1633 | 50.2 | 49.4 | $-511.28 | -3.1% | $488.72 | -1.3 | done | can't tell from luck |
| value_ev10 | 899 | 38.4 | 39.1 | $-513.27 | -5.7% | $486.73 | -1.4 | done | can't tell from luck |
| reversal_15m_0.10pct | 1994 | 51.6 | 50.8 | $-541.68 | -2.7% | $458.32 | -1.2 | done | can't tell from luck |
| value_ev5 | 1351 | 40.8 | 41.1 | $-618.49 | -4.6% | $381.51 | -1.4 | done | can't tell from luck |
| trend_filter | 1131 | 50.2 | 50.9 | $-634.55 | -5.6% | $365.45 | -1.9 | done | can't tell from luck |
| coinflip | 2804 | 50.2 | 50.3 | $-1184.22 | -4.2% | $-184.22 | -2.2 | done | losing for real |
| reversal_60m_0.30pct | 1633 | 49.8 | 51.4 | $-1230.27 | -7.5% | $-230.27 | -3.1 | done | losing for real |
| momentum_15m_0.10pct | 1994 | 48.4 | 50.0 | $-1407.93 | -7.1% | $-407.93 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 2804 | 50.9 | 51.8 | $-1493.16 | -5.3% | $-493.16 | -2.9 | done | losing for real |
| always_up | 2804 | 47.4 | 49.6 | $-2376.75 | -8.5% | $-1376.75 | -4.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4403 | 48.2 | 49.1 | $-2564.98 |
| ETH | 4831 | 48.3 | 48.5 | $-2759.79 |
| SOL | 5067 | 48.2 | 48.7 | $-2896.61 |
| XRP | 5118 | 48.5 | 48.4 | $-2534.26 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
