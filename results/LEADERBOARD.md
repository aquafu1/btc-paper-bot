# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 19, 9:45 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 823 windows, 22584 settled trades, 75 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 418 | 33.5 | 34.9 | $-350.80 | -8.4% | $649.20 | -1.3 | done | can't tell from luck |
| value_ev10 | 1033 | 37.7 | 39.2 | $-756.63 | -7.3% | $243.37 | -1.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 1890 | 49.9 | 49.6 | $-804.37 | -4.3% | $195.63 | -1.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 2303 | 50.9 | 50.7 | $-837.39 | -3.6% | $162.61 | -1.8 | done | can't tell from luck |
| trend_filter | 1330 | 49.8 | 50.9 | $-911.76 | -6.9% | $88.24 | -2.6 | done | losing for real |
| value_ev5 | 1565 | 39.9 | 41.1 | $-1020.83 | -6.5% | $-20.83 | -2.2 | done | losing for real |
| reversal_60m_0.30pct | 1890 | 50.1 | 51.2 | $-1322.43 | -7.0% | $-322.43 | -3.1 | done | losing for real |
| momentum_15m_0.10pct | 2303 | 49.1 | 50.2 | $-1412.67 | -6.1% | $-412.67 | -3.0 | done | losing for real |
| momentum_5m_0.00pct | 3284 | 51.2 | 51.7 | $-1492.72 | -4.5% | $-492.72 | -2.7 | done | losing for real |
| coinflip | 3284 | 50.1 | 50.3 | $-1507.41 | -4.6% | $-507.41 | -2.6 | done | losing for real |
| always_up | 3284 | 47.4 | 49.6 | $-2885.88 | -8.8% | $-1885.88 | -5.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5125 | 48.2 | 49.1 | $-3136.74 |
| ETH | 5621 | 48.1 | 48.5 | $-3749.44 |
| SOL | 5890 | 48.3 | 48.6 | $-3298.18 |
| XRP | 5948 | 48.5 | 48.5 | $-3118.52 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
