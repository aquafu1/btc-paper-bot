# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 17, 3:35 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 654 windows, 18093 settled trades, 40 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 343 | 34.1 | 35.4 | $-267.49 | -7.8% | $732.51 | -1.1 | done | can't tell from luck |
| momentum_60m_0.30pct | 1529 | 50.6 | 49.6 | $-360.65 | -2.4% | $639.35 | -0.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 1854 | 51.6 | 51.0 | $-564.17 | -3.0% | $435.83 | -1.3 | done | can't tell from luck |
| trend_filter | 1047 | 50.3 | 50.9 | $-568.49 | -5.4% | $431.51 | -1.8 | done | can't tell from luck |
| value_ev10 | 838 | 38.2 | 39.5 | $-615.05 | -7.3% | $384.95 | -1.8 | done | can't tell from luck |
| value_ev5 | 1266 | 40.8 | 41.4 | $-690.41 | -5.5% | $309.59 | -1.7 | done | can't tell from luck |
| coinflip | 2611 | 50.0 | 50.5 | $-1241.14 | -4.8% | $-241.14 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 1529 | 49.4 | 51.4 | $-1270.50 | -8.3% | $-270.50 | -3.3 | done | losing for real |
| momentum_15m_0.10pct | 1854 | 48.4 | 50.0 | $-1276.97 | -6.9% | $-276.97 | -3.0 | done | losing for real |
| momentum_5m_0.00pct | 2611 | 50.7 | 51.8 | $-1438.09 | -5.5% | $-438.09 | -2.9 | done | losing for real |
| always_up | 2611 | 47.5 | 49.7 | $-2175.34 | -8.3% | $-1175.34 | -4.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4098 | 48.3 | 49.3 | $-2521.50 |
| ETH | 4516 | 48.2 | 48.7 | $-2756.86 |
| SOL | 4710 | 48.1 | 48.8 | $-2902.52 |
| XRP | 4769 | 48.5 | 48.6 | $-2287.40 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
