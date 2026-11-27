# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 26, 6:50 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1531 windows, 37816 settled trades, 372 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 769 | 34.6 | 35.3 | $-546.25 | -7.1% | $453.75 | -1.5 | done | can't tell from luck |
| value_ev10 | 1851 | 38.6 | 39.2 | $-959.85 | -5.2% | $40.15 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 3754 | 50.9 | 50.0 | $-961.58 | -2.6% | $38.42 | -1.6 | done | can't tell from luck |
| value_ev5 | 2793 | 40.6 | 41.1 | $-1354.23 | -4.8% | $-354.23 | -2.2 | done | losing for real |
| reversal_60m_0.30pct | 3149 | 51.1 | 51.0 | $-1456.61 | -4.6% | $-456.61 | -2.7 | done | losing for real |
| momentum_60m_0.30pct | 3149 | 48.9 | 49.2 | $-1692.90 | -5.4% | $-692.90 | -3.0 | done | losing for real |
| trend_filter | 2238 | 48.6 | 50.3 | $-1919.10 | -8.6% | $-919.10 | -4.1 | done | losing for real |
| momentum_15m_0.10pct | 3754 | 49.1 | 50.2 | $-2343.21 | -6.2% | $-1343.21 | -3.9 | done | losing for real |
| coinflip | 5453 | 50.0 | 50.0 | $-2398.07 | -4.4% | $-1398.07 | -3.3 | done | losing for real |
| momentum_5m_0.00pct | 5453 | 50.2 | 51.3 | $-3378.25 | -6.2% | $-2378.25 | -4.7 | done | losing for real |
| always_up | 5453 | 48.0 | 49.2 | $-3589.25 | -6.6% | $-2589.25 | -4.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 9875 | 47.9 | 48.7 | $-5592.84 |
| ETH | 10631 | 48.1 | 47.9 | $-5422.24 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
