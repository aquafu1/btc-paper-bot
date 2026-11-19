# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 19, 5:30 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 806 windows, 22134 settled trades, 46 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 411 | 33.6 | 35.0 | $-321.28 | -7.8% | $678.72 | -1.2 | done | can't tell from luck |
| value_ev10 | 1011 | 38.0 | 39.2 | $-644.51 | -6.4% | $355.49 | -1.6 | done | can't tell from luck |
| momentum_60m_0.30pct | 1858 | 50.1 | 49.6 | $-713.43 | -3.8% | $286.57 | -1.7 | done | can't tell from luck |
| trend_filter | 1295 | 50.2 | 50.8 | $-772.92 | -6.0% | $227.08 | -2.2 | done | losing for real |
| reversal_15m_0.10pct | 2262 | 50.9 | 50.6 | $-811.42 | -3.6% | $188.58 | -1.7 | done | can't tell from luck |
| value_ev5 | 1529 | 40.2 | 41.1 | $-846.63 | -5.5% | $153.37 | -1.8 | done | can't tell from luck |
| reversal_60m_0.30pct | 1858 | 49.9 | 51.2 | $-1338.51 | -7.2% | $-338.51 | -3.2 | done | losing for real |
| coinflip | 3216 | 50.2 | 50.3 | $-1346.12 | -4.2% | $-346.12 | -2.4 | done | losing for real |
| momentum_5m_0.00pct | 3216 | 51.3 | 51.6 | $-1353.75 | -4.2% | $-353.75 | -2.5 | done | losing for real |
| momentum_15m_0.10pct | 2262 | 49.1 | 50.2 | $-1366.16 | -6.0% | $-366.16 | -2.9 | done | losing for real |
| always_up | 3216 | 47.4 | 49.7 | $-2786.92 | -8.7% | $-1786.92 | -4.9 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5027 | 48.4 | 49.1 | $-2789.64 |
| ETH | 5515 | 48.2 | 48.5 | $-3470.28 |
| SOL | 5764 | 48.3 | 48.6 | $-3164.93 |
| XRP | 5828 | 48.5 | 48.5 | $-2876.80 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
