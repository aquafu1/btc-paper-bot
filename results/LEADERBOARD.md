# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 20, 9:45 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 967 windows, 26785 settled trades, 77 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 494 | 34.8 | 34.9 | $-199.50 | -4.0% | $800.50 | -0.7 | done | can't tell from luck |
| value_ev10 | 1222 | 38.1 | 39.1 | $-699.05 | -5.7% | $300.95 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 2734 | 51.3 | 50.5 | $-707.56 | -2.6% | $292.44 | -1.4 | done | can't tell from luck |
| momentum_60m_0.30pct | 2284 | 50.2 | 49.8 | $-881.88 | -3.9% | $118.12 | -1.8 | done | can't tell from luck |
| trend_filter | 1600 | 49.9 | 50.9 | $-1065.98 | -6.7% | $-65.98 | -2.7 | done | losing for real |
| value_ev5 | 1853 | 39.9 | 41.0 | $-1072.06 | -5.8% | $-72.06 | -2.1 | done | losing for real |
| reversal_60m_0.30pct | 2284 | 49.8 | 51.0 | $-1619.74 | -7.1% | $-619.74 | -3.5 | done | losing for real |
| coinflip | 3860 | 50.2 | 50.4 | $-1750.60 | -4.5% | $-750.60 | -2.8 | done | losing for real |
| momentum_15m_0.10pct | 2734 | 48.7 | 50.3 | $-1948.11 | -7.1% | $-948.11 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 3860 | 50.9 | 51.6 | $-2008.95 | -5.2% | $-1008.95 | -3.3 | done | losing for real |
| always_up | 3860 | 46.8 | 49.6 | $-3809.88 | -9.9% | $-2809.88 | -6.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6102 | 48.2 | 49.1 | $-3489.91 |
| ETH | 6654 | 48.1 | 48.5 | $-4144.25 |
| SOL | 6996 | 48.2 | 48.6 | $-3827.68 |
| XRP | 7033 | 48.2 | 48.5 | $-4301.47 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
