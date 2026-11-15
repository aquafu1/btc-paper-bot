# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 14, 6:05 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 376 windows, 10230 settled trades, 45 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 195 | 37.4 | 36.5 | $-16.95 | -0.9% | $983.05 | -0.1 | Sat 8:45 PM | too few trades (195/200) |
| value_ev10 | 499 | 40.1 | 40.4 | $-199.12 | -4.0% | $800.88 | -0.7 | done | can't tell from luck |
| value_ev5 | 736 | 41.7 | 42.1 | $-322.45 | -4.4% | $677.55 | -1.0 | done | can't tell from luck |
| momentum_60m_0.30pct | 851 | 49.7 | 49.7 | $-382.24 | -4.5% | $617.76 | -1.3 | done | can't tell from luck |
| trend_filter | 566 | 48.8 | 50.4 | $-442.55 | -7.8% | $557.45 | -1.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 1019 | 51.6 | 52.2 | $-518.15 | -5.1% | $481.85 | -1.7 | done | can't tell from luck |
| momentum_15m_0.10pct | 1019 | 48.4 | 49.6 | $-619.14 | -6.1% | $380.86 | -1.9 | done | can't tell from luck |
| reversal_60m_0.30pct | 851 | 50.3 | 52.0 | $-623.17 | -7.3% | $376.83 | -2.2 | done | losing for real |
| coinflip | 1498 | 49.8 | 50.8 | $-848.04 | -5.7% | $151.96 | -2.2 | done | losing for real |
| momentum_5m_0.00pct | 1498 | 49.5 | 51.5 | $-1104.08 | -7.4% | $-104.08 | -3.0 | done | losing for real |
| always_up | 1498 | 45.8 | 50.8 | $-2002.79 | -13.4% | $-1002.79 | -5.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2300 | 47.4 | 49.4 | $-1795.62 |
| ETH | 2577 | 47.6 | 48.8 | $-1850.15 |
| SOL | 2646 | 47.8 | 49.4 | $-2002.86 |
| XRP | 2707 | 48.7 | 49.1 | $-1430.05 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
