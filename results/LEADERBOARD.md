# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 20, 3:05 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 940 windows, 26037 settled trades, 30 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 478 | 34.9 | 34.9 | $-175.74 | -3.7% | $824.26 | -0.6 | done | can't tell from luck |
| value_ev10 | 1178 | 38.0 | 39.1 | $-686.59 | -5.8% | $313.41 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 2661 | 51.1 | 50.6 | $-865.84 | -3.3% | $134.16 | -1.7 | done | can't tell from luck |
| momentum_60m_0.30pct | 2226 | 50.1 | 49.9 | $-944.38 | -4.2% | $55.62 | -2.0 | done | losing for real |
| trend_filter | 1550 | 49.9 | 51.0 | $-1090.13 | -7.0% | $-90.13 | -2.9 | done | losing for real |
| value_ev5 | 1789 | 39.7 | 41.0 | $-1137.14 | -6.4% | $-137.14 | -2.3 | done | losing for real |
| reversal_60m_0.30pct | 2226 | 49.9 | 50.9 | $-1563.83 | -7.0% | $-563.83 | -3.4 | done | losing for real |
| coinflip | 3756 | 50.4 | 50.4 | $-1597.11 | -4.3% | $-597.11 | -2.6 | done | losing for real |
| momentum_15m_0.10pct | 2661 | 48.9 | 50.3 | $-1763.03 | -6.6% | $-763.03 | -3.4 | done | losing for real |
| momentum_5m_0.00pct | 3756 | 50.9 | 51.6 | $-1950.21 | -5.2% | $-950.21 | -3.3 | done | losing for real |
| always_up | 3756 | 46.7 | 49.7 | $-3885.36 | -10.3% | $-2885.36 | -6.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5938 | 48.1 | 49.1 | $-3530.24 |
| ETH | 6474 | 48.2 | 48.6 | $-4083.19 |
| SOL | 6791 | 48.1 | 48.6 | $-4038.69 |
| XRP | 6834 | 48.3 | 48.5 | $-4007.23 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
