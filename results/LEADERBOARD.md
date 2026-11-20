# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 20, 1:20 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 933 windows, 25807 settled trades, 44 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 476 | 35.1 | 34.8 | $-155.74 | -3.3% | $844.26 | -0.5 | done | can't tell from luck |
| value_ev10 | 1167 | 38.0 | 39.1 | $-692.90 | -5.9% | $307.10 | -1.6 | done | can't tell from luck |
| momentum_60m_0.30pct | 2201 | 50.2 | 49.8 | $-915.25 | -4.2% | $84.75 | -2.0 | done | can't tell from luck |
| reversal_15m_0.10pct | 2637 | 50.9 | 50.6 | $-917.98 | -3.5% | $82.02 | -1.8 | done | can't tell from luck |
| trend_filter | 1533 | 50.0 | 51.0 | $-1043.51 | -6.8% | $-43.51 | -2.7 | done | losing for real |
| value_ev5 | 1774 | 39.6 | 41.0 | $-1136.70 | -6.4% | $-136.70 | -2.3 | done | losing for real |
| reversal_60m_0.30pct | 2201 | 49.8 | 50.9 | $-1557.97 | -7.1% | $-557.97 | -3.4 | done | losing for real |
| coinflip | 3727 | 50.4 | 50.4 | $-1575.68 | -4.2% | $-575.68 | -2.6 | done | losing for real |
| momentum_15m_0.10pct | 2637 | 49.1 | 50.3 | $-1664.33 | -6.3% | $-664.33 | -3.3 | done | losing for real |
| momentum_5m_0.00pct | 3727 | 51.0 | 51.6 | $-1882.27 | -5.1% | $-882.27 | -3.2 | done | losing for real |
| always_up | 3727 | 46.7 | 49.7 | $-3862.98 | -10.4% | $-2862.98 | -6.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5877 | 48.1 | 49.1 | $-3456.04 |
| ETH | 6420 | 48.2 | 48.6 | $-4053.01 |
| SOL | 6734 | 48.1 | 48.6 | $-4009.99 |
| XRP | 6776 | 48.3 | 48.5 | $-3886.25 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
