# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 27, 8:20 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1585 windows, 38527 settled trades, 374 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 810 | 34.4 | 35.1 | $-579.27 | -7.2% | $420.73 | -1.6 | done | can't tell from luck |
| value_ev10 | 1914 | 38.5 | 39.0 | $-976.47 | -5.1% | $23.53 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 3804 | 50.9 | 50.0 | $-976.54 | -2.6% | $23.46 | -1.6 | done | can't tell from luck |
| value_ev5 | 2874 | 40.5 | 41.0 | $-1412.04 | -4.9% | $-412.04 | -2.2 | done | losing for real |
| reversal_60m_0.30pct | 3186 | 51.0 | 50.9 | $-1497.76 | -4.7% | $-497.76 | -2.7 | done | losing for real |
| momentum_60m_0.30pct | 3186 | 49.0 | 49.2 | $-1678.08 | -5.3% | $-678.08 | -3.0 | done | losing for real |
| trend_filter | 2266 | 48.5 | 50.3 | $-1984.92 | -8.8% | $-984.92 | -4.3 | done | losing for real |
| coinflip | 5561 | 50.1 | 49.9 | $-2284.19 | -4.1% | $-1284.19 | -3.1 | done | losing for real |
| momentum_15m_0.10pct | 3804 | 49.1 | 50.2 | $-2363.14 | -6.2% | $-1363.14 | -3.9 | done | losing for real |
| momentum_5m_0.00pct | 5561 | 50.2 | 51.3 | $-3438.57 | -6.2% | $-2438.57 | -4.7 | done | losing for real |
| always_up | 5561 | 48.2 | 49.1 | $-3509.70 | -6.3% | $-2509.70 | -4.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 10206 | 48.0 | 48.6 | $-5652.74 |
| ETH | 11011 | 48.1 | 47.7 | $-5463.71 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
