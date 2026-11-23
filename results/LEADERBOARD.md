# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 23, 11:45 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1215 windows, 33384 settled trades, 323 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 652 | 34.5 | 35.3 | $-443.45 | -6.8% | $556.55 | -1.3 | done | can't tell from luck |
| value_ev10 | 1597 | 38.8 | 39.2 | $-766.01 | -4.8% | $233.99 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 3345 | 50.8 | 50.3 | $-1074.90 | -3.2% | $-74.90 | -1.9 | done | can't tell from luck |
| value_ev5 | 2415 | 40.5 | 41.1 | $-1181.23 | -4.9% | $-181.23 | -2.0 | done | losing for real |
| momentum_60m_0.30pct | 2799 | 49.5 | 49.4 | $-1272.59 | -4.5% | $-272.59 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 2799 | 50.5 | 51.1 | $-1659.23 | -5.9% | $-659.23 | -3.2 | done | losing for real |
| trend_filter | 1972 | 48.7 | 50.4 | $-1682.81 | -8.5% | $-682.81 | -3.9 | done | losing for real |
| momentum_15m_0.10pct | 3345 | 49.2 | 50.2 | $-2060.09 | -6.2% | $-1060.09 | -3.6 | done | losing for real |
| coinflip | 4820 | 50.0 | 50.1 | $-2207.85 | -4.6% | $-1207.85 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 4820 | 50.2 | 51.4 | $-2956.16 | -6.1% | $-1956.16 | -4.4 | done | losing for real |
| always_up | 4820 | 47.8 | 49.3 | $-3528.75 | -7.3% | $-2528.75 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7727 | 48.1 | 48.9 | $-4298.24 |
| ETH | 8347 | 48.0 | 48.3 | $-4950.60 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
