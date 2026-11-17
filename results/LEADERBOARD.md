# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 16, 8:50 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 579 windows, 16034 settled trades, 48 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1361 | 51.1 | 49.6 | $-278.07 | -2.0% | $721.93 | -0.8 | done | can't tell from luck |
| value_ev20 | 314 | 33.1 | 35.2 | $-354.56 | -11.3% | $645.44 | -1.5 | done | can't tell from luck |
| trend_filter | 929 | 50.4 | 51.0 | $-524.64 | -5.6% | $475.36 | -1.8 | done | can't tell from luck |
| value_ev10 | 754 | 37.4 | 39.4 | $-727.94 | -9.7% | $272.06 | -2.2 | done | losing for real |
| reversal_15m_0.10pct | 1631 | 51.0 | 51.0 | $-766.39 | -4.7% | $233.61 | -1.9 | done | can't tell from luck |
| value_ev5 | 1126 | 39.9 | 41.3 | $-873.91 | -7.8% | $126.09 | -2.2 | done | losing for real |
| momentum_15m_0.10pct | 1631 | 49.0 | 49.9 | $-996.84 | -6.1% | $3.16 | -2.5 | done | losing for real |
| coinflip | 2309 | 49.9 | 50.5 | $-1238.28 | -5.4% | $-238.28 | -2.6 | done | losing for real |
| reversal_60m_0.30pct | 1361 | 48.9 | 51.3 | $-1292.87 | -9.5% | $-292.87 | -3.6 | done | losing for real |
| momentum_5m_0.00pct | 2309 | 50.3 | 51.9 | $-1612.83 | -7.0% | $-612.83 | -3.5 | done | losing for real |
| always_up | 2309 | 46.9 | 49.8 | $-2347.21 | -10.2% | $-1347.21 | -4.9 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3641 | 47.7 | 49.2 | $-2744.97 |
| ETH | 3997 | 47.9 | 48.6 | $-2783.04 |
| SOL | 4172 | 47.7 | 48.8 | $-3165.01 |
| XRP | 4224 | 48.5 | 48.6 | $-2320.52 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
