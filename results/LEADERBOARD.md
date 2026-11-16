# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 16, 3:45 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 559 windows, 15489 settled trades, 54 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1315 | 51.1 | 49.7 | $-292.47 | -2.2% | $707.53 | -0.8 | done | can't tell from luck |
| value_ev20 | 306 | 33.0 | 35.2 | $-355.92 | -11.6% | $644.08 | -1.6 | done | can't tell from luck |
| trend_filter | 897 | 50.4 | 51.1 | $-516.64 | -5.8% | $483.36 | -1.8 | done | can't tell from luck |
| value_ev10 | 734 | 37.1 | 39.4 | $-759.27 | -10.3% | $240.73 | -2.3 | done | losing for real |
| momentum_15m_0.10pct | 1572 | 49.4 | 49.8 | $-828.16 | -5.3% | $171.84 | -2.1 | done | losing for real |
| reversal_15m_0.10pct | 1572 | 50.6 | 51.1 | $-922.94 | -5.9% | $77.06 | -2.4 | done | losing for real |
| value_ev5 | 1094 | 39.4 | 41.2 | $-944.39 | -8.6% | $55.61 | -2.5 | done | losing for real |
| coinflip | 2228 | 49.9 | 50.5 | $-1238.99 | -5.6% | $-238.99 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 1315 | 48.9 | 51.2 | $-1253.75 | -9.5% | $-253.75 | -3.6 | done | losing for real |
| momentum_5m_0.00pct | 2228 | 50.4 | 51.8 | $-1518.89 | -6.8% | $-518.89 | -3.4 | done | losing for real |
| always_up | 2228 | 47.0 | 49.9 | $-2296.48 | -10.3% | $-1296.48 | -4.9 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3502 | 47.6 | 49.2 | $-2762.35 |
| ETH | 3857 | 47.9 | 48.6 | $-2795.60 |
| SOL | 4041 | 47.7 | 48.7 | $-3086.57 |
| XRP | 4089 | 48.5 | 48.6 | $-2283.36 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
