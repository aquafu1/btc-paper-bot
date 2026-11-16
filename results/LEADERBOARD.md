# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 16, 3:15 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 557 windows, 15448 settled trades, 41 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1313 | 51.2 | 49.7 | $-272.47 | -2.1% | $727.53 | -0.8 | done | can't tell from luck |
| value_ev20 | 306 | 33.0 | 35.2 | $-355.92 | -11.6% | $644.08 | -1.6 | done | can't tell from luck |
| trend_filter | 896 | 50.4 | 51.0 | $-506.64 | -5.7% | $493.36 | -1.7 | done | can't tell from luck |
| value_ev10 | 732 | 37.0 | 39.3 | $-762.65 | -10.4% | $237.35 | -2.3 | done | losing for real |
| momentum_15m_0.10pct | 1569 | 49.3 | 49.8 | $-864.70 | -5.5% | $135.30 | -2.2 | done | losing for real |
| reversal_15m_0.10pct | 1569 | 50.7 | 51.1 | $-892.94 | -5.7% | $107.06 | -2.3 | done | losing for real |
| value_ev5 | 1090 | 39.4 | 41.2 | $-927.77 | -8.5% | $72.23 | -2.4 | done | losing for real |
| coinflip | 2220 | 49.9 | 50.5 | $-1274.72 | -5.7% | $-274.72 | -2.8 | done | losing for real |
| reversal_60m_0.30pct | 1313 | 48.8 | 51.2 | $-1280.63 | -9.8% | $-280.63 | -3.6 | done | losing for real |
| momentum_5m_0.00pct | 2220 | 50.4 | 51.8 | $-1529.28 | -6.9% | $-529.28 | -3.4 | done | losing for real |
| always_up | 2220 | 46.8 | 49.9 | $-2399.74 | -10.8% | $-1399.74 | -5.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3493 | 47.5 | 49.2 | $-2807.40 |
| ETH | 3847 | 47.9 | 48.6 | $-2805.39 |
| SOL | 4033 | 47.7 | 48.7 | $-3123.90 |
| XRP | 4075 | 48.5 | 48.6 | $-2330.76 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
