# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 20, 10:45 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 971 windows, 26924 settled trades, 65 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 496 | 34.7 | 34.8 | $-219.50 | -4.4% | $780.50 | -0.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 2749 | 51.3 | 50.5 | $-735.34 | -2.7% | $264.66 | -1.4 | done | can't tell from luck |
| value_ev10 | 1229 | 37.9 | 39.1 | $-744.80 | -6.1% | $255.20 | -1.7 | done | can't tell from luck |
| momentum_60m_0.30pct | 2300 | 50.4 | 49.8 | $-800.93 | -3.5% | $199.07 | -1.7 | done | can't tell from luck |
| trend_filter | 1608 | 50.0 | 50.9 | $-1067.85 | -6.6% | $-67.85 | -2.7 | done | losing for real |
| value_ev5 | 1865 | 39.8 | 41.0 | $-1098.05 | -5.9% | $-98.05 | -2.1 | done | losing for real |
| reversal_60m_0.30pct | 2300 | 49.6 | 50.9 | $-1727.28 | -7.5% | $-727.28 | -3.7 | done | losing for real |
| coinflip | 3876 | 50.2 | 50.3 | $-1783.13 | -4.6% | $-783.13 | -2.9 | done | losing for real |
| momentum_15m_0.10pct | 2749 | 48.7 | 50.3 | $-1951.16 | -7.1% | $-951.16 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 3876 | 50.8 | 51.6 | $-2090.82 | -5.4% | $-1090.82 | -3.5 | done | losing for real |
| always_up | 3876 | 46.7 | 49.6 | $-3917.42 | -10.1% | $-2917.42 | -6.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6132 | 48.2 | 49.1 | $-3492.12 |
| ETH | 6691 | 48.0 | 48.5 | $-4277.48 |
| SOL | 7031 | 48.2 | 48.6 | $-3948.16 |
| XRP | 7070 | 48.1 | 48.4 | $-4418.52 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
