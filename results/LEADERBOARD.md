# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 19, 2:50 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 843 windows, 23209 settled trades, 52 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 428 | 33.4 | 34.9 | $-358.95 | -8.4% | $641.05 | -1.3 | done | can't tell from luck |
| value_ev10 | 1059 | 37.5 | 39.1 | $-818.18 | -7.7% | $181.82 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 1957 | 50.1 | 49.7 | $-838.44 | -4.3% | $161.56 | -1.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 2370 | 50.8 | 50.6 | $-917.28 | -3.9% | $82.72 | -1.9 | done | can't tell from luck |
| trend_filter | 1366 | 49.9 | 50.9 | $-944.14 | -6.9% | $55.86 | -2.6 | done | losing for real |
| value_ev5 | 1604 | 39.7 | 41.1 | $-1110.72 | -6.9% | $-110.72 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 1957 | 49.9 | 51.1 | $-1435.48 | -7.3% | $-435.48 | -3.3 | done | losing for real |
| momentum_15m_0.10pct | 2370 | 49.2 | 50.3 | $-1441.04 | -6.1% | $-441.04 | -3.0 | done | losing for real |
| coinflip | 3366 | 50.2 | 50.3 | $-1487.86 | -4.4% | $-487.86 | -2.6 | done | losing for real |
| momentum_5m_0.00pct | 3366 | 51.2 | 51.7 | $-1597.84 | -4.7% | $-597.84 | -2.8 | done | losing for real |
| always_up | 3366 | 47.0 | 49.6 | $-3207.34 | -9.5% | $-2207.34 | -5.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5287 | 48.1 | 49.1 | $-3172.83 |
| ETH | 5773 | 48.0 | 48.5 | $-4053.27 |
| SOL | 6058 | 48.2 | 48.6 | $-3612.26 |
| XRP | 6091 | 48.4 | 48.5 | $-3318.91 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
