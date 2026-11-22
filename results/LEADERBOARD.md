# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 21, 11:45 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1071 windows, 29626 settled trades, 66 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 553 | 34.4 | 35.1 | $-343.30 | -6.2% | $656.70 | -1.1 | done | can't tell from luck |
| reversal_15m_0.10pct | 3002 | 51.3 | 50.5 | $-731.69 | -2.4% | $268.31 | -1.3 | done | can't tell from luck |
| value_ev10 | 1367 | 37.6 | 39.2 | $-980.20 | -7.2% | $19.80 | -2.2 | done | losing for real |
| momentum_60m_0.30pct | 2516 | 49.8 | 49.6 | $-1111.85 | -4.4% | $-111.85 | -2.2 | done | losing for real |
| trend_filter | 1764 | 49.6 | 50.7 | $-1245.65 | -7.1% | $-245.65 | -3.0 | done | losing for real |
| value_ev5 | 2078 | 39.7 | 41.0 | $-1369.80 | -6.6% | $-369.80 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 2516 | 50.2 | 51.0 | $-1626.19 | -6.5% | $-626.19 | -3.3 | done | losing for real |
| coinflip | 4276 | 50.5 | 50.3 | $-1684.19 | -3.9% | $-684.19 | -2.6 | done | losing for real |
| momentum_5m_0.00pct | 4276 | 51.0 | 51.5 | $-2056.90 | -4.8% | $-1056.90 | -3.2 | done | losing for real |
| momentum_15m_0.10pct | 3002 | 48.7 | 50.3 | $-2153.16 | -7.2% | $-1153.16 | -4.0 | done | losing for real |
| always_up | 4276 | 47.2 | 49.4 | $-3809.80 | -8.9% | $-2809.80 | -5.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6760 | 48.4 | 49.0 | $-3435.99 |
| ETH | 7328 | 48.1 | 48.5 | $-4626.82 |
| SOL | 7728 | 48.1 | 48.5 | $-4469.50 |
| XRP | 7810 | 48.2 | 48.3 | $-4580.42 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
