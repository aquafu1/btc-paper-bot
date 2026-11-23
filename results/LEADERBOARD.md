# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 23, 4:35 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1234 windows, 33667 settled trades, 428 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 660 | 34.4 | 35.3 | $-474.16 | -7.2% | $525.84 | -1.4 | done | can't tell from luck |
| value_ev10 | 1611 | 38.7 | 39.2 | $-770.67 | -4.8% | $229.33 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 3376 | 50.9 | 50.3 | $-1039.63 | -3.1% | $-39.63 | -1.8 | done | can't tell from luck |
| value_ev5 | 2434 | 40.5 | 41.1 | $-1217.46 | -5.0% | $-217.46 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 2823 | 49.5 | 49.4 | $-1291.06 | -4.6% | $-291.06 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 2823 | 50.5 | 51.1 | $-1651.52 | -5.9% | $-651.52 | -3.2 | done | losing for real |
| trend_filter | 1990 | 48.7 | 50.4 | $-1691.43 | -8.5% | $-691.43 | -3.9 | done | losing for real |
| momentum_15m_0.10pct | 3376 | 49.1 | 50.2 | $-2115.97 | -6.3% | $-1115.97 | -3.7 | done | losing for real |
| coinflip | 4858 | 50.0 | 50.1 | $-2201.00 | -4.5% | $-1201.00 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 4858 | 50.2 | 51.4 | $-2989.47 | -6.2% | $-1989.47 | -4.4 | done | losing for real |
| always_up | 4858 | 47.8 | 49.3 | $-3555.83 | -7.3% | $-2555.83 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7865 | 48.0 | 48.9 | $-4483.26 |
| ETH | 8492 | 48.1 | 48.3 | $-4930.71 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
