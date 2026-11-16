# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 16, 10:15 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 537 windows, 14854 settled trades, 64 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1270 | 51.4 | 49.7 | $-151.48 | -1.2% | $848.52 | -0.4 | done | can't tell from luck |
| value_ev20 | 284 | 34.2 | 35.5 | $-252.64 | -8.9% | $747.36 | -1.2 | done | can't tell from luck |
| trend_filter | 867 | 50.4 | 50.8 | $-445.28 | -5.1% | $554.72 | -1.5 | done | can't tell from luck |
| momentum_15m_0.10pct | 1505 | 50.2 | 49.8 | $-520.49 | -3.5% | $479.51 | -1.3 | done | can't tell from luck |
| value_ev10 | 696 | 37.6 | 39.7 | $-640.63 | -9.2% | $359.37 | -2.0 | done | losing for real |
| value_ev5 | 1037 | 39.8 | 41.5 | $-826.07 | -8.0% | $173.93 | -2.2 | done | losing for real |
| reversal_15m_0.10pct | 1505 | 49.8 | 51.3 | $-1149.34 | -7.6% | $-149.34 | -3.0 | done | losing for real |
| coinflip | 2140 | 49.8 | 50.6 | $-1237.66 | -5.8% | $-237.66 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 1270 | 48.6 | 51.3 | $-1271.97 | -10.0% | $-271.97 | -3.7 | done | losing for real |
| momentum_5m_0.00pct | 2140 | 50.0 | 51.7 | $-1524.42 | -7.1% | $-524.42 | -3.4 | done | losing for real |
| always_up | 2140 | 46.7 | 50.1 | $-2399.09 | -11.2% | $-1399.09 | -5.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3367 | 47.5 | 49.3 | $-2705.11 |
| ETH | 3704 | 48.1 | 48.7 | $-2473.45 |
| SOL | 3873 | 47.7 | 48.9 | $-2919.17 |
| XRP | 3910 | 48.4 | 48.8 | $-2321.33 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
