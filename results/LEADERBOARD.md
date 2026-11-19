# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 18, 11:15 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 781 windows, 21549 settled trades, 52 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 404 | 32.9 | 34.9 | $-391.45 | -9.7% | $608.55 | -1.5 | done | can't tell from luck |
| momentum_60m_0.30pct | 1828 | 50.2 | 49.6 | $-655.86 | -3.6% | $344.14 | -1.5 | done | can't tell from luck |
| trend_filter | 1269 | 50.4 | 50.8 | $-717.72 | -5.7% | $282.28 | -2.1 | done | losing for real |
| reversal_15m_0.10pct | 2202 | 51.0 | 50.6 | $-772.05 | -3.5% | $227.95 | -1.6 | done | can't tell from luck |
| value_ev10 | 982 | 37.4 | 39.1 | $-774.62 | -7.9% | $225.38 | -2.0 | done | losing for real |
| value_ev5 | 1486 | 39.8 | 41.0 | $-992.25 | -6.7% | $7.75 | -2.2 | done | losing for real |
| coinflip | 3116 | 50.2 | 50.3 | $-1330.25 | -4.3% | $-330.25 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 1828 | 49.8 | 51.2 | $-1341.76 | -7.3% | $-341.76 | -3.2 | done | losing for real |
| momentum_15m_0.10pct | 2202 | 49.0 | 50.2 | $-1374.95 | -6.2% | $-374.95 | -2.9 | done | losing for real |
| momentum_5m_0.00pct | 3116 | 51.2 | 51.7 | $-1427.11 | -4.6% | $-427.11 | -2.6 | done | losing for real |
| always_up | 3116 | 47.3 | 49.6 | $-2717.60 | -8.7% | $-1717.60 | -4.9 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4895 | 48.3 | 49.1 | $-2865.64 |
| ETH | 5381 | 48.0 | 48.5 | $-3581.98 |
| SOL | 5609 | 48.1 | 48.6 | $-3246.03 |
| XRP | 5664 | 48.5 | 48.5 | $-2801.97 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
