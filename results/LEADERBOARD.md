# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 21, 6:00 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1000 windows, 27788 settled trades, 57 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 514 | 34.2 | 34.9 | $-296.26 | -5.8% | $703.74 | -1.0 | done | can't tell from luck |
| reversal_15m_0.10pct | 2832 | 51.1 | 50.4 | $-841.44 | -3.0% | $158.56 | -1.6 | done | can't tell from luck |
| value_ev10 | 1274 | 37.5 | 39.1 | $-899.88 | -7.1% | $100.12 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 2384 | 49.8 | 49.7 | $-1098.76 | -4.6% | $-98.76 | -2.3 | done | losing for real |
| trend_filter | 1663 | 49.5 | 50.8 | $-1244.14 | -7.5% | $-244.14 | -3.1 | done | losing for real |
| value_ev5 | 1929 | 39.6 | 41.0 | $-1270.43 | -6.6% | $-270.43 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 2384 | 50.2 | 50.9 | $-1553.97 | -6.5% | $-553.97 | -3.3 | done | losing for real |
| coinflip | 3992 | 50.3 | 50.3 | $-1765.95 | -4.4% | $-765.95 | -2.8 | done | losing for real |
| momentum_15m_0.10pct | 2832 | 48.9 | 50.3 | $-1946.05 | -6.9% | $-946.05 | -3.7 | done | losing for real |
| momentum_5m_0.00pct | 3992 | 50.7 | 51.5 | $-2220.58 | -5.6% | $-1220.58 | -3.6 | done | losing for real |
| always_up | 3992 | 47.0 | 49.5 | $-3850.65 | -9.6% | $-2850.65 | -6.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6332 | 48.2 | 49.0 | $-3615.71 |
| ETH | 6903 | 48.0 | 48.5 | $-4562.91 |
| SOL | 7265 | 48.2 | 48.5 | $-4154.40 |
| XRP | 7288 | 48.1 | 48.4 | $-4655.09 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
