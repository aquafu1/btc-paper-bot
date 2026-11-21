# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 21, 2:30 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1034 windows, 28738 settled trades, 42 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 533 | 34.7 | 35.1 | $-283.54 | -5.3% | $716.46 | -0.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 2924 | 51.2 | 50.5 | $-851.68 | -2.9% | $148.32 | -1.6 | done | can't tell from luck |
| value_ev10 | 1324 | 37.5 | 39.2 | $-995.09 | -7.5% | $4.91 | -2.2 | done | losing for real |
| momentum_60m_0.30pct | 2463 | 49.8 | 49.6 | $-1102.65 | -4.5% | $-102.65 | -2.2 | done | losing for real |
| trend_filter | 1719 | 49.3 | 50.7 | $-1321.06 | -7.7% | $-321.06 | -3.3 | done | losing for real |
| value_ev5 | 2004 | 39.4 | 41.0 | $-1424.40 | -7.1% | $-424.40 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 2463 | 50.2 | 51.0 | $-1625.50 | -6.6% | $-625.50 | -3.4 | done | losing for real |
| coinflip | 4128 | 50.5 | 50.3 | $-1670.72 | -4.0% | $-670.72 | -2.6 | done | losing for real |
| momentum_15m_0.10pct | 2924 | 48.8 | 50.2 | $-1992.96 | -6.8% | $-992.96 | -3.7 | done | losing for real |
| momentum_5m_0.00pct | 4128 | 50.7 | 51.5 | $-2258.40 | -5.5% | $-1258.40 | -3.6 | done | losing for real |
| always_up | 4128 | 47.4 | 49.5 | $-3610.08 | -8.7% | $-2610.08 | -5.6 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6556 | 48.2 | 49.1 | $-3659.51 |
| ETH | 7130 | 48.1 | 48.5 | $-4406.53 |
| SOL | 7500 | 48.2 | 48.6 | $-4319.74 |
| XRP | 7552 | 48.1 | 48.3 | $-4750.30 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
