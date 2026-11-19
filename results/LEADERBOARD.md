# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 19, 12:15 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 785 windows, 21634 settled trades, 46 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 404 | 32.9 | 34.9 | $-391.45 | -9.7% | $608.55 | -1.5 | done | can't tell from luck |
| momentum_60m_0.30pct | 1832 | 50.1 | 49.6 | $-695.86 | -3.8% | $304.14 | -1.6 | done | can't tell from luck |
| trend_filter | 1271 | 50.3 | 50.8 | $-737.72 | -5.8% | $262.28 | -2.1 | done | losing for real |
| reversal_15m_0.10pct | 2210 | 51.0 | 50.6 | $-743.18 | -3.4% | $256.82 | -1.6 | done | can't tell from luck |
| value_ev10 | 986 | 37.3 | 39.1 | $-792.30 | -8.0% | $207.70 | -2.1 | done | losing for real |
| value_ev5 | 1493 | 39.7 | 41.1 | $-1020.62 | -6.8% | $-20.62 | -2.2 | done | losing for real |
| reversal_60m_0.30pct | 1832 | 49.9 | 51.2 | $-1321.10 | -7.2% | $-321.10 | -3.2 | done | losing for real |
| coinflip | 3132 | 50.3 | 50.3 | $-1329.62 | -4.2% | $-329.62 | -2.4 | done | losing for real |
| momentum_15m_0.10pct | 2210 | 49.0 | 50.2 | $-1423.42 | -6.4% | $-423.42 | -3.0 | done | losing for real |
| momentum_5m_0.00pct | 3132 | 51.2 | 51.7 | $-1455.75 | -4.6% | $-455.75 | -2.7 | done | losing for real |
| always_up | 3132 | 47.4 | 49.5 | $-2711.27 | -8.7% | $-1711.27 | -4.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4915 | 48.3 | 49.1 | $-2900.00 |
| ETH | 5398 | 48.0 | 48.5 | $-3624.14 |
| SOL | 5633 | 48.2 | 48.6 | $-3214.22 |
| XRP | 5688 | 48.5 | 48.5 | $-2883.92 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
