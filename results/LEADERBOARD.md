# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 18, 11:00 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 732 windows, 20151 settled trades, 69 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 381 | 33.3 | 34.9 | $-334.03 | -8.8% | $665.97 | -1.3 | done | can't tell from luck |
| reversal_15m_0.10pct | 2066 | 51.5 | 50.7 | $-497.55 | -2.4% | $502.45 | -1.1 | done | can't tell from luck |
| momentum_60m_0.30pct | 1692 | 50.4 | 49.6 | $-498.27 | -2.9% | $501.73 | -1.2 | done | can't tell from luck |
| value_ev10 | 920 | 38.0 | 39.1 | $-595.30 | -6.5% | $404.70 | -1.6 | done | can't tell from luck |
| trend_filter | 1184 | 50.3 | 51.0 | $-680.04 | -5.7% | $319.96 | -2.0 | done | losing for real |
| value_ev5 | 1390 | 40.6 | 41.1 | $-710.36 | -5.1% | $289.64 | -1.6 | done | can't tell from luck |
| coinflip | 2920 | 50.2 | 50.3 | $-1222.01 | -4.2% | $-222.01 | -2.3 | done | losing for real |
| reversal_60m_0.30pct | 1692 | 49.6 | 51.2 | $-1298.54 | -7.7% | $-298.54 | -3.2 | done | losing for real |
| momentum_15m_0.10pct | 2066 | 48.5 | 50.1 | $-1453.11 | -7.0% | $-453.11 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 2920 | 50.9 | 51.8 | $-1588.92 | -5.4% | $-588.92 | -3.0 | done | losing for real |
| always_up | 2920 | 46.9 | 49.6 | $-2745.04 | -9.4% | $-1745.04 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4563 | 48.1 | 49.1 | $-2867.46 |
| ETH | 5021 | 48.2 | 48.5 | $-3070.41 |
| SOL | 5247 | 48.1 | 48.7 | $-3089.74 |
| XRP | 5320 | 48.5 | 48.5 | $-2595.55 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
