# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 22, 6:35 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1098 windows, 30380 settled trades, 62 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 577 | 34.7 | 35.0 | $-321.49 | -5.6% | $678.51 | -1.0 | done | can't tell from luck |
| value_ev10 | 1412 | 38.2 | 39.1 | $-801.09 | -5.7% | $198.91 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 3066 | 51.0 | 50.5 | $-916.66 | -3.0% | $83.34 | -1.7 | done | can't tell from luck |
| momentum_60m_0.30pct | 2582 | 49.7 | 49.4 | $-1100.95 | -4.3% | $-100.95 | -2.2 | done | losing for real |
| value_ev5 | 2143 | 40.1 | 41.0 | $-1170.70 | -5.5% | $-170.70 | -2.1 | done | losing for real |
| trend_filter | 1800 | 49.3 | 50.5 | $-1327.14 | -7.4% | $-327.14 | -3.2 | done | losing for real |
| reversal_60m_0.30pct | 2582 | 50.3 | 51.1 | $-1650.49 | -6.4% | $-650.49 | -3.3 | done | losing for real |
| coinflip | 4384 | 50.5 | 50.2 | $-1661.36 | -3.8% | $-661.36 | -2.5 | done | losing for real |
| momentum_15m_0.10pct | 3066 | 49.0 | 50.2 | $-1968.77 | -6.4% | $-968.77 | -3.6 | done | losing for real |
| momentum_5m_0.00pct | 4384 | 50.8 | 51.4 | $-2271.03 | -5.2% | $-1271.03 | -3.5 | done | losing for real |
| always_up | 4384 | 47.5 | 49.3 | $-3469.01 | -7.9% | $-2469.01 | -5.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6951 | 48.5 | 49.0 | $-3362.75 |
| ETH | 7524 | 48.2 | 48.4 | $-4412.34 |
| SOL | 7911 | 48.1 | 48.4 | $-4337.04 |
| XRP | 7994 | 48.2 | 48.2 | $-4546.56 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
