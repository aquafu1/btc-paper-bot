# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 20, 9:30 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 918 windows, 25342 settled trades, 63 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 475 | 35.2 | 34.8 | $-145.74 | -3.1% | $854.26 | -0.5 | done | can't tell from luck |
| value_ev10 | 1159 | 38.1 | 39.0 | $-632.58 | -5.5% | $367.42 | -1.5 | done | can't tell from luck |
| momentum_60m_0.30pct | 2148 | 50.1 | 49.8 | $-886.94 | -4.1% | $113.06 | -1.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 2580 | 50.7 | 50.5 | $-976.42 | -3.8% | $23.58 | -1.9 | done | can't tell from luck |
| trend_filter | 1504 | 50.0 | 51.0 | $-1015.56 | -6.8% | $-15.56 | -2.7 | done | losing for real |
| value_ev5 | 1756 | 39.7 | 40.9 | $-1057.43 | -6.0% | $-57.43 | -2.1 | done | losing for real |
| momentum_15m_0.10pct | 2580 | 49.3 | 50.3 | $-1473.51 | -5.7% | $-473.51 | -2.9 | done | losing for real |
| reversal_60m_0.30pct | 2148 | 49.9 | 50.9 | $-1479.26 | -6.9% | $-479.26 | -3.3 | done | losing for real |
| coinflip | 3664 | 50.3 | 50.3 | $-1561.28 | -4.3% | $-561.28 | -2.6 | done | losing for real |
| momentum_5m_0.00pct | 3664 | 51.0 | 51.6 | $-1798.17 | -4.9% | $-798.17 | -3.1 | done | losing for real |
| always_up | 3664 | 46.8 | 49.7 | $-3681.63 | -10.0% | $-2681.63 | -6.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5770 | 48.2 | 49.0 | $-3279.30 |
| ETH | 6302 | 48.1 | 48.5 | $-3920.16 |
| SOL | 6612 | 48.2 | 48.6 | $-3819.45 |
| XRP | 6658 | 48.3 | 48.5 | $-3689.62 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
