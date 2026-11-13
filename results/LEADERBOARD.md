# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 13, 8:45 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 243 windows, 6345 settled trades, 53 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 626 | 56.2 | 52.3 | $+234.43 | +3.7% | $1234.43 | +1.0 | done | can't tell from luck |
| reversal_60m_0.30pct | 499 | 54.9 | 52.4 | $+60.06 | +1.2% | $1060.06 | +0.3 | done | can't tell from luck |
| value_ev20 | 114 | 34.2 | 36.7 | $-120.27 | -10.6% | $879.73 | -0.9 | Sun 9:45 AM | too few trades (114/200) |
| value_ev10 | 308 | 37.3 | 40.9 | $-373.26 | -12.1% | $626.74 | -1.8 | done | can't tell from luck |
| trend_filter | 332 | 44.6 | 50.3 | $-500.59 | -15.1% | $499.41 | -2.8 | done | losing for real |
| value_ev5 | 449 | 39.2 | 42.5 | $-520.65 | -11.6% | $479.35 | -2.2 | done | losing for real |
| coinflip | 964 | 49.6 | 50.9 | $-669.14 | -6.9% | $330.86 | -2.2 | done | losing for real |
| momentum_60m_0.30pct | 499 | 45.1 | 49.8 | $-673.59 | -13.5% | $326.41 | -3.1 | done | losing for real |
| momentum_5m_0.00pct | 964 | 49.8 | 51.6 | $-719.08 | -7.5% | $280.92 | -2.4 | done | losing for real |
| momentum_15m_0.10pct | 626 | 43.8 | 49.9 | $-988.87 | -15.8% | $11.13 | -4.0 | done | losing for real |
| always_up | 964 | 47.4 | 50.5 | $-1003.51 | -10.4% | $-3.51 | -3.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1418 | 46.4 | 49.8 | $-1484.10 |
| ETH | 1582 | 46.5 | 49.0 | $-1649.16 |
| SOL | 1638 | 48.2 | 49.4 | $-1298.05 |
| XRP | 1707 | 48.9 | 49.2 | $-843.16 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
