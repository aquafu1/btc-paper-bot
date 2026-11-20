# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 19, 9:45 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 871 windows, 24027 settled trades, 72 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 452 | 35.6 | 34.9 | $-106.41 | -2.4% | $893.59 | -0.4 | done | can't tell from luck |
| value_ev10 | 1102 | 38.4 | 39.1 | $-575.43 | -5.2% | $424.57 | -1.4 | done | can't tell from luck |
| momentum_60m_0.30pct | 2030 | 50.0 | 49.7 | $-844.75 | -4.2% | $155.25 | -1.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 2454 | 50.7 | 50.5 | $-915.36 | -3.7% | $84.64 | -1.8 | done | can't tell from luck |
| value_ev5 | 1665 | 40.1 | 41.0 | $-947.83 | -5.7% | $52.17 | -2.0 | done | can't tell from luck |
| trend_filter | 1412 | 49.9 | 51.0 | $-971.20 | -6.9% | $28.80 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 2030 | 50.0 | 51.0 | $-1375.60 | -6.8% | $-375.60 | -3.1 | done | losing for real |
| momentum_15m_0.10pct | 2454 | 49.3 | 50.4 | $-1429.65 | -5.8% | $-429.65 | -2.9 | done | losing for real |
| coinflip | 3476 | 50.1 | 50.3 | $-1528.20 | -4.4% | $-528.20 | -2.6 | done | losing for real |
| momentum_5m_0.00pct | 3476 | 51.2 | 51.7 | $-1645.37 | -4.7% | $-645.37 | -2.9 | done | losing for real |
| always_up | 3476 | 47.0 | 49.6 | $-3346.25 | -9.6% | $-2346.25 | -5.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5483 | 48.3 | 49.1 | $-2911.39 |
| ETH | 5974 | 48.1 | 48.5 | $-3829.21 |
| SOL | 6271 | 48.3 | 48.6 | $-3483.97 |
| XRP | 6299 | 48.3 | 48.5 | $-3461.47 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
