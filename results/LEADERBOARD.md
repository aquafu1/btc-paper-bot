# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 19, 5:20 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 805 windows, 22129 settled trades, 22 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 411 | 33.6 | 35.0 | $-321.28 | -7.8% | $678.72 | -1.2 | done | can't tell from luck |
| value_ev10 | 1011 | 38.0 | 39.2 | $-644.51 | -6.4% | $355.49 | -1.6 | done | can't tell from luck |
| momentum_60m_0.30pct | 1858 | 50.1 | 49.6 | $-713.43 | -3.8% | $286.57 | -1.7 | done | can't tell from luck |
| trend_filter | 1295 | 50.2 | 50.8 | $-772.92 | -6.0% | $227.08 | -2.2 | done | losing for real |
| reversal_15m_0.10pct | 2261 | 51.0 | 50.6 | $-801.42 | -3.5% | $198.58 | -1.7 | done | can't tell from luck |
| value_ev5 | 1529 | 40.2 | 41.1 | $-846.63 | -5.5% | $153.37 | -1.8 | done | can't tell from luck |
| reversal_60m_0.30pct | 1858 | 49.9 | 51.2 | $-1338.51 | -7.2% | $-338.51 | -3.2 | done | losing for real |
| coinflip | 3215 | 50.2 | 50.3 | $-1357.96 | -4.2% | $-357.96 | -2.4 | done | losing for real |
| momentum_5m_0.00pct | 3215 | 51.3 | 51.6 | $-1365.58 | -4.2% | $-365.58 | -2.5 | done | losing for real |
| momentum_15m_0.10pct | 2261 | 49.0 | 50.2 | $-1377.99 | -6.1% | $-377.99 | -2.9 | done | losing for real |
| always_up | 3215 | 47.4 | 49.7 | $-2776.92 | -8.6% | $-1776.92 | -4.9 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5022 | 48.3 | 49.1 | $-2805.14 |
| ETH | 5515 | 48.2 | 48.5 | $-3470.28 |
| SOL | 5764 | 48.3 | 48.6 | $-3164.93 |
| XRP | 5828 | 48.5 | 48.5 | $-2876.80 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
