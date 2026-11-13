# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 13, 7:45 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 239 windows, 6224 settled trades, 59 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 612 | 56.5 | 52.5 | $+271.82 | +4.4% | $1271.82 | +1.2 | done | can't tell from luck |
| reversal_60m_0.30pct | 487 | 54.2 | 52.3 | $+6.10 | +0.1% | $1006.10 | +0.0 | done | can't tell from luck |
| value_ev20 | 113 | 34.5 | 36.6 | $-110.27 | -9.8% | $889.73 | -0.8 | Sun 9:00 AM | too few trades (113/200) |
| value_ev10 | 302 | 38.1 | 40.8 | $-313.26 | -10.4% | $686.74 | -1.5 | done | can't tell from luck |
| value_ev5 | 440 | 39.8 | 42.5 | $-450.33 | -10.2% | $549.67 | -1.9 | done | can't tell from luck |
| trend_filter | 327 | 45.0 | 50.2 | $-463.21 | -14.2% | $536.79 | -2.6 | done | losing for real |
| momentum_60m_0.30pct | 487 | 45.8 | 49.9 | $-587.93 | -12.1% | $412.07 | -2.7 | done | losing for real |
| coinflip | 948 | 49.5 | 51.0 | $-656.92 | -6.9% | $343.08 | -2.2 | done | losing for real |
| momentum_5m_0.00pct | 948 | 49.6 | 51.5 | $-713.19 | -7.5% | $286.81 | -2.4 | done | losing for real |
| always_up | 948 | 47.6 | 50.4 | $-926.51 | -9.8% | $73.49 | -3.1 | done | losing for real |
| momentum_15m_0.10pct | 612 | 43.5 | 49.8 | $-979.19 | -16.0% | $20.81 | -4.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1391 | 46.4 | 49.7 | $-1427.33 |
| ETH | 1553 | 46.6 | 49.1 | $-1556.63 |
| SOL | 1605 | 48.3 | 49.4 | $-1190.19 |
| XRP | 1675 | 49.0 | 49.2 | $-748.74 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
