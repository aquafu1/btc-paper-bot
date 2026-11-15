# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 14, 6:00 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 376 windows, 10214 settled trades, 61 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 195 | 37.4 | 36.5 | $-16.95 | -0.9% | $983.05 | -0.1 | Sat 8:30 PM | too few trades (195/200) |
| value_ev10 | 497 | 40.2 | 40.4 | $-179.12 | -3.6% | $820.88 | -0.7 | done | can't tell from luck |
| value_ev5 | 734 | 41.8 | 42.1 | $-302.45 | -4.1% | $697.55 | -1.0 | done | can't tell from luck |
| momentum_60m_0.30pct | 850 | 49.8 | 49.7 | $-372.24 | -4.4% | $627.76 | -1.3 | done | can't tell from luck |
| trend_filter | 566 | 48.8 | 50.4 | $-442.55 | -7.8% | $557.45 | -1.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 1017 | 51.7 | 52.2 | $-498.15 | -4.9% | $501.85 | -1.6 | done | can't tell from luck |
| reversal_60m_0.30pct | 850 | 50.2 | 52.0 | $-629.42 | -7.4% | $370.58 | -2.3 | done | losing for real |
| momentum_15m_0.10pct | 1017 | 48.3 | 49.6 | $-632.12 | -6.2% | $367.88 | -2.0 | done | can't tell from luck |
| coinflip | 1496 | 49.8 | 50.8 | $-844.77 | -5.6% | $155.23 | -2.2 | done | losing for real |
| momentum_5m_0.00pct | 1496 | 49.5 | 51.5 | $-1117.06 | -7.5% | $-117.06 | -3.0 | done | losing for real |
| always_up | 1496 | 45.7 | 50.8 | $-2015.77 | -13.5% | $-1015.77 | -5.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2300 | 47.4 | 49.4 | $-1795.62 |
| ETH | 2568 | 47.6 | 48.8 | $-1825.15 |
| SOL | 2646 | 47.8 | 49.4 | $-2002.86 |
| XRP | 2700 | 48.6 | 49.1 | $-1426.99 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
