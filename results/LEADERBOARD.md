# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 21, 11:05 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1020 windows, 28406 settled trades, 45 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 524 | 34.5 | 35.1 | $-292.61 | -5.6% | $707.39 | -1.0 | done | can't tell from luck |
| reversal_15m_0.10pct | 2897 | 51.2 | 50.5 | $-808.49 | -2.8% | $191.51 | -1.5 | done | can't tell from luck |
| value_ev10 | 1300 | 37.5 | 39.2 | $-969.33 | -7.5% | $30.67 | -2.2 | done | losing for real |
| momentum_60m_0.30pct | 2448 | 49.9 | 49.7 | $-1059.34 | -4.3% | $-59.34 | -2.1 | done | losing for real |
| trend_filter | 1703 | 49.7 | 50.8 | $-1184.18 | -7.0% | $-184.18 | -2.9 | done | losing for real |
| value_ev5 | 1973 | 39.4 | 41.0 | $-1388.88 | -7.0% | $-388.88 | -2.6 | done | losing for real |
| reversal_60m_0.30pct | 2448 | 50.1 | 51.0 | $-1634.97 | -6.7% | $-634.97 | -3.4 | done | losing for real |
| coinflip | 4072 | 50.5 | 50.4 | $-1648.04 | -4.0% | $-648.04 | -2.6 | done | losing for real |
| momentum_15m_0.10pct | 2897 | 48.8 | 50.3 | $-2010.24 | -6.9% | $-1010.24 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 4072 | 50.8 | 51.5 | $-2178.04 | -5.3% | $-1178.04 | -3.5 | done | losing for real |
| always_up | 4072 | 47.3 | 49.5 | $-3627.31 | -8.9% | $-2627.31 | -5.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6477 | 48.3 | 49.1 | $-3487.86 |
| ETH | 7059 | 48.1 | 48.5 | $-4390.67 |
| SOL | 7417 | 48.2 | 48.6 | $-4256.54 |
| XRP | 7453 | 48.1 | 48.4 | $-4666.37 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
