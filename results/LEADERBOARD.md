# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 18, 10:30 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 730 windows, 20086 settled trades, 65 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 381 | 33.3 | 34.9 | $-334.03 | -8.8% | $665.97 | -1.3 | done | can't tell from luck |
| reversal_15m_0.10pct | 2058 | 51.7 | 50.7 | $-417.55 | -2.0% | $582.45 | -0.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 1684 | 50.1 | 49.5 | $-567.69 | -3.4% | $432.31 | -1.4 | done | can't tell from luck |
| value_ev10 | 920 | 38.0 | 39.1 | $-595.30 | -6.5% | $404.70 | -1.6 | done | can't tell from luck |
| value_ev5 | 1389 | 40.6 | 41.1 | $-700.36 | -5.0% | $299.64 | -1.6 | done | can't tell from luck |
| trend_filter | 1176 | 49.9 | 51.0 | $-749.46 | -6.4% | $250.54 | -2.2 | done | losing for real |
| coinflip | 2912 | 50.3 | 50.3 | $-1179.56 | -4.1% | $-179.56 | -2.2 | done | losing for real |
| reversal_60m_0.30pct | 1684 | 49.9 | 51.2 | $-1218.54 | -7.2% | $-218.54 | -3.0 | done | losing for real |
| momentum_15m_0.10pct | 2058 | 48.3 | 50.1 | $-1522.53 | -7.4% | $-522.53 | -3.4 | done | losing for real |
| momentum_5m_0.00pct | 2912 | 50.7 | 51.8 | $-1658.35 | -5.7% | $-658.35 | -3.2 | done | losing for real |
| always_up | 2912 | 47.0 | 49.6 | $-2665.04 | -9.2% | $-1665.04 | -4.9 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4547 | 48.1 | 49.1 | $-2878.99 |
| ETH | 5004 | 48.1 | 48.5 | $-3062.76 |
| SOL | 5231 | 48.1 | 48.7 | $-3078.89 |
| XRP | 5304 | 48.5 | 48.5 | $-2587.76 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
