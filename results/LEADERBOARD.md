# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 21, 5:50 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1047 windows, 29049 settled trades, 43 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 543 | 34.4 | 35.1 | $-325.47 | -6.0% | $674.53 | -1.1 | done | can't tell from luck |
| reversal_15m_0.10pct | 2947 | 51.2 | 50.5 | $-789.21 | -2.7% | $210.79 | -1.5 | done | can't tell from luck |
| value_ev10 | 1344 | 37.4 | 39.2 | $-1046.04 | -7.8% | $-46.04 | -2.3 | done | losing for real |
| momentum_60m_0.30pct | 2479 | 49.7 | 49.6 | $-1176.03 | -4.7% | $-176.03 | -2.4 | done | losing for real |
| trend_filter | 1736 | 49.3 | 50.7 | $-1366.32 | -7.9% | $-366.32 | -3.4 | done | losing for real |
| value_ev5 | 2034 | 39.3 | 41.0 | $-1481.77 | -7.3% | $-481.77 | -2.8 | done | losing for real |
| reversal_60m_0.30pct | 2479 | 50.3 | 51.0 | $-1565.77 | -6.3% | $-565.77 | -3.2 | done | losing for real |
| coinflip | 4180 | 50.5 | 50.3 | $-1671.81 | -4.0% | $-671.81 | -2.6 | done | losing for real |
| momentum_15m_0.10pct | 2947 | 48.8 | 50.3 | $-2064.57 | -7.0% | $-1064.57 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 4180 | 50.7 | 51.5 | $-2297.52 | -5.5% | $-1297.52 | -3.7 | done | losing for real |
| always_up | 4180 | 47.3 | 49.4 | $-3660.54 | -8.8% | $-2660.54 | -5.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6623 | 48.3 | 49.0 | $-3573.26 |
| ETH | 7197 | 48.1 | 48.5 | $-4562.37 |
| SOL | 7584 | 48.0 | 48.5 | $-4544.09 |
| XRP | 7645 | 48.1 | 48.3 | $-4765.32 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
