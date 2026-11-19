# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 18, 6:45 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 763 windows, 21047 settled trades, 41 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 395 | 33.7 | 34.9 | $-301.45 | -7.6% | $698.55 | -1.1 | done | can't tell from luck |
| reversal_15m_0.10pct | 2152 | 51.5 | 50.6 | $-521.13 | -2.4% | $478.87 | -1.1 | done | can't tell from luck |
| value_ev10 | 962 | 37.9 | 39.1 | $-627.51 | -6.5% | $372.49 | -1.6 | done | can't tell from luck |
| momentum_60m_0.30pct | 1781 | 49.9 | 49.6 | $-705.73 | -4.0% | $294.27 | -1.7 | done | can't tell from luck |
| trend_filter | 1239 | 49.9 | 50.9 | $-802.70 | -6.5% | $197.30 | -2.3 | done | losing for real |
| value_ev5 | 1453 | 40.1 | 41.1 | $-866.57 | -6.0% | $133.43 | -1.9 | done | can't tell from luck |
| coinflip | 3044 | 50.4 | 50.3 | $-1168.36 | -3.8% | $-168.36 | -2.1 | done | losing for real |
| reversal_60m_0.30pct | 1781 | 50.1 | 51.2 | $-1225.67 | -6.9% | $-225.67 | -3.0 | done | losing for real |
| momentum_15m_0.10pct | 2152 | 48.5 | 50.2 | $-1582.81 | -7.4% | $-582.81 | -3.4 | done | losing for real |
| momentum_5m_0.00pct | 3044 | 50.9 | 51.8 | $-1625.38 | -5.3% | $-625.38 | -3.0 | done | losing for real |
| always_up | 3044 | 47.0 | 49.6 | $-2874.45 | -9.4% | $-1874.45 | -5.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4775 | 48.2 | 49.1 | $-2931.57 |
| ETH | 5248 | 48.0 | 48.6 | $-3491.32 |
| SOL | 5479 | 48.0 | 48.6 | $-3323.53 |
| XRP | 5545 | 48.6 | 48.5 | $-2555.33 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
