# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 18, 4:45 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 755 windows, 20828 settled trades, 35 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 394 | 33.8 | 34.9 | $-291.45 | -7.4% | $708.55 | -1.1 | done | can't tell from luck |
| reversal_15m_0.10pct | 2126 | 51.5 | 50.6 | $-489.25 | -2.3% | $510.75 | -1.1 | done | can't tell from luck |
| value_ev10 | 957 | 38.0 | 39.1 | $-597.58 | -6.2% | $402.42 | -1.6 | done | can't tell from luck |
| momentum_60m_0.30pct | 1761 | 49.9 | 49.6 | $-689.40 | -3.9% | $310.60 | -1.6 | done | can't tell from luck |
| value_ev5 | 1441 | 40.4 | 41.1 | $-766.64 | -5.3% | $233.36 | -1.7 | done | can't tell from luck |
| trend_filter | 1226 | 49.8 | 50.9 | $-806.29 | -6.6% | $193.71 | -2.4 | done | losing for real |
| coinflip | 3012 | 50.5 | 50.3 | $-1100.68 | -3.7% | $-100.68 | -2.0 | done | losing for real |
| reversal_60m_0.30pct | 1761 | 50.1 | 51.2 | $-1182.60 | -6.7% | $-182.60 | -2.9 | done | losing for real |
| momentum_15m_0.10pct | 2126 | 48.5 | 50.2 | $-1545.75 | -7.3% | $-545.75 | -3.4 | done | losing for real |
| momentum_5m_0.00pct | 3012 | 50.9 | 51.8 | $-1580.00 | -5.2% | $-580.00 | -3.0 | done | losing for real |
| always_up | 3012 | 46.9 | 49.6 | $-2885.78 | -9.6% | $-1885.78 | -5.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4720 | 48.2 | 49.1 | $-2887.30 |
| ETH | 5194 | 48.1 | 48.6 | $-3391.48 |
| SOL | 5422 | 48.1 | 48.6 | $-3151.82 |
| XRP | 5492 | 48.6 | 48.5 | $-2504.84 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
