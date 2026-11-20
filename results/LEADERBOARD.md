# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 20, 9:35 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 918 windows, 25359 settled trades, 46 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 475 | 35.2 | 34.8 | $-145.74 | -3.1% | $854.26 | -0.5 | done | can't tell from luck |
| value_ev10 | 1159 | 38.1 | 39.0 | $-632.58 | -5.5% | $367.42 | -1.5 | done | can't tell from luck |
| momentum_60m_0.30pct | 2150 | 50.1 | 49.8 | $-872.82 | -4.1% | $127.18 | -1.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 2582 | 50.6 | 50.5 | $-996.42 | -3.9% | $3.58 | -2.0 | done | can't tell from luck |
| trend_filter | 1506 | 50.1 | 51.0 | $-1001.44 | -6.6% | $-1.44 | -2.7 | done | losing for real |
| value_ev5 | 1757 | 39.8 | 40.9 | $-1049.51 | -6.0% | $-49.51 | -2.1 | done | losing for real |
| momentum_15m_0.10pct | 2582 | 49.4 | 50.3 | $-1459.39 | -5.7% | $-459.39 | -2.9 | done | losing for real |
| reversal_60m_0.30pct | 2150 | 49.9 | 50.9 | $-1499.26 | -7.0% | $-499.26 | -3.3 | done | losing for real |
| coinflip | 3666 | 50.3 | 50.3 | $-1547.15 | -4.2% | $-547.15 | -2.6 | done | losing for real |
| momentum_5m_0.00pct | 3666 | 51.1 | 51.6 | $-1784.05 | -4.9% | $-784.05 | -3.0 | done | losing for real |
| always_up | 3666 | 46.8 | 49.7 | $-3701.63 | -10.1% | $-2701.63 | -6.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5770 | 48.2 | 49.0 | $-3279.30 |
| ETH | 6311 | 48.2 | 48.5 | $-3902.63 |
| SOL | 6620 | 48.2 | 48.6 | $-3818.45 |
| XRP | 6658 | 48.3 | 48.5 | $-3689.62 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
