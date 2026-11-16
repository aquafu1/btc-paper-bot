# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 15, 9:35 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 486 windows, 13371 settled trades, 47 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 247 | 34.8 | 35.8 | $-149.21 | -6.0% | $850.79 | -0.7 | done | can't tell from luck |
| momentum_60m_0.30pct | 1138 | 51.1 | 49.8 | $-186.36 | -1.6% | $813.64 | -0.6 | done | can't tell from luck |
| value_ev10 | 631 | 38.8 | 40.1 | $-390.56 | -6.2% | $609.44 | -1.3 | done | can't tell from luck |
| momentum_15m_0.10pct | 1346 | 50.1 | 49.9 | $-433.21 | -3.2% | $566.79 | -1.2 | done | can't tell from luck |
| value_ev5 | 930 | 40.9 | 41.8 | $-516.74 | -5.6% | $483.26 | -1.4 | done | can't tell from luck |
| trend_filter | 784 | 49.5 | 50.7 | $-517.15 | -6.6% | $482.85 | -1.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 1346 | 49.9 | 51.6 | $-961.77 | -7.1% | $38.23 | -2.7 | done | losing for real |
| coinflip | 1937 | 50.0 | 50.8 | $-1019.15 | -5.3% | $-19.15 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 1138 | 48.9 | 51.5 | $-1048.94 | -9.2% | $-48.94 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 1937 | 49.6 | 51.7 | $-1457.38 | -7.5% | $-457.38 | -3.4 | done | losing for real |
| always_up | 1937 | 46.5 | 50.4 | $-2226.57 | -11.5% | $-1226.57 | -5.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3016 | 47.4 | 49.3 | $-2416.07 |
| ETH | 3350 | 48.1 | 48.8 | $-2164.68 |
| SOL | 3487 | 47.8 | 49.3 | $-2478.93 |
| XRP | 3518 | 48.5 | 49.0 | $-1847.35 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
