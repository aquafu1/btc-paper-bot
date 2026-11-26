# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 26, 5:50 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1527 windows, 37766 settled trades, 371 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 766 | 34.6 | 35.4 | $-546.35 | -7.1% | $453.65 | -1.5 | done | can't tell from luck |
| value_ev10 | 1846 | 38.6 | 39.2 | $-939.95 | -5.1% | $60.05 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 3752 | 50.9 | 50.0 | $-980.98 | -2.6% | $19.02 | -1.6 | done | can't tell from luck |
| value_ev5 | 2785 | 40.6 | 41.1 | $-1349.07 | -4.8% | $-349.07 | -2.2 | done | losing for real |
| reversal_60m_0.30pct | 3147 | 51.1 | 51.0 | $-1453.77 | -4.6% | $-453.77 | -2.7 | done | losing for real |
| momentum_60m_0.30pct | 3147 | 48.9 | 49.2 | $-1703.00 | -5.4% | $-703.00 | -3.0 | done | losing for real |
| trend_filter | 2236 | 48.5 | 50.3 | $-1948.72 | -8.7% | $-948.72 | -4.2 | done | losing for real |
| momentum_15m_0.10pct | 3752 | 49.1 | 50.2 | $-2323.21 | -6.2% | $-1323.21 | -3.8 | done | losing for real |
| coinflip | 5445 | 50.0 | 50.0 | $-2382.47 | -4.4% | $-1382.47 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 5445 | 50.1 | 51.3 | $-3417.75 | -6.3% | $-2417.75 | -4.8 | done | losing for real |
| always_up | 5445 | 48.0 | 49.1 | $-3572.95 | -6.6% | $-2572.95 | -4.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 9854 | 48.0 | 48.7 | $-5537.80 |
| ETH | 10602 | 48.1 | 47.9 | $-5496.22 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
