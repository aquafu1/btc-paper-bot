# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 19, 7:05 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 860 windows, 23710 settled trades, 36 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 445 | 34.6 | 34.8 | $-223.90 | -5.0% | $776.10 | -0.8 | done | can't tell from luck |
| value_ev10 | 1083 | 37.9 | 39.0 | $-702.23 | -6.5% | $297.77 | -1.7 | done | can't tell from luck |
| momentum_60m_0.30pct | 2003 | 50.2 | 49.7 | $-787.52 | -3.9% | $212.48 | -1.8 | done | can't tell from luck |
| trend_filter | 1394 | 50.1 | 50.9 | $-896.12 | -6.4% | $103.88 | -2.5 | done | losing for real |
| reversal_15m_0.10pct | 2420 | 50.7 | 50.5 | $-920.99 | -3.8% | $79.01 | -1.9 | done | can't tell from luck |
| value_ev5 | 1640 | 39.9 | 41.0 | $-1014.63 | -6.2% | $-14.63 | -2.1 | done | losing for real |
| momentum_15m_0.10pct | 2420 | 49.3 | 50.4 | $-1439.24 | -5.9% | $-439.24 | -2.9 | done | losing for real |
| reversal_60m_0.30pct | 2003 | 49.8 | 51.0 | $-1479.22 | -7.4% | $-479.22 | -3.4 | done | losing for real |
| coinflip | 3434 | 50.1 | 50.3 | $-1552.03 | -4.5% | $-552.03 | -2.7 | done | losing for real |
| momentum_5m_0.00pct | 3434 | 51.2 | 51.7 | $-1651.15 | -4.8% | $-651.15 | -2.9 | done | losing for real |
| always_up | 3434 | 47.0 | 49.5 | $-3271.67 | -9.5% | $-2271.67 | -5.6 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5408 | 48.3 | 49.0 | $-2981.41 |
| ETH | 5903 | 48.0 | 48.5 | $-3909.77 |
| SOL | 6184 | 48.2 | 48.5 | $-3572.13 |
| XRP | 6215 | 48.3 | 48.5 | $-3475.39 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
