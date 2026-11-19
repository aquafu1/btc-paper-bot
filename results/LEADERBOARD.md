# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 19, 1:00 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 836 windows, 22977 settled trades, 54 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 423 | 33.1 | 34.9 | $-400.80 | -9.5% | $599.20 | -1.5 | done | can't tell from luck |
| reversal_15m_0.10pct | 2345 | 51.0 | 50.6 | $-813.98 | -3.5% | $186.02 | -1.7 | done | can't tell from luck |
| momentum_60m_0.30pct | 1933 | 49.9 | 49.7 | $-873.55 | -4.5% | $126.45 | -2.0 | done | can't tell from luck |
| value_ev10 | 1047 | 37.2 | 39.1 | $-873.78 | -8.3% | $126.22 | -2.2 | done | losing for real |
| trend_filter | 1356 | 49.7 | 50.8 | $-991.58 | -7.3% | $8.42 | -2.8 | done | losing for real |
| value_ev5 | 1587 | 39.6 | 41.1 | $-1157.89 | -7.3% | $-157.89 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 1933 | 50.1 | 51.2 | $-1370.72 | -7.1% | $-370.72 | -3.2 | done | losing for real |
| coinflip | 3336 | 50.4 | 50.3 | $-1393.30 | -4.2% | $-393.30 | -2.4 | done | losing for real |
| momentum_15m_0.10pct | 2345 | 49.0 | 50.3 | $-1533.75 | -6.5% | $-533.75 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 3336 | 51.1 | 51.7 | $-1626.17 | -4.9% | $-626.17 | -2.9 | done | losing for real |
| always_up | 3336 | 47.3 | 49.6 | $-3045.12 | -9.1% | $-2045.12 | -5.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5223 | 48.1 | 49.1 | $-3317.47 |
| ETH | 5720 | 48.0 | 48.5 | $-3950.05 |
| SOL | 5993 | 48.2 | 48.6 | $-3507.28 |
| XRP | 6041 | 48.4 | 48.5 | $-3305.85 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
