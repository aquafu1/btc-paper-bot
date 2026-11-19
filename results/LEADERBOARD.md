# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 18, 10:00 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 776 windows, 21394 settled trades, 69 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 403 | 33.0 | 34.9 | $-381.45 | -9.5% | $618.55 | -1.4 | done | can't tell from luck |
| reversal_15m_0.10pct | 2184 | 51.2 | 50.6 | $-655.22 | -3.0% | $344.78 | -1.4 | done | can't tell from luck |
| value_ev10 | 979 | 37.5 | 39.1 | $-744.62 | -7.6% | $255.38 | -1.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 1808 | 49.8 | 49.6 | $-762.92 | -4.2% | $237.08 | -1.8 | done | can't tell from luck |
| trend_filter | 1258 | 49.9 | 50.8 | $-802.59 | -6.4% | $197.41 | -2.3 | done | losing for real |
| value_ev5 | 1482 | 39.8 | 41.0 | $-975.88 | -6.6% | $24.12 | -2.1 | done | losing for real |
| reversal_60m_0.30pct | 1808 | 50.2 | 51.2 | $-1189.11 | -6.6% | $-189.11 | -2.9 | done | losing for real |
| coinflip | 3096 | 50.2 | 50.3 | $-1304.93 | -4.2% | $-304.93 | -2.4 | done | losing for real |
| momentum_15m_0.10pct | 2184 | 48.8 | 50.2 | $-1453.10 | -6.7% | $-453.10 | -3.1 | done | losing for real |
| momentum_5m_0.00pct | 3096 | 51.1 | 51.6 | $-1469.32 | -4.7% | $-469.32 | -2.7 | done | losing for real |
| always_up | 3096 | 47.1 | 49.5 | $-2824.66 | -9.1% | $-1824.66 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4859 | 48.2 | 49.1 | $-2929.99 |
| ETH | 5343 | 48.0 | 48.5 | $-3587.35 |
| SOL | 5569 | 48.1 | 48.6 | $-3279.62 |
| XRP | 5623 | 48.5 | 48.5 | $-2766.84 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
