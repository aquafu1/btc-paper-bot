# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 23, 12:05 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1216 windows, 33408 settled trades, 334 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 652 | 34.5 | 35.3 | $-443.45 | -6.8% | $556.55 | -1.3 | done | can't tell from luck |
| value_ev10 | 1597 | 38.8 | 39.2 | $-766.01 | -4.8% | $233.99 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 3348 | 50.8 | 50.3 | $-1087.13 | -3.2% | $-87.13 | -1.9 | done | can't tell from luck |
| value_ev5 | 2415 | 40.5 | 41.1 | $-1181.23 | -4.9% | $-181.23 | -2.0 | done | losing for real |
| momentum_60m_0.30pct | 2802 | 49.5 | 49.4 | $-1266.35 | -4.5% | $-266.35 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 2802 | 50.5 | 51.1 | $-1671.46 | -6.0% | $-671.46 | -3.2 | done | losing for real |
| trend_filter | 1975 | 48.7 | 50.4 | $-1676.56 | -8.5% | $-676.56 | -3.9 | done | losing for real |
| momentum_15m_0.10pct | 3348 | 49.2 | 50.2 | $-2053.85 | -6.1% | $-1053.85 | -3.6 | done | losing for real |
| coinflip | 4823 | 50.0 | 50.1 | $-2183.83 | -4.5% | $-1183.83 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 4823 | 50.2 | 51.4 | $-2949.92 | -6.1% | $-1949.92 | -4.4 | done | losing for real |
| always_up | 4823 | 47.8 | 49.3 | $-3540.97 | -7.3% | $-2540.97 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7743 | 48.1 | 48.9 | $-4299.83 |
| ETH | 8355 | 48.1 | 48.3 | $-4936.71 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
