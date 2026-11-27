# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 26, 8:20 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1537 windows, 37913 settled trades, 380 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 777 | 34.2 | 35.4 | $-626.25 | -8.1% | $373.75 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 3761 | 50.9 | 50.0 | $-976.82 | -2.6% | $23.18 | -1.6 | done | can't tell from luck |
| value_ev10 | 1860 | 38.4 | 39.2 | $-1027.26 | -5.5% | $-27.26 | -1.9 | done | can't tell from luck |
| value_ev5 | 2803 | 40.5 | 41.1 | $-1431.63 | -5.1% | $-431.63 | -2.3 | done | losing for real |
| reversal_60m_0.30pct | 3156 | 51.0 | 51.0 | $-1474.18 | -4.7% | $-474.18 | -2.7 | done | losing for real |
| momentum_60m_0.30pct | 3156 | 49.0 | 49.2 | $-1695.26 | -5.4% | $-695.26 | -3.0 | done | losing for real |
| trend_filter | 2244 | 48.6 | 50.3 | $-1931.36 | -8.6% | $-931.36 | -4.2 | done | losing for real |
| momentum_15m_0.10pct | 3761 | 49.1 | 50.2 | $-2350.59 | -6.2% | $-1350.59 | -3.9 | done | losing for real |
| coinflip | 5465 | 49.9 | 50.0 | $-2455.21 | -4.5% | $-1455.21 | -3.3 | done | losing for real |
| momentum_5m_0.00pct | 5465 | 50.2 | 51.3 | $-3403.46 | -6.2% | $-2403.46 | -4.7 | done | losing for real |
| always_up | 5465 | 48.1 | 49.2 | $-3566.09 | -6.5% | $-2566.09 | -4.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 9916 | 47.9 | 48.7 | $-5735.78 |
| ETH | 10687 | 48.1 | 47.9 | $-5618.09 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
