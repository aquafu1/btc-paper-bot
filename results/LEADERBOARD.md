# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 16, 4:20 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 561 windows, 15570 settled trades, 33 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1323 | 51.4 | 49.7 | $-216.30 | -1.6% | $783.70 | -0.6 | done | can't tell from luck |
| value_ev20 | 306 | 33.0 | 35.2 | $-355.92 | -11.6% | $644.08 | -1.6 | done | can't tell from luck |
| trend_filter | 902 | 50.7 | 51.1 | $-482.43 | -5.3% | $517.57 | -1.7 | done | can't tell from luck |
| value_ev10 | 740 | 37.6 | 39.4 | $-696.41 | -9.4% | $303.59 | -2.1 | done | losing for real |
| momentum_15m_0.10pct | 1578 | 49.6 | 49.8 | $-779.74 | -4.9% | $220.26 | -2.0 | done | can't tell from luck |
| value_ev5 | 1100 | 39.7 | 41.2 | $-881.53 | -8.0% | $118.47 | -2.3 | done | losing for real |
| reversal_15m_0.10pct | 1578 | 50.4 | 51.1 | $-982.94 | -6.2% | $17.06 | -2.5 | done | losing for real |
| coinflip | 2240 | 49.9 | 50.5 | $-1263.49 | -5.6% | $-263.49 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 1323 | 48.6 | 51.2 | $-1333.75 | -10.1% | $-333.75 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 2240 | 50.4 | 51.9 | $-1538.48 | -6.9% | $-538.48 | -3.4 | done | losing for real |
| always_up | 2240 | 47.3 | 49.9 | $-2195.56 | -9.8% | $-1195.56 | -4.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3521 | 47.6 | 49.2 | $-2729.82 |
| ETH | 3880 | 48.0 | 48.6 | $-2741.66 |
| SOL | 4066 | 47.9 | 48.7 | $-3000.02 |
| XRP | 4103 | 48.6 | 48.6 | $-2255.05 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
