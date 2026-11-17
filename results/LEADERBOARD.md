# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 16, 6:00 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 568 windows, 15743 settled trades, 52 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1338 | 51.4 | 49.7 | $-201.06 | -1.5% | $798.94 | -0.6 | done | can't tell from luck |
| value_ev20 | 309 | 33.3 | 35.2 | $-327.95 | -10.6% | $672.05 | -1.4 | done | can't tell from luck |
| trend_filter | 915 | 50.6 | 51.1 | $-499.11 | -5.5% | $500.89 | -1.7 | done | can't tell from luck |
| value_ev10 | 746 | 37.5 | 39.4 | $-698.44 | -9.4% | $301.56 | -2.1 | done | losing for real |
| reversal_15m_0.10pct | 1598 | 50.8 | 51.0 | $-837.56 | -5.2% | $162.44 | -2.1 | done | losing for real |
| value_ev5 | 1109 | 39.8 | 41.3 | $-868.84 | -7.8% | $131.16 | -2.2 | done | losing for real |
| momentum_15m_0.10pct | 1598 | 49.2 | 49.9 | $-886.92 | -5.6% | $113.08 | -2.2 | done | losing for real |
| coinflip | 2264 | 49.8 | 50.5 | $-1242.60 | -5.5% | $-242.60 | -2.6 | done | losing for real |
| reversal_60m_0.30pct | 1338 | 48.6 | 51.2 | $-1352.92 | -10.1% | $-352.92 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 2264 | 50.2 | 51.9 | $-1610.39 | -7.1% | $-610.39 | -3.5 | done | losing for real |
| always_up | 2264 | 47.1 | 49.9 | $-2251.48 | -9.9% | $-1251.48 | -4.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3556 | 47.7 | 49.2 | $-2742.32 |
| ETH | 3927 | 47.9 | 48.6 | $-2780.39 |
| SOL | 4108 | 47.8 | 48.7 | $-3041.06 |
| XRP | 4152 | 48.6 | 48.6 | $-2213.50 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
