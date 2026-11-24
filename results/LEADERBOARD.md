# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 24, 3:50 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1279 windows, 34339 settled trades, 399 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 673 | 34.0 | 35.3 | $-540.36 | -8.0% | $459.64 | -1.6 | done | can't tell from luck |
| value_ev10 | 1648 | 38.6 | 39.2 | $-840.65 | -5.1% | $159.35 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 3444 | 50.6 | 50.2 | $-1198.77 | -3.5% | $-198.77 | -2.0 | done | losing for real |
| value_ev5 | 2491 | 40.4 | 41.1 | $-1292.01 | -5.2% | $-292.01 | -2.2 | done | losing for real |
| momentum_60m_0.30pct | 2878 | 49.5 | 49.4 | $-1353.43 | -4.7% | $-353.43 | -2.5 | done | losing for real |
| trend_filter | 2033 | 49.0 | 50.5 | $-1623.73 | -8.0% | $-623.73 | -3.7 | done | losing for real |
| reversal_60m_0.30pct | 2878 | 50.5 | 51.0 | $-1643.39 | -5.7% | $-643.39 | -3.1 | done | losing for real |
| momentum_15m_0.10pct | 3444 | 49.4 | 50.3 | $-2048.38 | -5.9% | $-1048.38 | -3.5 | done | losing for real |
| coinflip | 4950 | 50.0 | 50.1 | $-2285.37 | -4.6% | $-1285.37 | -3.3 | done | losing for real |
| momentum_5m_0.00pct | 4950 | 50.5 | 51.4 | $-2765.68 | -5.6% | $-1765.68 | -4.0 | done | losing for real |
| always_up | 4950 | 47.9 | 49.3 | $-3640.09 | -7.4% | $-2640.09 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 8189 | 48.0 | 48.9 | $-4846.25 |
| ETH | 8840 | 48.2 | 48.2 | $-4801.37 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
