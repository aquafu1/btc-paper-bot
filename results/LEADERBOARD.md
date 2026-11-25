# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 24, 6:45 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1339 windows, 35225 settled trades, 411 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 694 | 34.3 | 35.4 | $-528.07 | -7.6% | $471.93 | -1.5 | done | can't tell from luck |
| value_ev10 | 1697 | 38.7 | 39.2 | $-830.05 | -4.9% | $169.95 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 3527 | 50.9 | 50.2 | $-999.25 | -2.8% | $0.75 | -1.7 | done | can't tell from luck |
| value_ev5 | 2562 | 40.4 | 41.1 | $-1325.90 | -5.2% | $-325.90 | -2.2 | done | losing for real |
| momentum_60m_0.30pct | 2959 | 49.4 | 49.5 | $-1440.85 | -4.9% | $-440.85 | -2.6 | done | losing for real |
| reversal_60m_0.30pct | 2959 | 50.6 | 50.9 | $-1545.83 | -5.2% | $-545.83 | -2.9 | done | losing for real |
| trend_filter | 2096 | 48.7 | 50.5 | $-1777.74 | -8.5% | $-777.74 | -4.0 | done | losing for real |
| momentum_15m_0.10pct | 3527 | 49.1 | 50.2 | $-2235.13 | -6.3% | $-1235.13 | -3.8 | done | losing for real |
| coinflip | 5068 | 49.9 | 50.1 | $-2348.78 | -4.6% | $-1348.78 | -3.3 | done | losing for real |
| momentum_5m_0.00pct | 5068 | 50.3 | 51.4 | $-3015.98 | -6.0% | $-2015.98 | -4.4 | done | losing for real |
| always_up | 5068 | 47.9 | 49.3 | $-3668.92 | -7.2% | $-2668.92 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 8622 | 47.9 | 48.9 | $-5234.50 |
| ETH | 9293 | 48.2 | 48.2 | $-4897.76 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
