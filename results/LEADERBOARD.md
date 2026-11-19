# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 19, 1:15 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 789 windows, 21734 settled trades, 60 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 404 | 32.9 | 34.9 | $-391.45 | -9.7% | $608.55 | -1.5 | done | can't tell from luck |
| momentum_60m_0.30pct | 1842 | 50.3 | 49.6 | $-650.47 | -3.5% | $349.53 | -1.5 | done | can't tell from luck |
| trend_filter | 1279 | 50.5 | 50.8 | $-692.70 | -5.4% | $307.30 | -2.0 | done | can't tell from luck |
| value_ev10 | 989 | 37.4 | 39.1 | $-778.33 | -7.9% | $221.67 | -2.0 | done | losing for real |
| reversal_15m_0.10pct | 2219 | 50.8 | 50.6 | $-833.18 | -3.8% | $166.82 | -1.8 | done | can't tell from luck |
| value_ev5 | 1496 | 39.8 | 41.1 | $-1006.66 | -6.7% | $-6.66 | -2.2 | done | losing for real |
| coinflip | 3148 | 50.3 | 50.3 | $-1333.14 | -4.2% | $-333.14 | -2.4 | done | losing for real |
| momentum_15m_0.10pct | 2219 | 49.2 | 50.3 | $-1355.09 | -6.1% | $-355.09 | -2.9 | done | losing for real |
| reversal_60m_0.30pct | 1842 | 49.7 | 51.2 | $-1392.25 | -7.6% | $-392.25 | -3.3 | done | losing for real |
| momentum_5m_0.00pct | 3148 | 51.3 | 51.7 | $-1427.34 | -4.5% | $-427.34 | -2.6 | done | losing for real |
| always_up | 3148 | 47.6 | 49.6 | $-2607.03 | -8.3% | $-1607.03 | -4.6 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4935 | 48.3 | 49.1 | $-2950.67 |
| ETH | 5420 | 48.2 | 48.5 | $-3508.80 |
| SOL | 5661 | 48.3 | 48.6 | $-3157.15 |
| XRP | 5718 | 48.5 | 48.5 | $-2851.02 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
