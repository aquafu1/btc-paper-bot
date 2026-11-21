# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 21, 7:30 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1006 windows, 27984 settled trades, 66 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 518 | 34.2 | 35.0 | $-312.56 | -6.0% | $687.44 | -1.0 | done | can't tell from luck |
| reversal_15m_0.10pct | 2851 | 51.1 | 50.4 | $-835.32 | -2.9% | $164.68 | -1.6 | done | can't tell from luck |
| value_ev10 | 1282 | 37.4 | 39.1 | $-934.13 | -7.3% | $65.87 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 2407 | 50.0 | 49.7 | $-988.79 | -4.1% | $11.21 | -2.0 | done | losing for real |
| trend_filter | 1676 | 49.6 | 50.8 | $-1205.22 | -7.2% | $-205.22 | -3.0 | done | losing for real |
| value_ev5 | 1944 | 39.6 | 41.0 | $-1285.86 | -6.6% | $-285.86 | -2.5 | done | losing for real |
| coinflip | 4016 | 50.4 | 50.3 | $-1673.51 | -4.2% | $-673.51 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 2407 | 50.0 | 51.0 | $-1682.52 | -7.0% | $-682.52 | -3.5 | done | losing for real |
| momentum_15m_0.10pct | 2851 | 48.9 | 50.3 | $-1961.45 | -6.9% | $-961.45 | -3.7 | done | losing for real |
| momentum_5m_0.00pct | 4016 | 50.7 | 51.5 | $-2256.73 | -5.6% | $-1256.73 | -3.7 | done | losing for real |
| always_up | 4016 | 47.1 | 49.5 | $-3724.15 | -9.3% | $-2724.15 | -5.9 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6380 | 48.2 | 49.0 | $-3597.53 |
| ETH | 6950 | 48.0 | 48.5 | $-4472.60 |
| SOL | 7315 | 48.2 | 48.6 | $-4125.28 |
| XRP | 7339 | 48.1 | 48.4 | $-4664.82 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
