# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 19, 4:45 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 851 windows, 23462 settled trades, 69 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 439 | 33.9 | 34.8 | $-292.45 | -6.7% | $707.55 | -1.0 | done | can't tell from luck |
| momentum_60m_0.30pct | 1984 | 50.3 | 49.7 | $-757.91 | -3.8% | $242.09 | -1.7 | done | can't tell from luck |
| value_ev10 | 1073 | 37.7 | 39.1 | $-758.84 | -7.1% | $241.16 | -1.9 | done | can't tell from luck |
| trend_filter | 1380 | 50.1 | 50.9 | $-909.35 | -6.6% | $90.65 | -2.5 | done | losing for real |
| reversal_15m_0.10pct | 2397 | 50.7 | 50.5 | $-932.70 | -3.9% | $67.30 | -1.9 | done | can't tell from luck |
| value_ev5 | 1620 | 39.8 | 41.0 | $-1071.38 | -6.6% | $-71.38 | -2.3 | done | losing for real |
| momentum_15m_0.10pct | 2397 | 49.3 | 50.4 | $-1436.56 | -6.0% | $-436.56 | -3.0 | done | losing for real |
| reversal_60m_0.30pct | 1984 | 49.7 | 51.0 | $-1499.72 | -7.6% | $-499.72 | -3.4 | done | losing for real |
| coinflip | 3396 | 50.2 | 50.3 | $-1529.04 | -4.5% | $-529.04 | -2.6 | done | losing for real |
| momentum_5m_0.00pct | 3396 | 51.3 | 51.7 | $-1596.95 | -4.7% | $-596.95 | -2.8 | done | losing for real |
| always_up | 3396 | 46.9 | 49.5 | $-3284.84 | -9.7% | $-2284.84 | -5.6 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5343 | 48.2 | 49.1 | $-3118.11 |
| ETH | 5842 | 48.0 | 48.5 | $-3958.85 |
| SOL | 6117 | 48.2 | 48.5 | $-3667.33 |
| XRP | 6160 | 48.4 | 48.5 | $-3325.45 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
