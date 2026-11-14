# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 14, 4:20 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 369 windows, 9997 settled trades, 51 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 189 | 38.1 | 36.4 | $+15.78 | +0.8% | $1015.78 | +0.1 | Sat 10:00 PM | too few trades (189/200) |
| value_ev10 | 485 | 41.0 | 40.4 | $-86.39 | -1.8% | $913.61 | -0.3 | done | can't tell from luck |
| value_ev5 | 716 | 42.3 | 42.1 | $-216.26 | -3.0% | $783.74 | -0.7 | done | can't tell from luck |
| momentum_60m_0.30pct | 827 | 49.6 | 49.7 | $-384.29 | -4.6% | $615.71 | -1.3 | done | can't tell from luck |
| trend_filter | 553 | 48.8 | 50.5 | $-415.29 | -7.5% | $584.71 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 995 | 51.6 | 52.1 | $-497.22 | -5.0% | $502.78 | -1.7 | done | can't tell from luck |
| reversal_60m_0.30pct | 827 | 50.4 | 52.1 | $-576.24 | -7.0% | $423.76 | -2.1 | done | losing for real |
| momentum_15m_0.10pct | 995 | 48.4 | 49.6 | $-595.25 | -6.0% | $404.75 | -1.9 | done | can't tell from luck |
| coinflip | 1470 | 49.7 | 50.8 | $-837.89 | -5.7% | $162.11 | -2.2 | done | losing for real |
| momentum_5m_0.00pct | 1470 | 49.5 | 51.5 | $-1078.99 | -7.3% | $-78.99 | -2.9 | done | losing for real |
| always_up | 1470 | 45.6 | 50.7 | $-1986.53 | -13.5% | $-986.53 | -5.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2243 | 47.3 | 49.3 | $-1776.00 |
| ETH | 2518 | 47.7 | 48.9 | $-1775.43 |
| SOL | 2586 | 48.0 | 49.5 | $-1808.98 |
| XRP | 2650 | 48.8 | 49.1 | $-1298.17 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
