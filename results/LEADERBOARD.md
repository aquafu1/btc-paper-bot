# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 16, 3:50 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 559 windows, 15513 settled trades, 30 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1316 | 51.1 | 49.7 | $-286.77 | -2.2% | $713.23 | -0.8 | done | can't tell from luck |
| value_ev20 | 306 | 33.0 | 35.2 | $-355.92 | -11.6% | $644.08 | -1.6 | done | can't tell from luck |
| trend_filter | 899 | 50.5 | 51.1 | $-504.99 | -5.6% | $495.01 | -1.7 | done | can't tell from luck |
| value_ev10 | 734 | 37.1 | 39.4 | $-759.27 | -10.3% | $240.73 | -2.3 | done | losing for real |
| momentum_15m_0.10pct | 1576 | 49.5 | 49.8 | $-804.61 | -5.1% | $195.39 | -2.0 | done | losing for real |
| value_ev5 | 1094 | 39.4 | 41.2 | $-944.39 | -8.6% | $55.61 | -2.5 | done | losing for real |
| reversal_15m_0.10pct | 1576 | 50.5 | 51.1 | $-962.94 | -6.1% | $37.06 | -2.5 | done | losing for real |
| coinflip | 2232 | 49.9 | 50.5 | $-1262.79 | -5.7% | $-262.79 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 1316 | 48.9 | 51.2 | $-1263.75 | -9.6% | $-263.75 | -3.6 | done | losing for real |
| momentum_5m_0.00pct | 2232 | 50.4 | 51.8 | $-1511.04 | -6.8% | $-511.04 | -3.3 | done | losing for real |
| always_up | 2232 | 47.1 | 49.9 | $-2272.93 | -10.2% | $-1272.93 | -4.9 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3507 | 47.6 | 49.2 | $-2780.95 |
| ETH | 3863 | 47.9 | 48.6 | $-2791.82 |
| SOL | 4049 | 47.7 | 48.7 | $-3088.07 |
| XRP | 4094 | 48.6 | 48.6 | $-2268.56 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
