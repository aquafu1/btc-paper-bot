# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 20, 6:45 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 907 windows, 25036 settled trades, 57 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 467 | 35.3 | 34.9 | $-131.30 | -2.8% | $868.70 | -0.5 | done | can't tell from luck |
| value_ev10 | 1147 | 38.3 | 39.1 | $-603.08 | -5.3% | $396.92 | -1.4 | done | can't tell from luck |
| momentum_60m_0.30pct | 2118 | 49.8 | 49.8 | $-984.86 | -4.6% | $15.14 | -2.1 | done | losing for real |
| value_ev5 | 1734 | 40.0 | 41.0 | $-987.46 | -5.7% | $12.54 | -2.0 | done | can't tell from luck |
| trend_filter | 1486 | 49.8 | 51.0 | $-1046.14 | -7.0% | $-46.14 | -2.8 | done | losing for real |
| reversal_15m_0.10pct | 2553 | 50.5 | 50.5 | $-1046.28 | -4.1% | $-46.28 | -2.1 | done | losing for real |
| reversal_60m_0.30pct | 2118 | 50.2 | 50.9 | $-1327.83 | -6.3% | $-327.83 | -2.9 | done | losing for real |
| momentum_15m_0.10pct | 2553 | 49.5 | 50.3 | $-1367.49 | -5.4% | $-367.49 | -2.7 | done | losing for real |
| coinflip | 3620 | 50.2 | 50.3 | $-1598.62 | -4.4% | $-598.62 | -2.7 | done | losing for real |
| momentum_5m_0.00pct | 3620 | 51.1 | 51.7 | $-1691.31 | -4.7% | $-691.31 | -2.9 | done | losing for real |
| always_up | 3620 | 46.9 | 49.7 | $-3568.85 | -9.9% | $-2568.85 | -5.9 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5706 | 48.2 | 49.1 | $-3127.98 |
| ETH | 6224 | 48.2 | 48.5 | $-3769.57 |
| SOL | 6533 | 48.1 | 48.6 | $-3770.48 |
| XRP | 6573 | 48.3 | 48.5 | $-3685.19 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
