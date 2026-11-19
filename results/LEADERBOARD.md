# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 19, 5:50 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 807 windows, 22151 settled trades, 56 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 411 | 33.6 | 35.0 | $-321.28 | -7.8% | $678.72 | -1.2 | done | can't tell from luck |
| value_ev10 | 1013 | 37.9 | 39.2 | $-664.51 | -6.6% | $335.49 | -1.7 | done | can't tell from luck |
| momentum_60m_0.30pct | 1858 | 50.1 | 49.6 | $-713.43 | -3.8% | $286.57 | -1.7 | done | can't tell from luck |
| trend_filter | 1295 | 50.2 | 50.8 | $-772.92 | -6.0% | $227.08 | -2.2 | done | losing for real |
| reversal_15m_0.10pct | 2262 | 50.9 | 50.6 | $-811.42 | -3.6% | $188.58 | -1.7 | done | can't tell from luck |
| value_ev5 | 1532 | 40.1 | 41.1 | $-876.63 | -5.7% | $123.37 | -1.9 | done | can't tell from luck |
| reversal_60m_0.30pct | 1858 | 49.9 | 51.2 | $-1338.51 | -7.2% | $-338.51 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 3220 | 51.3 | 51.6 | $-1342.86 | -4.2% | $-342.86 | -2.4 | done | losing for real |
| momentum_15m_0.10pct | 2262 | 49.1 | 50.2 | $-1366.16 | -6.0% | $-366.16 | -2.9 | done | losing for real |
| coinflip | 3220 | 50.2 | 50.3 | $-1369.58 | -4.3% | $-369.58 | -2.4 | done | losing for real |
| always_up | 3220 | 47.5 | 49.7 | $-2758.73 | -8.6% | $-1758.73 | -4.9 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5032 | 48.4 | 49.1 | $-2806.17 |
| ETH | 5518 | 48.2 | 48.5 | $-3465.06 |
| SOL | 5769 | 48.3 | 48.6 | $-3165.30 |
| XRP | 5832 | 48.5 | 48.5 | $-2899.49 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
