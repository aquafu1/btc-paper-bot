# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 13, 6:45 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 283 windows, 7484 settled trades, 54 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 738 | 54.3 | 51.8 | $+37.54 | +0.5% | $1037.54 | +0.1 | done | can't tell from luck |
| value_ev20 | 139 | 35.3 | 36.4 | $-119.35 | -8.6% | $880.65 | -0.8 | Sun 3:45 AM | too few trades (139/200) |
| reversal_60m_0.30pct | 602 | 52.3 | 51.8 | $-203.28 | -3.4% | $796.72 | -0.9 | done | can't tell from luck |
| value_ev10 | 364 | 38.2 | 40.5 | $-360.86 | -9.9% | $639.14 | -1.6 | done | can't tell from luck |
| trend_filter | 397 | 46.6 | 50.5 | $-489.72 | -12.3% | $510.28 | -2.5 | done | losing for real |
| value_ev5 | 532 | 40.0 | 42.2 | $-501.89 | -9.4% | $498.11 | -1.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 602 | 47.7 | 49.8 | $-550.88 | -9.2% | $449.12 | -2.3 | done | losing for real |
| coinflip | 1124 | 50.0 | 50.9 | $-669.66 | -6.0% | $330.34 | -2.1 | done | losing for real |
| momentum_5m_0.00pct | 1124 | 49.6 | 51.5 | $-888.33 | -7.9% | $111.67 | -2.8 | done | losing for real |
| momentum_15m_0.10pct | 738 | 45.7 | 49.9 | $-924.64 | -12.5% | $75.36 | -3.5 | done | losing for real |
| always_up | 1124 | 47.6 | 50.3 | $-1071.14 | -9.5% | $-71.14 | -3.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1670 | 46.7 | 49.4 | $-1625.61 |
| ETH | 1869 | 47.1 | 48.8 | $-1723.23 |
| SOL | 1942 | 48.3 | 49.3 | $-1480.41 |
| XRP | 2003 | 49.0 | 49.1 | $-912.96 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
