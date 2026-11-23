# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 23, 4:45 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1187 windows, 32807 settled trades, 51 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 640 | 35.0 | 35.3 | $-348.79 | -5.4% | $651.21 | -1.0 | done | can't tell from luck |
| value_ev10 | 1557 | 38.7 | 39.2 | $-742.33 | -4.8% | $257.67 | -1.5 | done | can't tell from luck |
| reversal_15m_0.10pct | 3286 | 50.8 | 50.3 | $-1074.21 | -3.3% | $-74.21 | -1.9 | done | can't tell from luck |
| value_ev5 | 2357 | 40.3 | 41.1 | $-1235.79 | -5.2% | $-235.79 | -2.2 | done | losing for real |
| momentum_60m_0.30pct | 2760 | 49.6 | 49.4 | $-1247.11 | -4.5% | $-247.11 | -2.4 | done | losing for real |
| trend_filter | 1941 | 48.8 | 50.5 | $-1627.84 | -8.4% | $-627.84 | -3.8 | done | losing for real |
| reversal_60m_0.30pct | 2760 | 50.4 | 51.1 | $-1671.96 | -6.1% | $-671.96 | -3.3 | done | losing for real |
| momentum_15m_0.10pct | 3286 | 49.2 | 50.3 | $-1995.75 | -6.1% | $-995.75 | -3.5 | done | losing for real |
| coinflip | 4740 | 50.0 | 50.2 | $-2145.36 | -4.5% | $-1145.36 | -3.1 | done | losing for real |
| momentum_5m_0.00pct | 4740 | 50.1 | 51.4 | $-3042.23 | -6.4% | $-2042.23 | -4.6 | done | losing for real |
| always_up | 4740 | 47.8 | 49.3 | $-3443.86 | -7.3% | $-2443.86 | -5.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7526 | 48.2 | 48.9 | $-4146.03 |
| ETH | 8133 | 48.0 | 48.4 | $-4962.28 |
| SOL | 8538 | 48.2 | 48.4 | $-4375.36 |
| XRP | 8610 | 48.1 | 48.2 | $-5091.57 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
