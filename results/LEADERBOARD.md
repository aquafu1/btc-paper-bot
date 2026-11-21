# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 21, 3:20 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 989 windows, 27510 settled trades, 34 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 505 | 34.3 | 34.9 | $-285.26 | -5.6% | $714.74 | -0.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 2809 | 51.1 | 50.4 | $-848.21 | -3.0% | $151.79 | -1.6 | done | can't tell from luck |
| value_ev10 | 1257 | 37.5 | 39.1 | $-881.38 | -7.0% | $118.62 | -2.0 | done | losing for real |
| momentum_60m_0.30pct | 2364 | 49.8 | 49.7 | $-1083.32 | -4.6% | $-83.32 | -2.2 | done | losing for real |
| trend_filter | 1647 | 49.6 | 50.9 | $-1202.65 | -7.3% | $-202.65 | -3.0 | done | losing for real |
| value_ev5 | 1902 | 39.5 | 41.0 | $-1257.79 | -6.6% | $-257.79 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 2364 | 50.2 | 50.9 | $-1537.20 | -6.5% | $-537.20 | -3.2 | done | losing for real |
| coinflip | 3951 | 50.2 | 50.3 | $-1785.60 | -4.5% | $-785.60 | -2.9 | done | losing for real |
| momentum_15m_0.10pct | 2809 | 48.9 | 50.4 | $-1919.83 | -6.8% | $-919.83 | -3.7 | done | losing for real |
| momentum_5m_0.00pct | 3951 | 50.8 | 51.5 | $-2067.06 | -5.2% | $-1067.06 | -3.4 | done | losing for real |
| always_up | 3951 | 46.8 | 49.6 | $-3958.05 | -10.0% | $-2958.05 | -6.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6275 | 48.2 | 49.1 | $-3572.52 |
| ETH | 6835 | 48.0 | 48.5 | $-4489.38 |
| SOL | 7189 | 48.1 | 48.6 | $-4234.68 |
| XRP | 7211 | 48.1 | 48.5 | $-4529.77 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
