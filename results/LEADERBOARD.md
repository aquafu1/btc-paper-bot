# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 18, 1:45 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 695 windows, 19218 settled trades, 43 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 369 | 34.1 | 34.9 | $-239.86 | -6.5% | $760.14 | -0.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 1619 | 50.4 | 49.5 | $-432.62 | -2.7% | $567.38 | -1.1 | done | can't tell from luck |
| value_ev10 | 891 | 38.4 | 39.1 | $-504.89 | -5.7% | $495.11 | -1.4 | done | can't tell from luck |
| value_ev5 | 1339 | 40.9 | 41.1 | $-570.11 | -4.3% | $429.89 | -1.3 | done | can't tell from luck |
| reversal_15m_0.10pct | 1972 | 51.4 | 50.8 | $-578.08 | -2.9% | $421.92 | -1.3 | done | can't tell from luck |
| trend_filter | 1121 | 50.4 | 50.9 | $-595.66 | -5.3% | $404.34 | -1.8 | done | can't tell from luck |
| reversal_60m_0.30pct | 1619 | 49.6 | 51.3 | $-1270.59 | -7.8% | $-270.59 | -3.2 | done | losing for real |
| coinflip | 2772 | 50.0 | 50.3 | $-1270.94 | -4.6% | $-270.94 | -2.4 | done | losing for real |
| momentum_15m_0.10pct | 1972 | 48.6 | 50.0 | $-1314.21 | -6.7% | $-314.21 | -3.0 | done | losing for real |
| momentum_5m_0.00pct | 2772 | 50.8 | 51.8 | $-1498.94 | -5.4% | $-498.94 | -2.9 | done | losing for real |
| always_up | 2772 | 47.4 | 49.5 | $-2326.77 | -8.4% | $-1326.77 | -4.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4356 | 48.2 | 49.1 | $-2513.88 |
| ETH | 4787 | 48.2 | 48.5 | $-2734.07 |
| SOL | 5014 | 48.1 | 48.6 | $-2922.12 |
| XRP | 5061 | 48.6 | 48.3 | $-2432.60 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
