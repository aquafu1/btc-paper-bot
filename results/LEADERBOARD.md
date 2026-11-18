# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 17, 7:15 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 669 windows, 18493 settled trades, 59 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 345 | 34.5 | 35.3 | $-215.88 | -6.3% | $784.12 | -0.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 1573 | 50.4 | 49.6 | $-424.35 | -2.7% | $575.65 | -1.1 | done | can't tell from luck |
| reversal_15m_0.10pct | 1895 | 51.5 | 50.9 | $-539.89 | -2.8% | $460.11 | -1.2 | done | can't tell from luck |
| value_ev10 | 849 | 38.4 | 39.4 | $-541.27 | -6.4% | $458.73 | -1.5 | done | can't tell from luck |
| trend_filter | 1077 | 50.3 | 50.9 | $-568.01 | -5.3% | $431.99 | -1.8 | done | can't tell from luck |
| value_ev5 | 1282 | 40.7 | 41.3 | $-666.63 | -5.2% | $333.37 | -1.6 | done | can't tell from luck |
| coinflip | 2668 | 50.1 | 50.4 | $-1178.55 | -4.4% | $-178.55 | -2.3 | done | losing for real |
| reversal_60m_0.30pct | 1573 | 49.6 | 51.3 | $-1225.54 | -7.8% | $-225.54 | -3.2 | done | losing for real |
| momentum_15m_0.10pct | 1895 | 48.5 | 50.1 | $-1298.83 | -6.9% | $-298.83 | -3.0 | done | losing for real |
| momentum_5m_0.00pct | 2668 | 50.8 | 51.8 | $-1425.88 | -5.3% | $-425.88 | -2.9 | done | losing for real |
| always_up | 2668 | 47.5 | 49.7 | $-2263.05 | -8.5% | $-1263.05 | -4.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4206 | 48.3 | 49.2 | $-2455.50 |
| ETH | 4612 | 48.2 | 48.6 | $-2774.13 |
| SOL | 4813 | 48.2 | 48.8 | $-2818.25 |
| XRP | 4862 | 48.6 | 48.6 | $-2300.00 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
