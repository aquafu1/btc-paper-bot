# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 21, 1:20 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 981 windows, 27282 settled trades, 33 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 502 | 34.5 | 34.9 | $-255.26 | -5.1% | $744.74 | -0.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 2788 | 51.2 | 50.5 | $-795.88 | -2.9% | $204.12 | -1.5 | done | can't tell from luck |
| value_ev10 | 1246 | 37.8 | 39.1 | $-797.53 | -6.4% | $202.47 | -1.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 2336 | 50.1 | 49.7 | $-938.66 | -4.0% | $61.34 | -1.9 | done | can't tell from luck |
| value_ev5 | 1886 | 39.8 | 41.0 | $-1144.87 | -6.1% | $-144.87 | -2.2 | done | losing for real |
| trend_filter | 1640 | 49.7 | 50.8 | $-1165.57 | -7.1% | $-165.57 | -3.0 | done | losing for real |
| reversal_60m_0.30pct | 2336 | 49.9 | 50.9 | $-1641.98 | -7.0% | $-641.98 | -3.5 | done | losing for real |
| coinflip | 3920 | 50.2 | 50.3 | $-1765.84 | -4.5% | $-765.84 | -2.8 | done | losing for real |
| momentum_15m_0.10pct | 2788 | 48.8 | 50.3 | $-1951.69 | -7.0% | $-951.69 | -3.7 | done | losing for real |
| momentum_5m_0.00pct | 3920 | 50.8 | 51.5 | $-2075.65 | -5.3% | $-1075.65 | -3.4 | done | losing for real |
| always_up | 3920 | 46.9 | 49.6 | $-3892.15 | -9.9% | $-2892.15 | -6.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6220 | 48.2 | 49.1 | $-3462.88 |
| ETH | 6782 | 48.0 | 48.5 | $-4414.06 |
| SOL | 7124 | 48.1 | 48.6 | $-4137.32 |
| XRP | 7156 | 48.2 | 48.5 | $-4410.83 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
