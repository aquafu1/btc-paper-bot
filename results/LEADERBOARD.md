# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 19, 8:15 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 865 windows, 23815 settled trades, 72 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 445 | 34.6 | 34.8 | $-223.90 | -5.0% | $776.10 | -0.8 | done | can't tell from luck |
| value_ev10 | 1088 | 37.9 | 39.1 | $-708.03 | -6.5% | $291.97 | -1.7 | done | can't tell from luck |
| momentum_60m_0.30pct | 2008 | 50.1 | 49.7 | $-816.71 | -4.1% | $183.29 | -1.8 | done | can't tell from luck |
| trend_filter | 1397 | 50.3 | 50.9 | $-872.10 | -6.2% | $127.90 | -2.4 | done | losing for real |
| reversal_15m_0.10pct | 2432 | 50.6 | 50.5 | $-968.59 | -4.0% | $31.41 | -2.0 | done | can't tell from luck |
| value_ev5 | 1649 | 39.8 | 41.0 | $-1060.43 | -6.4% | $-60.43 | -2.2 | done | losing for real |
| momentum_15m_0.10pct | 2432 | 49.4 | 50.4 | $-1393.95 | -5.7% | $-393.95 | -2.8 | done | losing for real |
| reversal_60m_0.30pct | 2008 | 49.9 | 51.0 | $-1442.50 | -7.2% | $-442.50 | -3.3 | done | losing for real |
| momentum_5m_0.00pct | 3452 | 51.4 | 51.7 | $-1504.57 | -4.4% | $-504.57 | -2.6 | done | losing for real |
| coinflip | 3452 | 50.1 | 50.3 | $-1558.96 | -4.5% | $-558.96 | -2.7 | done | losing for real |
| always_up | 3452 | 46.9 | 49.6 | $-3342.90 | -9.7% | $-2342.90 | -5.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5431 | 48.3 | 49.0 | $-2972.40 |
| ETH | 5925 | 48.1 | 48.5 | $-3893.47 |
| SOL | 6214 | 48.3 | 48.6 | $-3531.93 |
| XRP | 6245 | 48.3 | 48.5 | $-3494.84 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
