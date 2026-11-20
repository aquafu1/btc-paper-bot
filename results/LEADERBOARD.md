# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 19, 6:35 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 858 windows, 23670 settled trades, 34 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 444 | 34.5 | 34.8 | $-237.85 | -5.4% | $762.15 | -0.8 | done | can't tell from luck |
| value_ev10 | 1082 | 37.8 | 39.0 | $-716.18 | -6.6% | $283.82 | -1.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 2003 | 50.2 | 49.7 | $-787.52 | -3.9% | $212.48 | -1.8 | done | can't tell from luck |
| trend_filter | 1393 | 50.1 | 50.9 | $-903.02 | -6.5% | $96.98 | -2.5 | done | losing for real |
| reversal_15m_0.10pct | 2416 | 50.7 | 50.5 | $-930.62 | -3.9% | $69.38 | -1.9 | done | can't tell from luck |
| value_ev5 | 1635 | 39.8 | 41.0 | $-1035.18 | -6.3% | $-35.18 | -2.2 | done | losing for real |
| momentum_15m_0.10pct | 2416 | 49.3 | 50.3 | $-1432.08 | -5.9% | $-432.08 | -2.9 | done | losing for real |
| reversal_60m_0.30pct | 2003 | 49.8 | 51.0 | $-1479.22 | -7.4% | $-479.22 | -3.4 | done | losing for real |
| coinflip | 3426 | 50.2 | 50.3 | $-1492.94 | -4.4% | $-492.94 | -2.6 | done | losing for real |
| momentum_5m_0.00pct | 3426 | 51.2 | 51.7 | $-1625.41 | -4.7% | $-625.41 | -2.9 | done | losing for real |
| always_up | 3426 | 47.0 | 49.5 | $-3257.90 | -9.5% | $-2257.90 | -5.6 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5401 | 48.3 | 49.0 | $-2974.16 |
| ETH | 5894 | 48.1 | 48.5 | $-3873.03 |
| SOL | 6174 | 48.3 | 48.5 | $-3544.23 |
| XRP | 6201 | 48.3 | 48.5 | $-3506.51 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
