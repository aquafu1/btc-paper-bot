# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 12, 8:20 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 193 windows, 4940 settled trades, 57 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 483 | 58.6 | 52.6 | $+390.75 | +8.1% | $1390.75 | +1.9 | done | can't tell from luck |
| reversal_60m_0.30pct | 358 | 59.8 | 53.1 | $+337.19 | +9.4% | $1337.19 | +1.9 | done | can't tell from luck |
| value_ev20 | 95 | 31.6 | 37.0 | $-198.58 | -20.9% | $801.42 | -1.7 | Sun 7:00 AM | too few trades (95/200) |
| momentum_5m_0.00pct | 765 | 51.5 | 51.3 | $-298.37 | -3.9% | $701.63 | -1.1 | done | can't tell from luck |
| coinflip | 765 | 50.5 | 51.0 | $-429.96 | -5.6% | $570.04 | -1.6 | done | can't tell from luck |
| value_ev10 | 254 | 35.8 | 40.8 | $-430.34 | -16.9% | $569.66 | -2.4 | done | losing for real |
| trend_filter | 243 | 41.6 | 49.4 | $-457.37 | -18.8% | $542.63 | -2.9 | done | losing for real |
| value_ev5 | 371 | 38.3 | 42.6 | $-537.45 | -14.5% | $462.55 | -2.5 | done | losing for real |
| momentum_60m_0.30pct | 358 | 40.2 | 49.0 | $-772.17 | -21.6% | $227.83 | -4.2 | done | losing for real |
| momentum_15m_0.10pct | 483 | 41.4 | 49.6 | $-960.38 | -19.9% | $39.62 | -4.5 | done | losing for real |
| always_up | 765 | 46.3 | 50.3 | $-961.22 | -12.6% | $38.78 | -3.6 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1088 | 45.7 | 49.5 | $-1206.09 |
| ETH | 1226 | 46.0 | 48.8 | $-1397.81 |
| SOL | 1279 | 47.8 | 49.1 | $-1090.44 |
| XRP | 1347 | 49.5 | 49.2 | $-623.58 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
