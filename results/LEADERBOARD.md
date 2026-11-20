# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 19, 6:05 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 856 windows, 23642 settled trades, 21 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 444 | 34.5 | 34.8 | $-237.85 | -5.4% | $762.15 | -0.8 | done | can't tell from luck |
| value_ev10 | 1082 | 37.8 | 39.0 | $-716.18 | -6.6% | $283.82 | -1.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 2003 | 50.2 | 49.7 | $-787.52 | -3.9% | $212.48 | -1.8 | done | can't tell from luck |
| trend_filter | 1392 | 50.1 | 50.9 | $-893.02 | -6.4% | $106.98 | -2.5 | done | losing for real |
| reversal_15m_0.10pct | 2414 | 50.7 | 50.5 | $-945.22 | -3.9% | $54.78 | -1.9 | done | can't tell from luck |
| value_ev5 | 1633 | 39.9 | 41.0 | $-1015.18 | -6.2% | $-15.18 | -2.1 | done | losing for real |
| momentum_15m_0.10pct | 2414 | 49.3 | 50.3 | $-1412.08 | -5.8% | $-412.08 | -2.9 | done | losing for real |
| reversal_60m_0.30pct | 2003 | 49.8 | 51.0 | $-1479.22 | -7.4% | $-479.22 | -3.4 | done | losing for real |
| coinflip | 3419 | 50.2 | 50.3 | $-1496.47 | -4.4% | $-496.47 | -2.6 | done | losing for real |
| momentum_5m_0.00pct | 3419 | 51.3 | 51.7 | $-1555.41 | -4.5% | $-555.41 | -2.8 | done | losing for real |
| always_up | 3419 | 46.9 | 49.5 | $-3271.31 | -9.6% | $-2271.31 | -5.6 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5392 | 48.3 | 49.0 | $-2946.57 |
| ETH | 5888 | 48.1 | 48.5 | $-3848.25 |
| SOL | 6169 | 48.3 | 48.5 | $-3529.38 |
| XRP | 6193 | 48.3 | 48.5 | $-3485.26 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
