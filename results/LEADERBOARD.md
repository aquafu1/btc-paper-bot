# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 25, 6:20 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1433 windows, 36580 settled trades, 420 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 738 | 34.6 | 35.3 | $-513.47 | -7.0% | $486.53 | -1.4 | done | can't tell from luck |
| value_ev10 | 1778 | 38.8 | 39.1 | $-801.03 | -4.5% | $198.97 | -1.5 | done | can't tell from luck |
| reversal_15m_0.10pct | 3651 | 50.9 | 50.0 | $-986.63 | -2.7% | $13.37 | -1.6 | done | can't tell from luck |
| value_ev5 | 2680 | 40.6 | 41.1 | $-1285.48 | -4.8% | $-285.48 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 3068 | 49.3 | 49.3 | $-1488.96 | -4.9% | $-488.96 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 3068 | 50.7 | 51.0 | $-1594.04 | -5.2% | $-594.04 | -2.9 | done | losing for real |
| trend_filter | 2172 | 48.6 | 50.3 | $-1880.11 | -8.7% | $-880.11 | -4.1 | done | losing for real |
| coinflip | 5258 | 50.1 | 50.0 | $-2181.42 | -4.1% | $-1181.42 | -3.0 | done | losing for real |
| momentum_15m_0.10pct | 3651 | 49.1 | 50.2 | $-2257.03 | -6.2% | $-1257.03 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 5258 | 50.2 | 51.4 | $-3263.72 | -6.2% | $-2263.72 | -4.6 | done | losing for real |
| always_up | 5258 | 48.0 | 49.2 | $-3576.56 | -6.8% | $-2576.56 | -4.9 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 9286 | 48.1 | 48.7 | $-4816.82 |
| ETH | 9984 | 48.0 | 48.0 | $-5427.40 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
