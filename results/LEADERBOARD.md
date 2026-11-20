# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 20, 2:45 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 891 windows, 24581 settled trades, 58 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 461 | 35.6 | 34.9 | $-99.37 | -2.2% | $900.63 | -0.3 | done | can't tell from luck |
| value_ev10 | 1127 | 38.2 | 39.1 | $-607.59 | -5.4% | $392.41 | -1.5 | done | can't tell from luck |
| momentum_60m_0.30pct | 2075 | 49.9 | 49.8 | $-928.30 | -4.5% | $71.70 | -2.0 | done | losing for real |
| trend_filter | 1447 | 50.0 | 51.0 | $-991.24 | -6.9% | $8.76 | -2.7 | done | losing for real |
| reversal_15m_0.10pct | 2511 | 50.5 | 50.4 | $-995.11 | -4.0% | $4.89 | -2.0 | done | can't tell from luck |
| value_ev5 | 1706 | 39.9 | 41.0 | $-1002.12 | -5.9% | $-2.12 | -2.0 | done | losing for real |
| reversal_60m_0.30pct | 2075 | 50.1 | 50.9 | $-1359.78 | -6.6% | $-359.78 | -3.0 | done | losing for real |
| momentum_15m_0.10pct | 2511 | 49.5 | 50.4 | $-1397.39 | -5.6% | $-397.39 | -2.8 | done | losing for real |
| coinflip | 3556 | 50.3 | 50.3 | $-1493.39 | -4.2% | $-493.39 | -2.5 | done | losing for real |
| momentum_5m_0.00pct | 3556 | 51.2 | 51.7 | $-1652.37 | -4.6% | $-652.37 | -2.9 | done | losing for real |
| always_up | 3556 | 47.0 | 49.6 | $-3412.32 | -9.6% | $-2412.32 | -5.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5603 | 48.3 | 49.1 | $-2969.65 |
| ETH | 6119 | 48.2 | 48.5 | $-3713.93 |
| SOL | 6418 | 48.2 | 48.5 | $-3650.02 |
| XRP | 6441 | 48.3 | 48.5 | $-3605.38 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
