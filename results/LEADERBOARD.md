# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 25, 9:15 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1445 windows, 36714 settled trades, 397 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 740 | 34.5 | 35.3 | $-533.47 | -7.2% | $466.53 | -1.5 | done | can't tell from luck |
| value_ev10 | 1786 | 38.8 | 39.2 | $-806.32 | -4.5% | $193.68 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 3664 | 50.9 | 50.0 | $-983.79 | -2.7% | $16.21 | -1.6 | done | can't tell from luck |
| value_ev5 | 2691 | 40.5 | 41.1 | $-1302.34 | -4.8% | $-302.34 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 3076 | 49.2 | 49.2 | $-1519.80 | -4.9% | $-519.80 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 3076 | 50.8 | 51.0 | $-1572.86 | -5.1% | $-572.86 | -2.9 | done | losing for real |
| trend_filter | 2177 | 48.6 | 50.3 | $-1887.44 | -8.7% | $-887.44 | -4.1 | done | losing for real |
| coinflip | 5280 | 50.0 | 50.0 | $-2266.47 | -4.3% | $-1266.47 | -3.1 | done | losing for real |
| momentum_15m_0.10pct | 3664 | 49.1 | 50.2 | $-2274.76 | -6.2% | $-1274.76 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 5280 | 50.1 | 51.3 | $-3325.03 | -6.3% | $-2325.03 | -4.7 | done | losing for real |
| always_up | 5280 | 48.0 | 49.2 | $-3569.92 | -6.8% | $-2569.92 | -4.9 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 9355 | 48.1 | 48.7 | $-4928.53 |
| ETH | 10049 | 48.0 | 48.0 | $-5529.44 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
