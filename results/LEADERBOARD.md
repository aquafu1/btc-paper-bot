# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 19, 7:20 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 813 windows, 22314 settled trades, 36 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 413 | 33.4 | 35.0 | $-341.28 | -8.3% | $658.72 | -1.3 | done | can't tell from luck |
| value_ev10 | 1019 | 37.8 | 39.2 | $-701.12 | -6.9% | $298.88 | -1.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 1869 | 49.9 | 49.6 | $-790.88 | -4.2% | $209.12 | -1.8 | done | can't tell from luck |
| trend_filter | 1309 | 50.0 | 50.9 | $-849.66 | -6.5% | $150.34 | -2.4 | done | losing for real |
| reversal_15m_0.10pct | 2280 | 50.8 | 50.6 | $-871.08 | -3.8% | $128.92 | -1.8 | done | can't tell from luck |
| value_ev5 | 1540 | 40.0 | 41.1 | $-933.25 | -6.1% | $66.75 | -2.0 | done | losing for real |
| reversal_60m_0.30pct | 1869 | 50.1 | 51.2 | $-1285.74 | -6.9% | $-285.74 | -3.0 | done | losing for real |
| momentum_15m_0.10pct | 2280 | 49.2 | 50.2 | $-1328.62 | -5.8% | $-328.62 | -2.8 | done | losing for real |
| coinflip | 3245 | 50.2 | 50.3 | $-1415.23 | -4.4% | $-415.23 | -2.5 | done | losing for real |
| momentum_5m_0.00pct | 3245 | 51.3 | 51.6 | $-1417.58 | -4.4% | $-417.58 | -2.6 | done | losing for real |
| always_up | 3245 | 47.4 | 49.7 | $-2830.11 | -8.7% | $-1830.11 | -5.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5067 | 48.3 | 49.1 | $-2901.26 |
| ETH | 5551 | 48.2 | 48.6 | $-3545.41 |
| SOL | 5817 | 48.2 | 48.6 | $-3280.43 |
| XRP | 5879 | 48.4 | 48.5 | $-3037.47 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
