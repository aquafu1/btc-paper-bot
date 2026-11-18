# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 17, 6:20 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 665 windows, 18402 settled trades, 32 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 343 | 34.1 | 35.4 | $-267.49 | -7.8% | $732.51 | -1.1 | done | can't tell from luck |
| momentum_60m_0.30pct | 1565 | 50.4 | 49.6 | $-437.13 | -2.8% | $562.87 | -1.1 | done | can't tell from luck |
| reversal_15m_0.10pct | 1887 | 51.5 | 50.9 | $-565.24 | -3.0% | $434.76 | -1.3 | done | can't tell from luck |
| trend_filter | 1067 | 50.3 | 51.0 | $-595.94 | -5.6% | $404.06 | -1.9 | done | can't tell from luck |
| value_ev10 | 844 | 38.2 | 39.5 | $-631.06 | -7.5% | $368.94 | -1.8 | done | can't tell from luck |
| value_ev5 | 1276 | 40.6 | 41.4 | $-746.42 | -5.8% | $253.58 | -1.8 | done | can't tell from luck |
| coinflip | 2656 | 50.2 | 50.4 | $-1181.73 | -4.4% | $-181.73 | -2.3 | done | losing for real |
| reversal_60m_0.30pct | 1565 | 49.6 | 51.3 | $-1222.50 | -7.8% | $-222.50 | -3.2 | done | losing for real |
| momentum_15m_0.10pct | 1887 | 48.5 | 50.1 | $-1311.62 | -7.0% | $-311.62 | -3.0 | done | losing for real |
| momentum_5m_0.00pct | 2656 | 50.8 | 51.8 | $-1448.60 | -5.5% | $-448.60 | -2.9 | done | losing for real |
| always_up | 2656 | 47.6 | 49.7 | $-2220.01 | -8.4% | $-1220.01 | -4.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4182 | 48.3 | 49.3 | $-2604.42 |
| ETH | 4591 | 48.2 | 48.7 | $-2885.42 |
| SOL | 4792 | 48.2 | 48.8 | $-2823.09 |
| XRP | 4837 | 48.6 | 48.6 | $-2314.80 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
