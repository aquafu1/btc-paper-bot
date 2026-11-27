# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 26, 10:15 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1545 windows, 38025 settled trades, 408 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 782 | 34.0 | 35.3 | $-676.25 | -8.6% | $323.75 | -1.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 3770 | 50.9 | 50.0 | $-1017.85 | -2.7% | $-17.85 | -1.7 | done | can't tell from luck |
| value_ev10 | 1870 | 38.3 | 39.1 | $-1076.90 | -5.8% | $-76.90 | -2.0 | done | losing for real |
| value_ev5 | 2815 | 40.4 | 41.1 | $-1480.55 | -5.3% | $-480.55 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 3166 | 51.0 | 51.0 | $-1532.30 | -4.8% | $-532.30 | -2.8 | done | losing for real |
| momentum_60m_0.30pct | 3166 | 49.0 | 49.2 | $-1665.88 | -5.3% | $-665.88 | -2.9 | done | losing for real |
| trend_filter | 2246 | 48.6 | 50.3 | $-1921.41 | -8.6% | $-921.41 | -4.1 | done | losing for real |
| momentum_15m_0.10pct | 3770 | 49.1 | 50.2 | $-2325.64 | -6.2% | $-1325.64 | -3.8 | done | losing for real |
| coinflip | 5480 | 49.9 | 49.9 | $-2450.28 | -4.5% | $-1450.28 | -3.3 | done | losing for real |
| momentum_5m_0.00pct | 5480 | 50.2 | 51.3 | $-3377.57 | -6.2% | $-2377.57 | -4.7 | done | losing for real |
| always_up | 5480 | 48.1 | 49.2 | $-3574.03 | -6.5% | $-2574.03 | -4.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 9976 | 47.9 | 48.7 | $-5739.96 |
| ETH | 10739 | 48.0 | 47.8 | $-5774.46 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
