# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 26, 12:30 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1458 windows, 36892 settled trades, 376 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 748 | 34.1 | 35.3 | $-613.47 | -8.2% | $386.53 | -1.7 | done | can't tell from luck |
| value_ev10 | 1799 | 38.6 | 39.2 | $-920.25 | -5.1% | $79.75 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 3677 | 50.9 | 50.0 | $-1009.53 | -2.7% | $-9.53 | -1.7 | done | can't tell from luck |
| value_ev5 | 2708 | 40.4 | 41.1 | $-1420.24 | -5.2% | $-420.24 | -2.3 | done | losing for real |
| momentum_60m_0.30pct | 3088 | 49.2 | 49.3 | $-1538.88 | -5.0% | $-538.88 | -2.8 | done | losing for real |
| reversal_60m_0.30pct | 3088 | 50.8 | 51.0 | $-1583.10 | -5.1% | $-583.10 | -2.9 | done | losing for real |
| trend_filter | 2189 | 48.7 | 50.4 | $-1857.98 | -8.5% | $-857.98 | -4.1 | done | losing for real |
| momentum_15m_0.10pct | 3677 | 49.1 | 50.2 | $-2289.87 | -6.2% | $-1289.87 | -3.8 | done | losing for real |
| coinflip | 5306 | 50.0 | 50.0 | $-2313.69 | -4.4% | $-1313.69 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 5306 | 50.2 | 51.3 | $-3288.44 | -6.2% | $-2288.44 | -4.6 | done | losing for real |
| always_up | 5306 | 48.0 | 49.2 | $-3629.97 | -6.8% | $-2629.97 | -4.9 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 9442 | 48.0 | 48.7 | $-5200.48 |
| ETH | 10140 | 48.0 | 48.0 | $-5680.70 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
