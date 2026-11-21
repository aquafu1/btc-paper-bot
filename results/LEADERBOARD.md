# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 21, 12:45 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 979 windows, 27193 settled trades, 56 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 502 | 34.5 | 34.9 | $-255.26 | -5.1% | $744.74 | -0.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 2776 | 51.3 | 50.5 | $-724.99 | -2.6% | $275.01 | -1.4 | done | can't tell from luck |
| value_ev10 | 1245 | 37.8 | 39.1 | $-787.53 | -6.3% | $212.47 | -1.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 2327 | 50.1 | 49.7 | $-937.26 | -4.0% | $62.74 | -1.9 | done | can't tell from luck |
| value_ev5 | 1884 | 39.8 | 41.0 | $-1124.87 | -6.0% | $-124.87 | -2.2 | done | losing for real |
| trend_filter | 1632 | 49.6 | 50.8 | $-1174.18 | -7.2% | $-174.18 | -3.0 | done | losing for real |
| reversal_60m_0.30pct | 2327 | 49.9 | 51.0 | $-1620.98 | -7.0% | $-620.98 | -3.4 | done | losing for real |
| coinflip | 3908 | 50.3 | 50.3 | $-1740.20 | -4.5% | $-740.20 | -2.8 | done | losing for real |
| momentum_15m_0.10pct | 2776 | 48.7 | 50.3 | $-1999.76 | -7.2% | $-999.76 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 3908 | 50.7 | 51.5 | $-2119.15 | -5.4% | $-1119.15 | -3.5 | done | losing for real |
| always_up | 3908 | 46.8 | 49.6 | $-3940.22 | -10.1% | $-2940.22 | -6.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6199 | 48.2 | 49.1 | $-3562.25 |
| ETH | 6760 | 48.0 | 48.5 | $-4369.19 |
| SOL | 7102 | 48.1 | 48.6 | $-4104.25 |
| XRP | 7132 | 48.1 | 48.4 | $-4388.68 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
