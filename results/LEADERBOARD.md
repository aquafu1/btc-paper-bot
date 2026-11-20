# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 19, 11:45 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 879 windows, 24266 settled trades, 59 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 457 | 35.9 | 34.9 | $-59.37 | -1.3% | $940.63 | -0.2 | done | can't tell from luck |
| value_ev10 | 1112 | 38.5 | 39.1 | $-534.76 | -4.8% | $465.24 | -1.3 | done | can't tell from luck |
| momentum_60m_0.30pct | 2053 | 50.1 | 49.8 | $-839.16 | -4.1% | $160.84 | -1.9 | done | can't tell from luck |
| trend_filter | 1430 | 50.2 | 51.0 | $-907.04 | -6.3% | $92.96 | -2.5 | done | losing for real |
| value_ev5 | 1681 | 40.0 | 41.0 | $-941.98 | -5.6% | $58.02 | -1.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 2478 | 50.5 | 50.4 | $-994.09 | -4.0% | $5.91 | -2.0 | done | can't tell from luck |
| momentum_15m_0.10pct | 2478 | 49.5 | 50.4 | $-1365.15 | -5.5% | $-365.15 | -2.8 | done | losing for real |
| reversal_60m_0.30pct | 2053 | 49.9 | 50.9 | $-1398.09 | -6.8% | $-398.09 | -3.1 | done | losing for real |
| momentum_5m_0.00pct | 3508 | 51.3 | 51.7 | $-1539.35 | -4.4% | $-539.35 | -2.7 | done | losing for real |
| coinflip | 3508 | 50.1 | 50.3 | $-1579.02 | -4.5% | $-579.02 | -2.7 | done | losing for real |
| always_up | 3508 | 46.9 | 49.6 | $-3404.66 | -9.7% | $-2404.66 | -5.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5538 | 48.3 | 49.1 | $-2977.61 |
| ETH | 6037 | 48.2 | 48.5 | $-3702.36 |
| SOL | 6333 | 48.3 | 48.5 | $-3530.01 |
| XRP | 6358 | 48.4 | 48.5 | $-3352.69 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
