# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 17, 4:20 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 657 windows, 18174 settled trades, 33 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 343 | 34.1 | 35.4 | $-267.49 | -7.8% | $732.51 | -1.1 | done | can't tell from luck |
| momentum_60m_0.30pct | 1539 | 50.6 | 49.7 | $-390.98 | -2.5% | $609.02 | -1.0 | done | can't tell from luck |
| reversal_15m_0.10pct | 1863 | 51.6 | 50.9 | $-513.00 | -2.8% | $487.00 | -1.2 | done | can't tell from luck |
| trend_filter | 1054 | 50.4 | 51.0 | $-568.82 | -5.4% | $431.18 | -1.8 | done | can't tell from luck |
| value_ev10 | 838 | 38.2 | 39.5 | $-615.05 | -7.3% | $384.95 | -1.8 | done | can't tell from luck |
| value_ev5 | 1266 | 40.8 | 41.4 | $-690.41 | -5.5% | $309.59 | -1.7 | done | can't tell from luck |
| coinflip | 2623 | 50.1 | 50.5 | $-1165.33 | -4.4% | $-165.33 | -2.3 | done | losing for real |
| reversal_60m_0.30pct | 1539 | 49.4 | 51.3 | $-1210.45 | -7.9% | $-210.45 | -3.2 | done | losing for real |
| momentum_15m_0.10pct | 1863 | 48.4 | 50.0 | $-1298.17 | -7.0% | $-298.17 | -3.0 | done | losing for real |
| momentum_5m_0.00pct | 2623 | 50.8 | 51.8 | $-1413.71 | -5.4% | $-413.71 | -2.9 | done | losing for real |
| always_up | 2623 | 47.5 | 49.7 | $-2205.99 | -8.4% | $-1205.99 | -4.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4125 | 48.3 | 49.3 | $-2452.89 |
| ETH | 4534 | 48.3 | 48.7 | $-2766.74 |
| SOL | 4733 | 48.1 | 48.8 | $-2834.09 |
| XRP | 4782 | 48.5 | 48.6 | $-2285.68 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
