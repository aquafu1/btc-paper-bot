# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 22, 5:20 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1093 windows, 30254 settled trades, 45 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 570 | 34.6 | 35.0 | $-327.96 | -5.8% | $672.04 | -1.0 | done | can't tell from luck |
| value_ev10 | 1401 | 38.0 | 39.1 | $-856.74 | -6.1% | $143.26 | -1.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 3056 | 51.0 | 50.5 | $-905.81 | -3.0% | $94.19 | -1.6 | done | can't tell from luck |
| momentum_60m_0.30pct | 2575 | 49.7 | 49.4 | $-1104.77 | -4.3% | $-104.77 | -2.2 | done | losing for real |
| value_ev5 | 2129 | 40.0 | 41.0 | $-1217.52 | -5.7% | $-217.52 | -2.2 | done | losing for real |
| trend_filter | 1797 | 49.4 | 50.4 | $-1311.80 | -7.3% | $-311.80 | -3.2 | done | losing for real |
| coinflip | 4365 | 50.6 | 50.2 | $-1603.13 | -3.7% | $-603.13 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 2575 | 50.3 | 51.1 | $-1651.36 | -6.4% | $-651.36 | -3.3 | done | losing for real |
| momentum_15m_0.10pct | 3056 | 49.0 | 50.2 | $-1980.86 | -6.5% | $-980.86 | -3.6 | done | losing for real |
| momentum_5m_0.00pct | 4365 | 50.8 | 51.4 | $-2198.46 | -5.0% | $-1198.46 | -3.4 | done | losing for real |
| always_up | 4365 | 47.5 | 49.3 | $-3521.83 | -8.1% | $-2521.83 | -5.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6923 | 48.5 | 49.0 | $-3354.98 |
| ETH | 7493 | 48.2 | 48.4 | $-4392.42 |
| SOL | 7882 | 48.1 | 48.4 | $-4431.30 |
| XRP | 7956 | 48.3 | 48.2 | $-4501.56 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
