# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 16, 9:50 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 535 windows, 14806 settled trades, 48 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1265 | 51.6 | 49.8 | $-101.48 | -0.8% | $898.52 | -0.3 | done | can't tell from luck |
| value_ev20 | 281 | 34.5 | 35.5 | $-222.64 | -7.9% | $777.36 | -1.0 | done | can't tell from luck |
| trend_filter | 867 | 50.4 | 50.8 | $-445.28 | -5.1% | $554.72 | -1.5 | done | can't tell from luck |
| momentum_15m_0.10pct | 1501 | 50.1 | 49.8 | $-536.03 | -3.6% | $463.97 | -1.4 | done | can't tell from luck |
| value_ev10 | 692 | 37.9 | 39.7 | $-600.63 | -8.7% | $399.37 | -1.9 | done | can't tell from luck |
| value_ev5 | 1032 | 40.0 | 41.5 | $-776.07 | -7.5% | $223.93 | -2.1 | done | losing for real |
| reversal_15m_0.10pct | 1501 | 49.9 | 51.3 | $-1109.34 | -7.4% | $-109.34 | -2.9 | done | losing for real |
| coinflip | 2134 | 49.9 | 50.6 | $-1214.25 | -5.7% | $-214.25 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 1265 | 48.4 | 51.3 | $-1296.09 | -10.2% | $-296.09 | -3.7 | done | losing for real |
| momentum_5m_0.00pct | 2134 | 49.9 | 51.7 | $-1556.55 | -7.3% | $-556.55 | -3.5 | done | losing for real |
| always_up | 2134 | 46.5 | 50.1 | $-2431.22 | -11.4% | $-1431.22 | -5.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3354 | 47.5 | 49.3 | $-2689.16 |
| ETH | 3689 | 48.0 | 48.7 | $-2453.51 |
| SOL | 3863 | 47.7 | 48.9 | $-2871.82 |
| XRP | 3900 | 48.4 | 48.8 | $-2275.09 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
