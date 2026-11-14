# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 13, 6:20 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 281 windows, 7422 settled trades, 62 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 733 | 54.6 | 52.1 | $+64.70 | +0.9% | $1064.70 | +0.3 | done | can't tell from luck |
| value_ev20 | 136 | 36.0 | 36.9 | $-89.35 | -6.6% | $910.65 | -0.6 | Sun 5:45 AM | too few trades (136/200) |
| reversal_60m_0.30pct | 595 | 52.8 | 52.2 | $-156.12 | -2.6% | $843.88 | -0.7 | done | can't tell from luck |
| value_ev10 | 359 | 38.4 | 40.8 | $-333.02 | -9.3% | $666.98 | -1.5 | done | can't tell from luck |
| value_ev5 | 526 | 40.1 | 42.4 | $-486.88 | -9.3% | $513.12 | -1.9 | done | can't tell from luck |
| trend_filter | 394 | 46.2 | 50.3 | $-496.54 | -12.6% | $503.46 | -2.6 | done | losing for real |
| momentum_60m_0.30pct | 595 | 47.2 | 49.7 | $-570.58 | -9.6% | $429.42 | -2.4 | done | losing for real |
| coinflip | 1117 | 50.1 | 50.9 | $-623.70 | -5.6% | $376.30 | -1.9 | done | can't tell from luck |
| momentum_5m_0.00pct | 1117 | 49.5 | 51.5 | $-877.99 | -7.9% | $122.01 | -2.7 | done | losing for real |
| momentum_15m_0.10pct | 733 | 45.4 | 49.8 | $-927.41 | -12.7% | $72.59 | -3.5 | done | losing for real |
| always_up | 1117 | 47.4 | 50.2 | $-1090.84 | -9.8% | $-90.84 | -3.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1663 | 46.8 | 49.5 | $-1585.19 |
| ETH | 1851 | 47.1 | 49.0 | $-1660.48 |
| SOL | 1923 | 48.3 | 49.4 | $-1456.62 |
| XRP | 1985 | 49.0 | 49.1 | $-885.46 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
