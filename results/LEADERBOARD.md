# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 26, 12:45 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1459 windows, 36908 settled trades, 376 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 748 | 34.1 | 35.3 | $-613.47 | -8.2% | $386.53 | -1.7 | done | can't tell from luck |
| value_ev10 | 1799 | 38.6 | 39.2 | $-920.25 | -5.1% | $79.75 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 3679 | 50.9 | 50.0 | $-993.59 | -2.7% | $6.41 | -1.6 | done | can't tell from luck |
| value_ev5 | 2708 | 40.4 | 41.1 | $-1420.24 | -5.2% | $-420.24 | -2.3 | done | losing for real |
| momentum_60m_0.30pct | 3090 | 49.2 | 49.3 | $-1558.88 | -5.0% | $-558.88 | -2.8 | done | losing for real |
| reversal_60m_0.30pct | 3090 | 50.8 | 51.0 | $-1567.17 | -5.1% | $-567.17 | -2.9 | done | losing for real |
| trend_filter | 2191 | 48.7 | 50.3 | $-1877.98 | -8.6% | $-877.98 | -4.1 | done | losing for real |
| momentum_15m_0.10pct | 3679 | 49.1 | 50.2 | $-2309.87 | -6.3% | $-1309.87 | -3.8 | done | losing for real |
| coinflip | 5308 | 50.0 | 50.0 | $-2333.69 | -4.4% | $-1333.69 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 5308 | 50.2 | 51.3 | $-3308.44 | -6.2% | $-2308.44 | -4.7 | done | losing for real |
| always_up | 5308 | 48.0 | 49.2 | $-3614.03 | -6.8% | $-2614.03 | -4.9 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 9450 | 48.0 | 48.7 | $-5224.17 |
| ETH | 10148 | 48.0 | 48.0 | $-5709.20 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
