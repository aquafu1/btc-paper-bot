# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 13, 7:15 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 237 windows, 6180 settled trades, 44 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 607 | 56.5 | 52.6 | $+251.13 | +4.1% | $1251.13 | +1.1 | done | can't tell from luck |
| reversal_60m_0.30pct | 483 | 54.2 | 52.3 | $+5.50 | +0.1% | $1005.50 | +0.0 | done | can't tell from luck |
| value_ev20 | 113 | 34.5 | 36.6 | $-110.27 | -9.8% | $889.73 | -0.8 | Sun 8:15 AM | too few trades (113/200) |
| value_ev10 | 302 | 38.1 | 40.8 | $-313.26 | -10.4% | $686.74 | -1.5 | done | can't tell from luck |
| value_ev5 | 440 | 39.8 | 42.5 | $-450.33 | -10.2% | $549.67 | -1.9 | done | can't tell from luck |
| trend_filter | 325 | 44.9 | 50.1 | $-458.44 | -14.1% | $541.56 | -2.6 | done | losing for real |
| momentum_60m_0.30pct | 483 | 45.8 | 49.8 | $-583.00 | -12.1% | $417.00 | -2.7 | done | losing for real |
| coinflip | 940 | 49.6 | 50.9 | $-627.40 | -6.7% | $372.60 | -2.1 | done | losing for real |
| momentum_5m_0.00pct | 940 | 49.6 | 51.4 | $-703.35 | -7.5% | $296.65 | -2.4 | done | losing for real |
| always_up | 940 | 47.4 | 50.5 | $-956.18 | -10.2% | $43.82 | -3.2 | done | losing for real |
| momentum_15m_0.10pct | 607 | 43.5 | 49.7 | $-960.37 | -15.8% | $39.63 | -4.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1381 | 46.3 | 49.7 | $-1438.04 |
| ETH | 1540 | 46.6 | 49.0 | $-1537.22 |
| SOL | 1597 | 48.2 | 49.4 | $-1215.96 |
| XRP | 1662 | 49.0 | 49.2 | $-714.74 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
