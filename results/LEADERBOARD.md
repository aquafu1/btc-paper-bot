# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 19, 3:15 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 845 windows, 23261 settled trades, 59 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 430 | 33.7 | 34.9 | $-317.48 | -7.4% | $682.52 | -1.2 | done | can't tell from luck |
| value_ev10 | 1061 | 37.6 | 39.1 | $-776.71 | -7.3% | $223.29 | -1.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 1963 | 50.1 | 49.7 | $-831.91 | -4.2% | $168.09 | -1.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 2376 | 50.9 | 50.5 | $-849.28 | -3.6% | $150.72 | -1.7 | done | can't tell from luck |
| trend_filter | 1369 | 49.9 | 50.9 | $-951.29 | -6.9% | $48.71 | -2.6 | done | losing for real |
| value_ev5 | 1607 | 39.8 | 41.1 | $-1079.26 | -6.7% | $-79.26 | -2.3 | done | losing for real |
| reversal_60m_0.30pct | 1963 | 49.9 | 51.1 | $-1416.96 | -7.2% | $-416.96 | -3.3 | done | losing for real |
| coinflip | 3372 | 50.3 | 50.3 | $-1455.95 | -4.3% | $-455.95 | -2.5 | done | losing for real |
| momentum_15m_0.10pct | 2376 | 49.1 | 50.3 | $-1483.99 | -6.2% | $-483.99 | -3.1 | done | losing for real |
| momentum_5m_0.00pct | 3372 | 51.2 | 51.7 | $-1635.00 | -4.8% | $-635.00 | -2.9 | done | losing for real |
| always_up | 3372 | 47.0 | 49.5 | $-3188.82 | -9.5% | $-2188.82 | -5.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5295 | 48.2 | 49.1 | $-3138.62 |
| ETH | 5791 | 48.0 | 48.5 | $-3964.60 |
| SOL | 6065 | 48.2 | 48.6 | $-3614.04 |
| XRP | 6110 | 48.4 | 48.5 | $-3269.41 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
