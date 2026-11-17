# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 17, 7:45 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 623 windows, 17213 settled trades, 57 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1457 | 51.5 | 49.6 | $-87.87 | -0.6% | $912.13 | -0.2 | done | can't tell from luck |
| value_ev20 | 329 | 34.0 | 35.3 | $-264.70 | -8.0% | $735.30 | -1.1 | done | can't tell from luck |
| trend_filter | 996 | 50.5 | 50.9 | $-491.18 | -4.9% | $508.82 | -1.6 | done | can't tell from luck |
| value_ev10 | 797 | 38.3 | 39.5 | $-574.18 | -7.2% | $425.82 | -1.7 | done | can't tell from luck |
| value_ev5 | 1203 | 40.5 | 41.4 | $-732.82 | -6.1% | $267.18 | -1.8 | done | can't tell from luck |
| momentum_15m_0.10pct | 1761 | 49.4 | 50.0 | $-884.04 | -5.0% | $115.96 | -2.1 | done | losing for real |
| reversal_15m_0.10pct | 1761 | 50.6 | 51.0 | $-886.28 | -5.0% | $113.72 | -2.1 | done | losing for real |
| coinflip | 2484 | 50.0 | 50.5 | $-1228.49 | -4.9% | $-228.49 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 1457 | 48.5 | 51.4 | $-1466.99 | -10.1% | $-466.99 | -4.0 | done | losing for real |
| momentum_5m_0.00pct | 2484 | 50.4 | 51.7 | $-1498.98 | -6.0% | $-498.98 | -3.1 | done | losing for real |
| always_up | 2484 | 47.5 | 49.7 | $-2092.16 | -8.4% | $-1092.16 | -4.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3912 | 48.2 | 49.2 | $-2430.82 |
| ETH | 4307 | 48.2 | 48.6 | $-2608.87 |
| SOL | 4470 | 48.0 | 48.8 | $-2931.56 |
| XRP | 4524 | 48.5 | 48.6 | $-2236.45 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
