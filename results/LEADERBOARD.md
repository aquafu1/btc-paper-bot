# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 23, 4:05 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1184 windows, 32730 settled trades, 49 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 638 | 35.0 | 35.3 | $-353.40 | -5.5% | $646.60 | -1.1 | done | can't tell from luck |
| value_ev10 | 1551 | 38.6 | 39.2 | $-775.47 | -5.0% | $224.53 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 3279 | 50.7 | 50.3 | $-1092.39 | -3.3% | $-92.39 | -1.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 2757 | 49.6 | 49.4 | $-1235.21 | -4.5% | $-235.21 | -2.3 | done | losing for real |
| value_ev5 | 2348 | 40.3 | 41.1 | $-1263.78 | -5.4% | $-263.78 | -2.2 | done | losing for real |
| trend_filter | 1937 | 48.8 | 50.5 | $-1605.94 | -8.3% | $-605.94 | -3.7 | done | losing for real |
| reversal_60m_0.30pct | 2757 | 50.4 | 51.1 | $-1677.20 | -6.1% | $-677.20 | -3.3 | done | losing for real |
| momentum_15m_0.10pct | 3279 | 49.3 | 50.2 | $-1975.97 | -6.0% | $-975.97 | -3.5 | done | losing for real |
| coinflip | 4728 | 50.1 | 50.2 | $-2124.80 | -4.5% | $-1124.80 | -3.1 | done | losing for real |
| momentum_5m_0.00pct | 4728 | 50.1 | 51.4 | $-3005.72 | -6.4% | $-2005.72 | -4.5 | done | losing for real |
| always_up | 4728 | 47.9 | 49.3 | $-3416.75 | -7.2% | $-2416.75 | -4.9 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7507 | 48.2 | 48.9 | $-4115.09 |
| ETH | 8115 | 48.1 | 48.4 | $-4890.89 |
| SOL | 8514 | 48.2 | 48.4 | $-4436.68 |
| XRP | 8594 | 48.1 | 48.2 | $-5083.98 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
