# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 17, 6:05 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 616 windows, 17019 settled trades, 63 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1436 | 51.3 | 49.7 | $-192.89 | -1.3% | $807.11 | -0.5 | done | can't tell from luck |
| value_ev20 | 328 | 34.1 | 35.3 | $-254.70 | -7.8% | $745.30 | -1.1 | done | can't tell from luck |
| trend_filter | 984 | 50.5 | 51.0 | $-522.10 | -5.3% | $477.90 | -1.7 | done | can't tell from luck |
| value_ev10 | 792 | 38.0 | 39.4 | $-601.87 | -7.6% | $398.13 | -1.8 | done | can't tell from luck |
| value_ev5 | 1195 | 40.2 | 41.3 | $-794.88 | -6.7% | $205.12 | -2.0 | done | can't tell from luck |
| reversal_15m_0.10pct | 1740 | 50.6 | 50.9 | $-844.83 | -4.9% | $155.17 | -2.0 | done | losing for real |
| momentum_15m_0.10pct | 1740 | 49.4 | 50.1 | $-935.34 | -5.4% | $64.66 | -2.3 | done | losing for real |
| coinflip | 2456 | 50.1 | 50.5 | $-1177.97 | -4.8% | $-177.97 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 1436 | 48.7 | 51.3 | $-1366.34 | -9.5% | $-366.34 | -3.7 | done | losing for real |
| momentum_5m_0.00pct | 2456 | 50.5 | 51.8 | $-1509.35 | -6.1% | $-509.35 | -3.2 | done | losing for real |
| always_up | 2456 | 47.2 | 49.8 | $-2271.20 | -9.2% | $-1271.20 | -4.6 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3864 | 48.1 | 49.2 | $-2503.22 |
| ETH | 4258 | 48.0 | 48.6 | $-2782.44 |
| SOL | 4421 | 48.0 | 48.8 | $-2890.71 |
| XRP | 4476 | 48.5 | 48.6 | $-2295.09 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
