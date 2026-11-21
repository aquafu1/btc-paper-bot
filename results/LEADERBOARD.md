# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 21, 1:00 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1028 windows, 28611 settled trades, 27 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 530 | 34.7 | 35.1 | $-278.51 | -5.3% | $721.49 | -0.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 2914 | 51.1 | 50.5 | $-870.19 | -3.0% | $129.81 | -1.6 | done | can't tell from luck |
| value_ev10 | 1316 | 37.6 | 39.2 | $-940.06 | -7.1% | $59.94 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 2459 | 49.9 | 49.6 | $-1062.65 | -4.3% | $-62.65 | -2.1 | done | losing for real |
| trend_filter | 1715 | 49.4 | 50.7 | $-1281.06 | -7.5% | $-281.06 | -3.2 | done | losing for real |
| value_ev5 | 1992 | 39.5 | 41.0 | $-1368.88 | -6.9% | $-368.88 | -2.6 | done | losing for real |
| reversal_60m_0.30pct | 2459 | 50.1 | 51.0 | $-1647.90 | -6.7% | $-647.90 | -3.4 | done | losing for real |
| coinflip | 4104 | 50.5 | 50.3 | $-1691.84 | -4.1% | $-691.84 | -2.7 | done | losing for real |
| momentum_15m_0.10pct | 2914 | 48.9 | 50.3 | $-1948.93 | -6.7% | $-948.93 | -3.6 | done | losing for real |
| momentum_5m_0.00pct | 4104 | 50.6 | 51.5 | $-2306.45 | -5.6% | $-1306.45 | -3.7 | done | losing for real |
| always_up | 4104 | 47.4 | 49.5 | $-3547.30 | -8.6% | $-2547.30 | -5.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6522 | 48.3 | 49.1 | $-3556.46 |
| ETH | 7103 | 48.1 | 48.5 | $-4395.23 |
| SOL | 7469 | 48.2 | 48.6 | $-4262.21 |
| XRP | 7517 | 48.1 | 48.4 | $-4729.88 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
