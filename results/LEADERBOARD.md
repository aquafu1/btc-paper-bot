# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 28, 1:45 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1655 windows, 39429 settled trades, 381 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 841 | 34.4 | 35.2 | $-631.08 | -7.5% | $368.92 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 3874 | 50.8 | 49.9 | $-1024.04 | -2.6% | $-24.04 | -1.6 | done | can't tell from luck |
| value_ev10 | 1984 | 38.3 | 39.0 | $-1137.41 | -5.7% | $-137.41 | -2.1 | done | losing for real |
| reversal_60m_0.30pct | 3242 | 51.1 | 50.9 | $-1436.36 | -4.4% | $-436.36 | -2.6 | done | losing for real |
| value_ev5 | 2963 | 40.3 | 41.0 | $-1620.10 | -5.5% | $-620.10 | -2.5 | done | losing for real |
| momentum_60m_0.30pct | 3242 | 48.9 | 49.2 | $-1822.51 | -5.6% | $-822.51 | -3.2 | done | losing for real |
| trend_filter | 2309 | 48.3 | 50.4 | $-2124.47 | -9.2% | $-1124.47 | -4.5 | done | losing for real |
| momentum_15m_0.10pct | 3874 | 49.2 | 50.2 | $-2358.00 | -6.1% | $-1358.00 | -3.8 | done | losing for real |
| coinflip | 5700 | 49.9 | 49.9 | $-2517.37 | -4.4% | $-1517.37 | -3.3 | done | losing for real |
| momentum_5m_0.00pct | 5700 | 50.2 | 51.3 | $-3532.57 | -6.2% | $-2532.57 | -4.8 | done | losing for real |
| always_up | 5700 | 48.3 | 49.0 | $-3532.64 | -6.2% | $-2532.64 | -4.6 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 10616 | 47.9 | 48.5 | $-5995.42 |
| ETH | 11503 | 47.9 | 47.6 | $-6156.89 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
