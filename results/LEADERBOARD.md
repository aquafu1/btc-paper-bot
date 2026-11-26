# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 26, 11:45 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1503 windows, 37464 settled trades, 377 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 760 | 34.3 | 35.4 | $-579.35 | -7.6% | $420.65 | -1.6 | done | can't tell from luck |
| value_ev10 | 1827 | 38.4 | 39.2 | $-997.14 | -5.5% | $2.86 | -1.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 3727 | 50.8 | 50.1 | $-1033.78 | -2.8% | $-33.78 | -1.7 | done | can't tell from luck |
| value_ev5 | 2757 | 40.5 | 41.1 | $-1385.02 | -5.0% | $-385.02 | -2.2 | done | losing for real |
| reversal_60m_0.30pct | 3129 | 51.1 | 51.0 | $-1437.96 | -4.6% | $-437.96 | -2.6 | done | losing for real |
| momentum_60m_0.30pct | 3129 | 48.9 | 49.2 | $-1697.92 | -5.4% | $-697.92 | -3.0 | done | losing for real |
| trend_filter | 2220 | 48.6 | 50.3 | $-1899.92 | -8.6% | $-899.92 | -4.1 | done | losing for real |
| momentum_15m_0.10pct | 3727 | 49.2 | 50.2 | $-2239.93 | -6.0% | $-1239.93 | -3.7 | done | losing for real |
| coinflip | 5396 | 50.0 | 50.0 | $-2342.42 | -4.3% | $-1342.42 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 5396 | 50.2 | 51.3 | $-3286.13 | -6.1% | $-2286.13 | -4.6 | done | losing for real |
| always_up | 5396 | 48.0 | 49.2 | $-3577.27 | -6.6% | $-2577.27 | -4.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 9712 | 48.0 | 48.7 | $-5327.43 |
| ETH | 10442 | 48.0 | 47.9 | $-5565.19 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
