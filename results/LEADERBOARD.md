# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 20, 8:30 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 914 windows, 25228 settled trades, 59 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 472 | 35.0 | 34.8 | $-181.30 | -3.8% | $818.70 | -0.6 | done | can't tell from luck |
| value_ev10 | 1156 | 38.1 | 39.1 | $-668.14 | -5.8% | $331.86 | -1.6 | done | can't tell from luck |
| momentum_60m_0.30pct | 2137 | 50.0 | 49.8 | $-940.55 | -4.4% | $59.45 | -2.0 | done | losing for real |
| trend_filter | 1498 | 50.0 | 51.0 | $-1007.11 | -6.7% | $-7.11 | -2.7 | done | losing for real |
| reversal_15m_0.10pct | 2568 | 50.5 | 50.5 | $-1088.38 | -4.2% | $-88.38 | -2.2 | done | losing for real |
| value_ev5 | 1748 | 39.7 | 41.0 | $-1102.52 | -6.3% | $-102.52 | -2.2 | done | losing for real |
| momentum_15m_0.10pct | 2568 | 49.5 | 50.3 | $-1370.53 | -5.3% | $-370.53 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 2137 | 50.0 | 50.8 | $-1424.99 | -6.7% | $-424.99 | -3.1 | done | losing for real |
| coinflip | 3648 | 50.3 | 50.3 | $-1559.37 | -4.3% | $-559.37 | -2.6 | done | losing for real |
| momentum_5m_0.00pct | 3648 | 51.1 | 51.6 | $-1717.27 | -4.7% | $-717.27 | -2.9 | done | losing for real |
| always_up | 3648 | 46.8 | 49.7 | $-3655.00 | -10.0% | $-2655.00 | -6.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5745 | 48.2 | 49.1 | $-3247.78 |
| ETH | 6273 | 48.2 | 48.5 | $-3901.89 |
| SOL | 6583 | 48.1 | 48.6 | $-3846.02 |
| XRP | 6627 | 48.3 | 48.5 | $-3719.45 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
