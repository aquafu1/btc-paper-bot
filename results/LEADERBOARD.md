# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 26, 5:30 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1526 windows, 37747 settled trades, 383 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 766 | 34.6 | 35.4 | $-546.35 | -7.1% | $453.65 | -1.5 | done | can't tell from luck |
| value_ev10 | 1845 | 38.6 | 39.2 | $-929.95 | -5.0% | $70.05 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 3750 | 50.9 | 50.0 | $-960.98 | -2.6% | $39.02 | -1.6 | done | can't tell from luck |
| value_ev5 | 2784 | 40.6 | 41.1 | $-1339.07 | -4.8% | $-339.07 | -2.2 | done | losing for real |
| reversal_60m_0.30pct | 3146 | 51.1 | 51.0 | $-1443.77 | -4.6% | $-443.77 | -2.6 | done | losing for real |
| momentum_60m_0.30pct | 3146 | 48.9 | 49.2 | $-1712.90 | -5.4% | $-712.90 | -3.0 | done | losing for real |
| trend_filter | 2234 | 48.5 | 50.3 | $-1948.62 | -8.7% | $-948.62 | -4.2 | done | losing for real |
| momentum_15m_0.10pct | 3750 | 49.1 | 50.2 | $-2341.88 | -6.2% | $-1341.88 | -3.9 | done | losing for real |
| coinflip | 5442 | 50.0 | 50.0 | $-2371.24 | -4.4% | $-1371.24 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 5442 | 50.1 | 51.4 | $-3407.65 | -6.3% | $-2407.65 | -4.8 | done | losing for real |
| always_up | 5442 | 48.1 | 49.1 | $-3557.63 | -6.5% | $-2557.63 | -4.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 9843 | 48.0 | 48.7 | $-5480.01 |
| ETH | 10594 | 48.1 | 47.9 | $-5495.82 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
