# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 20, 1:30 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 934 windows, 25815 settled trades, 61 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 476 | 35.1 | 34.8 | $-155.74 | -3.3% | $844.26 | -0.5 | done | can't tell from luck |
| value_ev10 | 1167 | 38.0 | 39.1 | $-692.90 | -5.9% | $307.10 | -1.6 | done | can't tell from luck |
| momentum_60m_0.30pct | 2202 | 50.2 | 49.8 | $-909.55 | -4.1% | $90.45 | -1.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 2638 | 50.9 | 50.6 | $-927.98 | -3.5% | $72.02 | -1.8 | done | can't tell from luck |
| trend_filter | 1534 | 50.1 | 51.0 | $-1037.81 | -6.8% | $-37.81 | -2.7 | done | losing for real |
| value_ev5 | 1774 | 39.6 | 41.0 | $-1136.70 | -6.4% | $-136.70 | -2.3 | done | losing for real |
| reversal_60m_0.30pct | 2202 | 49.8 | 50.9 | $-1567.97 | -7.1% | $-567.97 | -3.4 | done | losing for real |
| coinflip | 3728 | 50.4 | 50.4 | $-1585.68 | -4.3% | $-585.68 | -2.6 | done | losing for real |
| momentum_15m_0.10pct | 2638 | 49.1 | 50.3 | $-1658.63 | -6.3% | $-658.63 | -3.3 | done | losing for real |
| momentum_5m_0.00pct | 3728 | 51.0 | 51.6 | $-1876.57 | -5.0% | $-876.57 | -3.2 | done | losing for real |
| always_up | 3728 | 46.7 | 49.7 | $-3872.98 | -10.4% | $-2872.98 | -6.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5885 | 48.1 | 49.1 | $-3473.24 |
| ETH | 6420 | 48.2 | 48.6 | $-4053.01 |
| SOL | 6734 | 48.1 | 48.6 | $-4009.99 |
| XRP | 6776 | 48.3 | 48.5 | $-3886.25 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
