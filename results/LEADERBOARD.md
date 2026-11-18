# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 18, 5:45 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 759 windows, 20921 settled trades, 67 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 394 | 33.8 | 34.9 | $-291.45 | -7.4% | $708.55 | -1.1 | done | can't tell from luck |
| reversal_15m_0.10pct | 2137 | 51.5 | 50.6 | $-495.16 | -2.3% | $504.84 | -1.1 | done | can't tell from luck |
| value_ev10 | 958 | 38.0 | 39.1 | $-607.58 | -6.3% | $392.42 | -1.6 | done | can't tell from luck |
| momentum_60m_0.30pct | 1768 | 49.9 | 49.6 | $-686.42 | -3.9% | $313.58 | -1.6 | done | can't tell from luck |
| value_ev5 | 1445 | 40.3 | 41.1 | $-806.64 | -5.6% | $193.36 | -1.8 | done | can't tell from luck |
| trend_filter | 1230 | 49.8 | 50.9 | $-825.35 | -6.7% | $174.65 | -2.4 | done | losing for real |
| coinflip | 3028 | 50.4 | 50.3 | $-1136.67 | -3.8% | $-136.67 | -2.1 | done | losing for real |
| reversal_60m_0.30pct | 1768 | 50.1 | 51.2 | $-1206.22 | -6.8% | $-206.22 | -2.9 | done | losing for real |
| momentum_15m_0.10pct | 2137 | 48.5 | 50.2 | $-1572.49 | -7.4% | $-572.49 | -3.4 | done | losing for real |
| momentum_5m_0.00pct | 3028 | 50.8 | 51.7 | $-1657.80 | -5.5% | $-657.80 | -3.1 | done | losing for real |
| always_up | 3028 | 47.0 | 49.6 | $-2881.80 | -9.5% | $-1881.80 | -5.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4742 | 48.1 | 49.1 | $-2937.82 |
| ETH | 5217 | 48.0 | 48.6 | $-3483.86 |
| SOL | 5446 | 48.0 | 48.6 | $-3236.99 |
| XRP | 5516 | 48.6 | 48.5 | $-2508.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
