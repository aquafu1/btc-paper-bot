# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 18, 2:00 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 696 windows, 19239 settled trades, 56 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 369 | 34.1 | 34.9 | $-239.86 | -6.5% | $760.14 | -0.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 1620 | 50.4 | 49.5 | $-442.62 | -2.7% | $557.38 | -1.1 | done | can't tell from luck |
| value_ev10 | 891 | 38.4 | 39.1 | $-504.89 | -5.7% | $495.11 | -1.4 | done | can't tell from luck |
| value_ev5 | 1339 | 40.9 | 41.1 | $-570.11 | -4.3% | $429.89 | -1.3 | done | can't tell from luck |
| reversal_15m_0.10pct | 1975 | 51.4 | 50.8 | $-590.47 | -3.0% | $409.53 | -1.3 | done | can't tell from luck |
| trend_filter | 1122 | 50.4 | 50.9 | $-605.66 | -5.4% | $394.34 | -1.8 | done | can't tell from luck |
| coinflip | 2776 | 50.1 | 50.3 | $-1241.56 | -4.5% | $-241.56 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 1620 | 49.6 | 51.3 | $-1262.98 | -7.8% | $-262.98 | -3.2 | done | losing for real |
| momentum_15m_0.10pct | 1975 | 48.6 | 50.0 | $-1310.36 | -6.6% | $-310.36 | -3.0 | done | losing for real |
| momentum_5m_0.00pct | 2776 | 50.9 | 51.8 | $-1487.16 | -5.4% | $-487.16 | -2.9 | done | losing for real |
| always_up | 2776 | 47.3 | 49.5 | $-2366.77 | -8.5% | $-1366.77 | -4.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4359 | 48.2 | 49.1 | $-2508.03 |
| ETH | 4792 | 48.2 | 48.5 | $-2734.69 |
| SOL | 5019 | 48.1 | 48.6 | $-2919.95 |
| XRP | 5069 | 48.6 | 48.4 | $-2459.77 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
