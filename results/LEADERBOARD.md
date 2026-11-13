# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 12, 8:05 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 192 windows, 4925 settled trades, 38 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 481 | 58.4 | 52.6 | $+379.32 | +7.9% | $1379.32 | +1.8 | done | can't tell from luck |
| reversal_60m_0.30pct | 358 | 59.8 | 53.1 | $+337.19 | +9.4% | $1337.19 | +1.9 | done | can't tell from luck |
| value_ev20 | 95 | 31.6 | 37.0 | $-198.58 | -20.9% | $801.42 | -1.7 | Sun 6:30 AM | too few trades (95/200) |
| momentum_5m_0.00pct | 762 | 51.7 | 51.3 | $-268.37 | -3.5% | $731.63 | -1.0 | done | can't tell from luck |
| value_ev10 | 253 | 36.0 | 40.9 | $-420.34 | -16.6% | $579.66 | -2.3 | done | losing for real |
| coinflip | 762 | 50.4 | 51.0 | $-434.41 | -5.7% | $565.59 | -1.6 | done | can't tell from luck |
| trend_filter | 243 | 41.6 | 49.4 | $-457.37 | -18.8% | $542.63 | -2.9 | done | losing for real |
| value_ev5 | 370 | 38.4 | 42.6 | $-527.45 | -14.3% | $472.55 | -2.5 | done | losing for real |
| momentum_60m_0.30pct | 358 | 40.2 | 49.0 | $-772.17 | -21.6% | $227.83 | -4.2 | done | losing for real |
| momentum_15m_0.10pct | 481 | 41.6 | 49.6 | $-940.38 | -19.6% | $59.62 | -4.4 | done | losing for real |
| always_up | 762 | 46.2 | 50.2 | $-962.65 | -12.6% | $37.35 | -3.6 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1078 | 45.8 | 49.5 | $-1154.80 |
| ETH | 1221 | 45.9 | 48.8 | $-1396.41 |
| SOL | 1279 | 47.8 | 49.1 | $-1090.44 |
| XRP | 1347 | 49.5 | 49.2 | $-623.58 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
