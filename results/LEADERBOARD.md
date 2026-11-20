# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 20, 4:30 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 946 windows, 26203 settled trades, 72 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 483 | 35.0 | 34.9 | $-173.29 | -3.6% | $826.71 | -0.6 | done | can't tell from luck |
| value_ev10 | 1188 | 38.0 | 39.1 | $-680.60 | -5.7% | $319.40 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 2678 | 51.1 | 50.6 | $-843.45 | -3.1% | $156.55 | -1.6 | done | can't tell from luck |
| momentum_60m_0.30pct | 2241 | 50.1 | 49.8 | $-916.91 | -4.1% | $83.09 | -1.9 | done | can't tell from luck |
| trend_filter | 1560 | 50.0 | 50.9 | $-1034.33 | -6.6% | $-34.33 | -2.7 | done | losing for real |
| value_ev5 | 1806 | 39.9 | 41.0 | $-1054.38 | -5.8% | $-54.38 | -2.1 | done | losing for real |
| coinflip | 3776 | 50.4 | 50.3 | $-1586.01 | -4.2% | $-586.01 | -2.6 | done | losing for real |
| reversal_60m_0.30pct | 2241 | 49.9 | 51.0 | $-1590.17 | -7.1% | $-590.17 | -3.4 | done | losing for real |
| momentum_15m_0.10pct | 2678 | 48.9 | 50.2 | $-1784.71 | -6.7% | $-784.71 | -3.5 | done | losing for real |
| momentum_5m_0.00pct | 3776 | 51.0 | 51.6 | $-1877.55 | -5.0% | $-877.55 | -3.2 | done | losing for real |
| always_up | 3776 | 46.8 | 49.6 | $-3780.19 | -10.0% | $-2780.19 | -6.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5975 | 48.2 | 49.0 | $-3385.88 |
| ETH | 6519 | 48.2 | 48.5 | $-4040.51 |
| SOL | 6830 | 48.2 | 48.6 | $-3852.05 |
| XRP | 6879 | 48.3 | 48.5 | $-4043.15 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
