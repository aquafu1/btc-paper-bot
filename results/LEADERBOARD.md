# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 22, 7:50 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1103 windows, 30520 settled trades, 54 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 579 | 34.5 | 35.0 | $-341.49 | -5.9% | $658.51 | -1.1 | done | can't tell from luck |
| reversal_15m_0.10pct | 3080 | 51.1 | 50.4 | $-830.23 | -2.7% | $169.77 | -1.5 | done | can't tell from luck |
| value_ev10 | 1419 | 38.1 | 39.1 | $-871.09 | -6.1% | $128.91 | -1.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 2597 | 49.7 | 49.4 | $-1071.85 | -4.1% | $-71.85 | -2.1 | done | losing for real |
| value_ev5 | 2152 | 40.0 | 41.0 | $-1237.31 | -5.7% | $-237.31 | -2.3 | done | losing for real |
| trend_filter | 1804 | 49.3 | 50.4 | $-1323.65 | -7.3% | $-323.65 | -3.2 | done | losing for real |
| coinflip | 4404 | 50.5 | 50.2 | $-1653.01 | -3.8% | $-653.01 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 2597 | 50.3 | 51.1 | $-1700.29 | -6.5% | $-700.29 | -3.4 | done | losing for real |
| momentum_15m_0.10pct | 3080 | 48.9 | 50.2 | $-2059.17 | -6.7% | $-1059.17 | -3.7 | done | losing for real |
| momentum_5m_0.00pct | 4404 | 50.7 | 51.4 | $-2291.58 | -5.2% | $-1291.58 | -3.6 | done | losing for real |
| always_up | 4404 | 47.5 | 49.3 | $-3579.59 | -8.1% | $-2579.59 | -5.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6989 | 48.4 | 49.0 | $-3429.17 |
| ETH | 7556 | 48.2 | 48.4 | $-4452.87 |
| SOL | 7944 | 48.1 | 48.4 | $-4410.00 |
| XRP | 8031 | 48.2 | 48.2 | $-4667.22 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
