# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 27, 9:45 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1639 windows, 39232 settled trades, 392 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 834 | 34.4 | 35.2 | $-611.28 | -7.3% | $388.72 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 3860 | 50.8 | 49.9 | $-1057.63 | -2.7% | $-57.63 | -1.7 | done | can't tell from luck |
| value_ev10 | 1970 | 38.4 | 39.0 | $-1096.49 | -5.6% | $-96.49 | -2.0 | done | losing for real |
| reversal_60m_0.30pct | 3231 | 51.0 | 50.9 | $-1512.94 | -4.7% | $-512.94 | -2.7 | done | losing for real |
| value_ev5 | 2942 | 40.4 | 41.0 | $-1549.03 | -5.3% | $-549.03 | -2.4 | done | losing for real |
| momentum_60m_0.30pct | 3231 | 49.0 | 49.2 | $-1740.63 | -5.4% | $-740.63 | -3.0 | done | losing for real |
| trend_filter | 2300 | 48.5 | 50.4 | $-2048.35 | -8.9% | $-1048.35 | -4.4 | done | losing for real |
| momentum_15m_0.10pct | 3860 | 49.2 | 50.2 | $-2337.32 | -6.1% | $-1337.32 | -3.8 | done | losing for real |
| coinflip | 5668 | 49.9 | 49.9 | $-2497.47 | -4.4% | $-1497.47 | -3.3 | done | losing for real |
| momentum_5m_0.00pct | 5668 | 50.2 | 51.3 | $-3526.81 | -6.2% | $-2526.81 | -4.8 | done | losing for real |
| always_up | 5668 | 48.2 | 49.1 | $-3569.20 | -6.3% | $-2569.20 | -4.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 10524 | 47.9 | 48.6 | $-5943.42 |
| ETH | 11398 | 47.9 | 47.6 | $-6019.50 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
