# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 13, 6:30 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 282 windows, 7455 settled trades, 51 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 736 | 54.3 | 51.8 | $+34.70 | +0.5% | $1034.70 | +0.1 | done | can't tell from luck |
| value_ev20 | 139 | 35.3 | 36.4 | $-119.35 | -8.6% | $880.65 | -0.8 | Sun 3:15 AM | too few trades (139/200) |
| reversal_60m_0.30pct | 598 | 52.5 | 51.8 | $-186.12 | -3.1% | $813.88 | -0.8 | done | can't tell from luck |
| value_ev10 | 362 | 38.1 | 40.5 | $-363.02 | -10.0% | $636.98 | -1.6 | done | can't tell from luck |
| trend_filter | 397 | 46.6 | 50.5 | $-489.72 | -12.3% | $510.28 | -2.5 | done | losing for real |
| value_ev5 | 529 | 39.9 | 42.2 | $-516.88 | -9.8% | $483.12 | -2.0 | done | can't tell from luck |
| momentum_60m_0.30pct | 598 | 47.5 | 49.8 | $-563.77 | -9.4% | $436.23 | -2.3 | done | losing for real |
| coinflip | 1120 | 50.2 | 50.9 | $-629.66 | -5.6% | $370.34 | -1.9 | done | can't tell from luck |
| momentum_5m_0.00pct | 1120 | 49.6 | 51.5 | $-871.17 | -7.8% | $128.83 | -2.7 | done | losing for real |
| momentum_15m_0.10pct | 736 | 45.7 | 49.9 | $-920.59 | -12.5% | $79.41 | -3.4 | done | losing for real |
| always_up | 1120 | 47.5 | 50.3 | $-1084.03 | -9.7% | $-84.03 | -3.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1663 | 46.8 | 49.5 | $-1585.19 |
| ETH | 1862 | 47.2 | 48.8 | $-1701.07 |
| SOL | 1934 | 48.3 | 49.3 | $-1491.78 |
| XRP | 1996 | 48.9 | 49.1 | $-931.57 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
