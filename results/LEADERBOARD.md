# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 18, 2:45 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 747 windows, 20606 settled trades, 67 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 387 | 33.3 | 34.9 | $-344.61 | -8.9% | $655.39 | -1.3 | done | can't tell from luck |
| reversal_15m_0.10pct | 2108 | 51.6 | 50.6 | $-484.41 | -2.3% | $515.59 | -1.1 | done | can't tell from luck |
| momentum_60m_0.30pct | 1742 | 50.1 | 49.5 | $-605.39 | -3.5% | $394.61 | -1.4 | done | can't tell from luck |
| value_ev10 | 943 | 37.8 | 39.1 | $-672.96 | -7.1% | $327.04 | -1.8 | done | can't tell from luck |
| trend_filter | 1214 | 49.9 | 50.9 | $-777.67 | -6.4% | $222.33 | -2.3 | done | losing for real |
| value_ev5 | 1422 | 40.2 | 41.1 | $-836.18 | -5.9% | $163.82 | -1.9 | done | can't tell from luck |
| coinflip | 2980 | 50.3 | 50.3 | $-1229.64 | -4.1% | $-229.64 | -2.3 | done | losing for real |
| reversal_60m_0.30pct | 1742 | 49.9 | 51.3 | $-1277.57 | -7.3% | $-277.57 | -3.1 | done | losing for real |
| momentum_15m_0.10pct | 2108 | 48.4 | 50.2 | $-1566.01 | -7.4% | $-566.01 | -3.4 | done | losing for real |
| momentum_5m_0.00pct | 2980 | 50.8 | 51.8 | $-1665.21 | -5.6% | $-665.21 | -3.2 | done | losing for real |
| always_up | 2980 | 46.8 | 49.6 | $-2870.39 | -9.6% | $-1870.39 | -5.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4665 | 48.1 | 49.1 | $-2953.82 |
| ETH | 5136 | 48.0 | 48.5 | $-3310.54 |
| SOL | 5371 | 48.0 | 48.6 | $-3325.17 |
| XRP | 5434 | 48.5 | 48.5 | $-2740.50 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
