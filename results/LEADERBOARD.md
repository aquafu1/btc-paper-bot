# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 17, 7:05 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 620 windows, 17145 settled trades, 39 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1452 | 51.4 | 49.6 | $-120.65 | -0.8% | $879.35 | -0.3 | done | can't tell from luck |
| value_ev20 | 329 | 34.0 | 35.3 | $-264.70 | -8.0% | $735.30 | -1.1 | done | can't tell from luck |
| trend_filter | 994 | 50.5 | 50.9 | $-490.12 | -4.9% | $509.88 | -1.6 | done | can't tell from luck |
| value_ev10 | 794 | 38.0 | 39.4 | $-607.33 | -7.6% | $392.67 | -1.8 | done | can't tell from luck |
| value_ev5 | 1198 | 40.2 | 41.3 | $-786.96 | -6.6% | $213.04 | -1.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 1755 | 50.7 | 51.0 | $-844.53 | -4.8% | $155.47 | -2.0 | done | losing for real |
| momentum_15m_0.10pct | 1755 | 49.3 | 50.0 | $-926.83 | -5.3% | $73.17 | -2.2 | done | losing for real |
| coinflip | 2472 | 50.0 | 50.5 | $-1233.99 | -5.0% | $-233.99 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 1452 | 48.6 | 51.4 | $-1435.24 | -9.9% | $-435.24 | -3.9 | done | losing for real |
| momentum_5m_0.00pct | 2472 | 50.4 | 51.7 | $-1523.00 | -6.2% | $-523.00 | -3.2 | done | losing for real |
| always_up | 2472 | 47.3 | 49.7 | $-2198.96 | -8.9% | $-1198.96 | -4.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3895 | 48.1 | 49.2 | $-2548.85 |
| ETH | 4290 | 48.0 | 48.6 | $-2708.38 |
| SOL | 4451 | 48.0 | 48.8 | $-2914.03 |
| XRP | 4509 | 48.5 | 48.5 | $-2261.04 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
