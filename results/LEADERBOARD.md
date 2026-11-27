# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 26, 6:20 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1529 windows, 37800 settled trades, 350 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 767 | 34.7 | 35.4 | $-526.25 | -6.9% | $473.75 | -1.5 | done | can't tell from luck |
| value_ev10 | 1849 | 38.6 | 39.2 | $-939.85 | -5.1% | $60.15 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 3754 | 50.9 | 50.0 | $-961.58 | -2.6% | $38.42 | -1.6 | done | can't tell from luck |
| value_ev5 | 2790 | 40.6 | 41.1 | $-1349.08 | -4.8% | $-349.08 | -2.2 | done | losing for real |
| reversal_60m_0.30pct | 3149 | 51.1 | 51.0 | $-1456.61 | -4.6% | $-456.61 | -2.7 | done | losing for real |
| momentum_60m_0.30pct | 3149 | 48.9 | 49.2 | $-1692.90 | -5.4% | $-692.90 | -3.0 | done | losing for real |
| trend_filter | 2238 | 48.6 | 50.3 | $-1919.10 | -8.6% | $-919.10 | -4.1 | done | losing for real |
| momentum_15m_0.10pct | 3754 | 49.1 | 50.2 | $-2343.21 | -6.2% | $-1343.21 | -3.9 | done | losing for real |
| coinflip | 5450 | 50.0 | 50.0 | $-2382.49 | -4.4% | $-1382.49 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 5450 | 50.2 | 51.3 | $-3362.66 | -6.2% | $-2362.66 | -4.7 | done | losing for real |
| always_up | 5450 | 48.0 | 49.1 | $-3587.36 | -6.6% | $-2587.36 | -4.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 9865 | 48.0 | 48.7 | $-5531.40 |
| ETH | 10625 | 48.1 | 47.9 | $-5405.48 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
