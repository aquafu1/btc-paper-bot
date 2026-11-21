# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 21, 3:35 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1038 windows, 28833 settled trades, 46 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 536 | 34.7 | 35.1 | $-284.76 | -5.3% | $715.24 | -0.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 2930 | 51.2 | 50.5 | $-801.53 | -2.7% | $198.47 | -1.5 | done | can't tell from luck |
| value_ev10 | 1330 | 37.4 | 39.2 | $-1002.06 | -7.5% | $-2.06 | -2.2 | done | losing for real |
| momentum_60m_0.30pct | 2467 | 49.7 | 49.6 | $-1126.35 | -4.6% | $-126.35 | -2.3 | done | losing for real |
| trend_filter | 1725 | 49.3 | 50.7 | $-1349.42 | -7.8% | $-349.42 | -3.3 | done | losing for real |
| value_ev5 | 2013 | 39.4 | 41.0 | $-1413.93 | -7.0% | $-413.93 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 2467 | 50.3 | 51.0 | $-1602.08 | -6.5% | $-602.08 | -3.3 | done | losing for real |
| coinflip | 4145 | 50.5 | 50.3 | $-1651.36 | -4.0% | $-651.36 | -2.6 | done | losing for real |
| momentum_15m_0.10pct | 2930 | 48.8 | 50.3 | $-2037.63 | -7.0% | $-1037.63 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 4145 | 50.7 | 51.5 | $-2298.08 | -5.5% | $-1298.08 | -3.7 | done | losing for real |
| always_up | 4145 | 47.4 | 49.5 | $-3578.12 | -8.6% | $-2578.12 | -5.6 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6577 | 48.3 | 49.0 | $-3636.32 |
| ETH | 7146 | 48.1 | 48.5 | $-4432.08 |
| SOL | 7529 | 48.1 | 48.6 | $-4379.90 |
| XRP | 7581 | 48.1 | 48.3 | $-4697.02 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
