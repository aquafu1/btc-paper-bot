# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 28, 4:45 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1667 windows, 39561 settled trades, 365 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 845 | 34.3 | 35.2 | $-644.92 | -7.6% | $355.08 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 3885 | 50.8 | 49.9 | $-994.49 | -2.6% | $5.51 | -1.6 | done | can't tell from luck |
| value_ev10 | 1995 | 38.3 | 39.0 | $-1150.05 | -5.8% | $-150.05 | -2.1 | done | losing for real |
| reversal_60m_0.30pct | 3244 | 51.1 | 50.9 | $-1434.75 | -4.4% | $-434.75 | -2.6 | done | losing for real |
| value_ev5 | 2978 | 40.3 | 41.0 | $-1645.89 | -5.5% | $-645.89 | -2.6 | done | losing for real |
| momentum_60m_0.30pct | 3244 | 48.9 | 49.3 | $-1824.73 | -5.6% | $-824.73 | -3.2 | done | losing for real |
| trend_filter | 2313 | 48.3 | 50.3 | $-2144.17 | -9.3% | $-1144.17 | -4.6 | done | losing for real |
| momentum_15m_0.10pct | 3885 | 49.2 | 50.2 | $-2391.90 | -6.2% | $-1391.90 | -3.9 | done | losing for real |
| coinflip | 5724 | 49.9 | 49.9 | $-2524.49 | -4.4% | $-1524.49 | -3.3 | done | losing for real |
| always_up | 5724 | 48.3 | 49.0 | $-3540.65 | -6.2% | $-2540.65 | -4.6 | done | losing for real |
| momentum_5m_0.00pct | 5724 | 50.1 | 51.3 | $-3590.51 | -6.3% | $-2590.51 | -4.9 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 10676 | 47.9 | 48.5 | $-6068.36 |
| ETH | 11575 | 47.8 | 47.6 | $-6233.97 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
