# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 15, 9:30 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 486 windows, 13365 settled trades, 53 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 247 | 34.8 | 35.8 | $-149.21 | -6.0% | $850.79 | -0.7 | done | can't tell from luck |
| momentum_60m_0.30pct | 1137 | 51.1 | 49.8 | $-176.36 | -1.6% | $823.64 | -0.5 | done | can't tell from luck |
| value_ev10 | 631 | 38.8 | 40.1 | $-390.56 | -6.2% | $609.44 | -1.3 | done | can't tell from luck |
| momentum_15m_0.10pct | 1346 | 50.1 | 49.9 | $-433.21 | -3.2% | $566.79 | -1.2 | done | can't tell from luck |
| trend_filter | 783 | 49.6 | 50.7 | $-507.15 | -6.5% | $492.85 | -1.9 | done | can't tell from luck |
| value_ev5 | 930 | 40.9 | 41.8 | $-516.74 | -5.6% | $483.26 | -1.4 | done | can't tell from luck |
| reversal_15m_0.10pct | 1346 | 49.9 | 51.6 | $-961.77 | -7.1% | $38.23 | -2.7 | done | losing for real |
| coinflip | 1936 | 49.9 | 50.8 | $-1028.17 | -5.3% | $-28.17 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 1137 | 48.9 | 51.5 | $-1057.97 | -9.3% | $-57.97 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 1936 | 49.6 | 51.7 | $-1447.38 | -7.5% | $-447.38 | -3.4 | done | losing for real |
| always_up | 1936 | 46.5 | 50.4 | $-2216.57 | -11.4% | $-1216.57 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3016 | 47.4 | 49.3 | $-2416.07 |
| ETH | 3350 | 48.1 | 48.8 | $-2164.68 |
| SOL | 3481 | 47.8 | 49.3 | $-2456.99 |
| XRP | 3518 | 48.5 | 49.0 | $-1847.35 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
