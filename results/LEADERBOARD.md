# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 19, 3:05 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 796 windows, 21910 settled trades, 46 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 405 | 33.1 | 34.9 | $-372.37 | -9.2% | $627.63 | -1.4 | done | can't tell from luck |
| momentum_60m_0.30pct | 1849 | 50.2 | 49.6 | $-675.56 | -3.7% | $324.44 | -1.6 | done | can't tell from luck |
| value_ev10 | 1001 | 37.8 | 39.2 | $-698.48 | -7.0% | $301.52 | -1.8 | done | can't tell from luck |
| trend_filter | 1286 | 50.4 | 50.8 | $-717.79 | -5.6% | $282.21 | -2.1 | done | losing for real |
| reversal_15m_0.10pct | 2239 | 50.7 | 50.6 | $-880.86 | -3.9% | $119.14 | -1.9 | done | can't tell from luck |
| value_ev5 | 1511 | 40.0 | 41.1 | $-904.20 | -6.0% | $95.80 | -2.0 | done | can't tell from luck |
| momentum_15m_0.10pct | 2239 | 49.3 | 50.2 | $-1286.66 | -5.7% | $-286.66 | -2.7 | done | losing for real |
| momentum_5m_0.00pct | 3177 | 51.4 | 51.7 | $-1349.12 | -4.2% | $-349.12 | -2.5 | done | losing for real |
| coinflip | 3177 | 50.2 | 50.3 | $-1349.67 | -4.2% | $-349.67 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 1849 | 49.8 | 51.2 | $-1361.44 | -7.4% | $-361.44 | -3.2 | done | losing for real |
| always_up | 3177 | 47.5 | 49.6 | $-2717.69 | -8.6% | $-1717.69 | -4.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4981 | 48.3 | 49.1 | $-2883.91 |
| ETH | 5458 | 48.2 | 48.5 | $-3428.68 |
| SOL | 5707 | 48.3 | 48.6 | $-3130.28 |
| XRP | 5764 | 48.5 | 48.5 | $-2870.98 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
