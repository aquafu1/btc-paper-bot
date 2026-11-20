# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 19, 7:35 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 862 windows, 23769 settled trades, 23 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 445 | 34.6 | 34.8 | $-223.90 | -5.0% | $776.10 | -0.8 | done | can't tell from luck |
| value_ev10 | 1087 | 37.8 | 39.1 | $-721.42 | -6.6% | $278.58 | -1.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 2006 | 50.1 | 49.7 | $-796.71 | -4.0% | $203.29 | -1.8 | done | can't tell from luck |
| trend_filter | 1396 | 50.2 | 50.9 | $-882.46 | -6.3% | $117.54 | -2.4 | done | losing for real |
| reversal_15m_0.10pct | 2426 | 50.7 | 50.5 | $-925.61 | -3.8% | $74.39 | -1.9 | done | can't tell from luck |
| value_ev5 | 1648 | 39.7 | 41.0 | $-1073.81 | -6.5% | $-73.81 | -2.2 | done | losing for real |
| momentum_15m_0.10pct | 2426 | 49.3 | 50.4 | $-1443.34 | -5.9% | $-443.34 | -3.0 | done | losing for real |
| reversal_60m_0.30pct | 2006 | 49.9 | 51.0 | $-1471.76 | -7.3% | $-471.76 | -3.4 | done | losing for real |
| coinflip | 3443 | 50.1 | 50.3 | $-1606.47 | -4.7% | $-606.47 | -2.8 | done | losing for real |
| momentum_5m_0.00pct | 3443 | 51.2 | 51.7 | $-1617.02 | -4.7% | $-617.02 | -2.9 | done | losing for real |
| always_up | 3443 | 47.0 | 49.5 | $-3252.90 | -9.4% | $-2252.90 | -5.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5421 | 48.3 | 49.0 | $-2985.59 |
| ETH | 5915 | 48.0 | 48.5 | $-3940.59 |
| SOL | 6198 | 48.3 | 48.5 | $-3566.06 |
| XRP | 6235 | 48.3 | 48.5 | $-3523.16 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
