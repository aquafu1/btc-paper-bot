# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 22, 10:50 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1115 windows, 30861 settled trades, 42 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 589 | 34.6 | 35.1 | $-339.77 | -5.8% | $660.23 | -1.1 | done | can't tell from luck |
| reversal_15m_0.10pct | 3113 | 51.2 | 50.5 | $-815.25 | -2.6% | $184.75 | -1.5 | done | can't tell from luck |
| value_ev10 | 1439 | 38.1 | 39.1 | $-881.17 | -6.1% | $118.83 | -1.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 2618 | 49.8 | 49.4 | $-1064.77 | -4.1% | $-64.77 | -2.1 | done | losing for real |
| value_ev5 | 2179 | 40.0 | 41.0 | $-1255.47 | -5.8% | $-255.47 | -2.3 | done | losing for real |
| trend_filter | 1827 | 49.2 | 50.4 | $-1378.65 | -7.5% | $-378.65 | -3.3 | done | losing for real |
| reversal_60m_0.30pct | 2618 | 50.2 | 51.1 | $-1703.70 | -6.5% | $-703.70 | -3.4 | done | losing for real |
| coinflip | 4455 | 50.4 | 50.2 | $-1735.72 | -3.9% | $-735.72 | -2.6 | done | losing for real |
| momentum_15m_0.10pct | 3113 | 48.8 | 50.2 | $-2086.00 | -6.7% | $-1086.00 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 4455 | 50.5 | 51.4 | $-2513.36 | -5.6% | $-1513.36 | -3.9 | done | losing for real |
| always_up | 4455 | 47.7 | 49.3 | $-3438.47 | -7.7% | $-2438.47 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7069 | 48.4 | 49.0 | $-3522.30 |
| ETH | 7646 | 48.1 | 48.4 | $-4651.15 |
| SOL | 8025 | 48.1 | 48.4 | $-4471.21 |
| XRP | 8121 | 48.2 | 48.2 | $-4567.67 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
