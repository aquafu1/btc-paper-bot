# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 26, 12:05 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1504 windows, 37489 settled trades, 366 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 762 | 34.4 | 35.4 | $-577.73 | -7.6% | $422.27 | -1.6 | done | can't tell from luck |
| value_ev10 | 1829 | 38.4 | 39.2 | $-995.52 | -5.4% | $4.48 | -1.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 3729 | 50.9 | 50.1 | $-1014.07 | -2.7% | $-14.07 | -1.7 | done | can't tell from luck |
| value_ev5 | 2760 | 40.5 | 41.1 | $-1393.39 | -5.0% | $-393.39 | -2.2 | done | losing for real |
| reversal_60m_0.30pct | 3130 | 51.1 | 51.0 | $-1434.35 | -4.6% | $-434.35 | -2.6 | done | losing for real |
| momentum_60m_0.30pct | 3130 | 48.9 | 49.2 | $-1707.92 | -5.5% | $-707.92 | -3.0 | done | losing for real |
| trend_filter | 2220 | 48.6 | 50.3 | $-1899.92 | -8.6% | $-899.92 | -4.1 | done | losing for real |
| momentum_15m_0.10pct | 3729 | 49.1 | 50.2 | $-2259.93 | -6.1% | $-1259.93 | -3.7 | done | losing for real |
| coinflip | 5400 | 50.0 | 50.0 | $-2360.80 | -4.4% | $-1360.80 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 5400 | 50.2 | 51.3 | $-3295.35 | -6.1% | $-2295.35 | -4.6 | done | losing for real |
| always_up | 5400 | 48.0 | 49.2 | $-3577.55 | -6.6% | $-2577.55 | -4.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 9721 | 48.0 | 48.7 | $-5364.08 |
| ETH | 10458 | 48.0 | 47.9 | $-5568.23 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
