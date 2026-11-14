# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 13, 6:35 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 282 windows, 7462 settled trades, 44 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 736 | 54.3 | 51.8 | $+34.70 | +0.5% | $1034.70 | +0.1 | done | can't tell from luck |
| value_ev20 | 139 | 35.3 | 36.4 | $-119.35 | -8.6% | $880.65 | -0.8 | Sun 3:45 AM | too few trades (139/200) |
| reversal_60m_0.30pct | 599 | 52.4 | 51.8 | $-196.12 | -3.3% | $803.88 | -0.8 | done | can't tell from luck |
| value_ev10 | 363 | 38.0 | 40.5 | $-373.02 | -10.3% | $626.98 | -1.7 | done | can't tell from luck |
| trend_filter | 397 | 46.6 | 50.5 | $-489.72 | -12.3% | $510.28 | -2.5 | done | losing for real |
| value_ev5 | 530 | 39.8 | 42.2 | $-526.88 | -9.9% | $473.12 | -2.0 | done | losing for real |
| momentum_60m_0.30pct | 599 | 47.6 | 49.8 | $-558.98 | -9.3% | $441.02 | -2.3 | done | losing for real |
| coinflip | 1121 | 50.1 | 50.9 | $-639.66 | -5.7% | $360.34 | -2.0 | done | can't tell from luck |
| momentum_5m_0.00pct | 1121 | 49.6 | 51.5 | $-881.17 | -7.9% | $118.83 | -2.7 | done | losing for real |
| momentum_15m_0.10pct | 736 | 45.7 | 49.9 | $-920.59 | -12.5% | $79.41 | -3.4 | done | losing for real |
| always_up | 1121 | 47.5 | 50.3 | $-1079.23 | -9.6% | $-79.23 | -3.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1670 | 46.7 | 49.4 | $-1625.61 |
| ETH | 1862 | 47.2 | 48.8 | $-1701.07 |
| SOL | 1934 | 48.3 | 49.3 | $-1491.78 |
| XRP | 1996 | 48.9 | 49.1 | $-931.57 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
