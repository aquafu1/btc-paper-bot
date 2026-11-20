# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 19, 10:30 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 874 windows, 24118 settled trades, 55 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 454 | 35.5 | 34.9 | $-126.41 | -2.8% | $873.59 | -0.4 | done | can't tell from luck |
| value_ev10 | 1106 | 38.3 | 39.1 | $-595.75 | -5.4% | $404.25 | -1.5 | done | can't tell from luck |
| momentum_60m_0.30pct | 2039 | 50.0 | 49.8 | $-857.75 | -4.2% | $142.25 | -1.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 2463 | 50.6 | 50.5 | $-945.89 | -3.8% | $54.11 | -1.9 | done | can't tell from luck |
| value_ev5 | 1669 | 40.0 | 41.0 | $-968.15 | -5.8% | $31.85 | -2.0 | done | can't tell from luck |
| trend_filter | 1421 | 50.0 | 51.0 | $-969.19 | -6.8% | $30.81 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 2039 | 50.0 | 51.0 | $-1391.12 | -6.8% | $-391.12 | -3.1 | done | losing for real |
| momentum_15m_0.10pct | 2463 | 49.4 | 50.4 | $-1427.90 | -5.8% | $-427.90 | -2.9 | done | losing for real |
| coinflip | 3488 | 50.1 | 50.3 | $-1585.60 | -4.5% | $-585.60 | -2.7 | done | losing for real |
| momentum_5m_0.00pct | 3488 | 51.3 | 51.8 | $-1625.94 | -4.7% | $-625.94 | -2.8 | done | losing for real |
| always_up | 3488 | 46.9 | 49.6 | $-3389.25 | -9.7% | $-2389.25 | -5.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5502 | 48.3 | 49.1 | $-2963.95 |
| ETH | 5998 | 48.1 | 48.5 | $-3849.79 |
| SOL | 6295 | 48.3 | 48.6 | $-3583.10 |
| XRP | 6323 | 48.4 | 48.5 | $-3486.09 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
