# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 19, 7:15 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 861 windows, 23722 settled trades, 52 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 445 | 34.6 | 34.8 | $-223.90 | -5.0% | $776.10 | -0.8 | done | can't tell from luck |
| value_ev10 | 1084 | 37.8 | 39.1 | $-712.23 | -6.6% | $287.77 | -1.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 2004 | 50.1 | 49.7 | $-797.52 | -4.0% | $202.48 | -1.8 | done | can't tell from luck |
| trend_filter | 1394 | 50.1 | 50.9 | $-896.12 | -6.4% | $103.88 | -2.5 | done | losing for real |
| reversal_15m_0.10pct | 2421 | 50.7 | 50.5 | $-911.78 | -3.8% | $88.22 | -1.9 | done | can't tell from luck |
| value_ev5 | 1641 | 39.9 | 41.0 | $-1024.63 | -6.2% | $-24.63 | -2.1 | done | losing for real |
| momentum_15m_0.10pct | 2421 | 49.3 | 50.4 | $-1449.24 | -6.0% | $-449.24 | -3.0 | done | losing for real |
| reversal_60m_0.30pct | 2004 | 49.9 | 51.0 | $-1470.01 | -7.3% | $-470.01 | -3.4 | done | losing for real |
| coinflip | 3436 | 50.1 | 50.3 | $-1572.03 | -4.6% | $-572.03 | -2.7 | done | losing for real |
| momentum_5m_0.00pct | 3436 | 51.2 | 51.7 | $-1651.94 | -4.8% | $-651.94 | -2.9 | done | losing for real |
| always_up | 3436 | 47.0 | 49.5 | $-3272.46 | -9.5% | $-2272.46 | -5.6 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5408 | 48.3 | 49.0 | $-2981.41 |
| ETH | 5903 | 48.0 | 48.5 | $-3909.77 |
| SOL | 6191 | 48.2 | 48.5 | $-3565.29 |
| XRP | 6220 | 48.3 | 48.5 | $-3525.39 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
