# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 17, 7:35 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 622 windows, 17184 settled trades, 59 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1453 | 51.3 | 49.6 | $-130.65 | -0.9% | $869.35 | -0.3 | done | can't tell from luck |
| value_ev20 | 329 | 34.0 | 35.3 | $-264.70 | -8.0% | $735.30 | -1.1 | done | can't tell from luck |
| trend_filter | 996 | 50.5 | 50.9 | $-491.18 | -4.9% | $508.82 | -1.6 | done | can't tell from luck |
| value_ev10 | 795 | 38.1 | 39.4 | $-595.97 | -7.5% | $404.03 | -1.7 | done | can't tell from luck |
| value_ev5 | 1200 | 40.3 | 41.4 | $-765.52 | -6.4% | $234.48 | -1.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 1759 | 50.7 | 51.0 | $-866.28 | -4.9% | $133.72 | -2.1 | done | losing for real |
| momentum_15m_0.10pct | 1759 | 49.3 | 50.0 | $-903.06 | -5.1% | $96.94 | -2.2 | done | losing for real |
| coinflip | 2480 | 50.0 | 50.5 | $-1232.25 | -5.0% | $-232.25 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 1453 | 48.7 | 51.4 | $-1426.99 | -9.8% | $-426.99 | -3.9 | done | losing for real |
| momentum_5m_0.00pct | 2480 | 50.5 | 51.7 | $-1458.98 | -5.9% | $-458.98 | -3.0 | done | losing for real |
| always_up | 2480 | 47.4 | 49.7 | $-2134.94 | -8.6% | $-1134.94 | -4.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3905 | 48.1 | 49.2 | $-2475.03 |
| ETH | 4301 | 48.1 | 48.6 | $-2632.54 |
| SOL | 4463 | 48.0 | 48.8 | $-2921.79 |
| XRP | 4515 | 48.5 | 48.5 | $-2241.16 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
