# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 27, 9:15 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1637 windows, 39207 settled trades, 374 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 834 | 34.4 | 35.2 | $-611.28 | -7.3% | $388.72 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 3860 | 50.8 | 49.9 | $-1057.63 | -2.7% | $-57.63 | -1.7 | done | can't tell from luck |
| value_ev10 | 1969 | 38.3 | 39.0 | $-1105.62 | -5.6% | $-105.62 | -2.0 | done | losing for real |
| reversal_60m_0.30pct | 3227 | 51.0 | 50.9 | $-1512.37 | -4.7% | $-512.37 | -2.7 | done | losing for real |
| value_ev5 | 2940 | 40.4 | 41.0 | $-1548.16 | -5.3% | $-548.16 | -2.4 | done | losing for real |
| momentum_60m_0.30pct | 3227 | 49.0 | 49.2 | $-1737.18 | -5.4% | $-737.18 | -3.0 | done | losing for real |
| trend_filter | 2298 | 48.5 | 50.4 | $-2028.35 | -8.8% | $-1028.35 | -4.3 | done | losing for real |
| momentum_15m_0.10pct | 3860 | 49.2 | 50.2 | $-2337.32 | -6.1% | $-1337.32 | -3.8 | done | losing for real |
| coinflip | 5664 | 50.0 | 49.9 | $-2457.47 | -4.3% | $-1457.47 | -3.3 | done | losing for real |
| momentum_5m_0.00pct | 5664 | 50.2 | 51.3 | $-3486.81 | -6.2% | $-2486.81 | -4.8 | done | losing for real |
| always_up | 5664 | 48.2 | 49.1 | $-3568.63 | -6.3% | $-2568.63 | -4.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 10511 | 48.0 | 48.6 | $-5908.70 |
| ETH | 11386 | 47.9 | 47.6 | $-5957.89 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
