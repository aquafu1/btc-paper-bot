# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 20, 4:20 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 945 windows, 26194 settled trades, 42 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 483 | 35.0 | 34.9 | $-173.29 | -3.6% | $826.71 | -0.6 | done | can't tell from luck |
| value_ev10 | 1188 | 38.0 | 39.1 | $-680.60 | -5.7% | $319.40 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 2677 | 51.1 | 50.6 | $-858.62 | -3.2% | $141.38 | -1.7 | done | can't tell from luck |
| momentum_60m_0.30pct | 2240 | 50.1 | 49.8 | $-932.09 | -4.2% | $67.91 | -2.0 | done | can't tell from luck |
| trend_filter | 1559 | 50.0 | 50.9 | $-1049.51 | -6.7% | $-49.51 | -2.7 | done | losing for real |
| value_ev5 | 1805 | 39.8 | 41.0 | $-1069.56 | -5.9% | $-69.56 | -2.1 | done | losing for real |
| coinflip | 3775 | 50.4 | 50.3 | $-1576.01 | -4.2% | $-576.01 | -2.6 | done | losing for real |
| reversal_60m_0.30pct | 2240 | 49.9 | 51.0 | $-1580.17 | -7.1% | $-580.17 | -3.4 | done | losing for real |
| momentum_15m_0.10pct | 2677 | 48.9 | 50.2 | $-1774.71 | -6.6% | $-774.71 | -3.5 | done | losing for real |
| momentum_5m_0.00pct | 3775 | 51.0 | 51.6 | $-1892.72 | -5.0% | $-892.72 | -3.2 | done | losing for real |
| always_up | 3775 | 46.8 | 49.6 | $-3795.37 | -10.1% | $-2795.37 | -6.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5966 | 48.2 | 49.0 | $-3446.93 |
| ETH | 6519 | 48.2 | 48.5 | $-4040.51 |
| SOL | 6830 | 48.2 | 48.6 | $-3852.05 |
| XRP | 6879 | 48.3 | 48.5 | $-4043.15 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
