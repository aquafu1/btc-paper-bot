# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 17, 9:00 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 628 windows, 17356 settled trades, 46 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1465 | 51.2 | 49.5 | $-167.87 | -1.1% | $832.13 | -0.4 | done | can't tell from luck |
| value_ev20 | 330 | 33.9 | 35.3 | $-274.70 | -8.3% | $725.30 | -1.2 | done | can't tell from luck |
| trend_filter | 1006 | 50.1 | 50.8 | $-573.57 | -5.7% | $426.43 | -1.8 | done | can't tell from luck |
| value_ev10 | 803 | 38.2 | 39.5 | $-590.20 | -7.3% | $409.80 | -1.7 | done | can't tell from luck |
| value_ev5 | 1215 | 40.5 | 41.4 | $-755.19 | -6.2% | $244.81 | -1.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 1780 | 50.8 | 51.0 | $-832.86 | -4.7% | $167.14 | -2.0 | done | losing for real |
| momentum_15m_0.10pct | 1780 | 49.2 | 49.9 | $-987.72 | -5.5% | $12.28 | -2.3 | done | losing for real |
| coinflip | 2504 | 50.0 | 50.5 | $-1219.98 | -4.9% | $-219.98 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 1465 | 48.8 | 51.4 | $-1410.24 | -9.6% | $-410.24 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 2504 | 50.2 | 51.7 | $-1605.50 | -6.4% | $-605.50 | -3.3 | done | losing for real |
| always_up | 2504 | 47.4 | 49.6 | $-2134.60 | -8.5% | $-1134.60 | -4.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3939 | 48.2 | 49.2 | $-2458.96 |
| ETH | 4342 | 48.1 | 48.6 | $-2678.81 |
| SOL | 4507 | 47.9 | 48.8 | $-3045.64 |
| XRP | 4568 | 48.4 | 48.5 | $-2369.04 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
