# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 19, 12:00 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 784 windows, 21618 settled trades, 35 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 404 | 32.9 | 34.9 | $-391.45 | -9.7% | $608.55 | -1.5 | done | can't tell from luck |
| momentum_60m_0.30pct | 1832 | 50.1 | 49.6 | $-695.86 | -3.8% | $304.14 | -1.6 | done | can't tell from luck |
| trend_filter | 1271 | 50.3 | 50.8 | $-737.72 | -5.8% | $262.28 | -2.1 | done | losing for real |
| reversal_15m_0.10pct | 2209 | 51.0 | 50.6 | $-749.38 | -3.4% | $250.62 | -1.6 | done | can't tell from luck |
| value_ev10 | 985 | 37.4 | 39.1 | $-782.30 | -7.9% | $217.70 | -2.0 | done | losing for real |
| value_ev5 | 1492 | 39.7 | 41.1 | $-1010.62 | -6.8% | $-10.62 | -2.2 | done | losing for real |
| reversal_60m_0.30pct | 1832 | 49.9 | 51.2 | $-1321.10 | -7.2% | $-321.10 | -3.2 | done | losing for real |
| coinflip | 3128 | 50.2 | 50.3 | $-1336.88 | -4.3% | $-336.88 | -2.4 | done | losing for real |
| momentum_15m_0.10pct | 2209 | 49.0 | 50.2 | $-1413.42 | -6.4% | $-413.42 | -3.0 | done | losing for real |
| momentum_5m_0.00pct | 3128 | 51.2 | 51.7 | $-1464.06 | -4.7% | $-464.06 | -2.7 | done | losing for real |
| always_up | 3128 | 47.3 | 49.5 | $-2735.27 | -8.7% | $-1735.27 | -4.9 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4910 | 48.2 | 49.1 | $-2914.80 |
| ETH | 5395 | 48.0 | 48.5 | $-3627.61 |
| SOL | 5628 | 48.2 | 48.6 | $-3210.35 |
| XRP | 5685 | 48.5 | 48.5 | $-2885.29 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
