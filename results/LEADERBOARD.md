# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 20, 8:20 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 961 windows, 26633 settled trades, 25 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 491 | 35.0 | 34.8 | $-169.50 | -3.5% | $830.50 | -0.6 | done | can't tell from luck |
| value_ev10 | 1211 | 38.2 | 39.1 | $-632.30 | -5.2% | $367.70 | -1.5 | done | can't tell from luck |
| reversal_15m_0.10pct | 2722 | 51.4 | 50.5 | $-684.35 | -2.5% | $315.65 | -1.3 | done | can't tell from luck |
| momentum_60m_0.30pct | 2270 | 50.1 | 49.7 | $-901.20 | -4.0% | $98.80 | -1.9 | done | can't tell from luck |
| value_ev5 | 1838 | 40.0 | 41.0 | $-983.13 | -5.3% | $16.87 | -1.9 | done | can't tell from luck |
| trend_filter | 1592 | 49.9 | 50.9 | $-1070.96 | -6.7% | $-70.96 | -2.8 | done | losing for real |
| reversal_60m_0.30pct | 2270 | 49.9 | 51.0 | $-1578.09 | -7.0% | $-578.09 | -3.4 | done | losing for real |
| coinflip | 3839 | 50.1 | 50.4 | $-1779.22 | -4.6% | $-779.22 | -2.9 | done | losing for real |
| momentum_15m_0.10pct | 2722 | 48.6 | 50.3 | $-1951.37 | -7.2% | $-951.37 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 3839 | 50.8 | 51.6 | $-2007.10 | -5.2% | $-1007.10 | -3.3 | done | losing for real |
| always_up | 3839 | 46.9 | 49.6 | $-3719.82 | -9.7% | $-2719.82 | -6.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6062 | 48.2 | 49.0 | $-3449.96 |
| ETH | 6618 | 48.1 | 48.5 | $-4035.89 |
| SOL | 6957 | 48.3 | 48.6 | $-3779.99 |
| XRP | 6996 | 48.2 | 48.5 | $-4211.20 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
