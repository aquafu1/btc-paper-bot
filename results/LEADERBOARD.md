# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 12, 10:50 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 203 windows, 5263 settled trades, 51 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 516 | 57.6 | 52.8 | $+297.19 | +5.8% | $1297.19 | +1.4 | done | can't tell from luck |
| reversal_60m_0.30pct | 397 | 56.4 | 52.9 | $+123.29 | +3.1% | $1123.29 | +0.7 | done | can't tell from luck |
| value_ev20 | 100 | 31.0 | 37.1 | $-224.01 | -22.4% | $775.99 | -1.9 | Sun 6:15 AM | too few trades (100/200) |
| momentum_5m_0.00pct | 805 | 51.2 | 51.4 | $-371.89 | -4.6% | $628.11 | -1.4 | done | can't tell from luck |
| trend_filter | 269 | 43.9 | 49.6 | $-407.35 | -15.1% | $592.65 | -2.5 | done | losing for real |
| coinflip | 805 | 50.6 | 51.0 | $-447.09 | -5.6% | $552.91 | -1.6 | done | can't tell from luck |
| value_ev10 | 265 | 35.5 | 41.0 | $-479.46 | -18.1% | $520.54 | -2.6 | done | losing for real |
| value_ev5 | 388 | 37.9 | 42.7 | $-610.98 | -15.7% | $389.02 | -2.8 | done | losing for real |
| momentum_60m_0.30pct | 397 | 43.6 | 49.4 | $-628.89 | -15.8% | $371.11 | -3.2 | done | losing for real |
| momentum_15m_0.10pct | 516 | 42.4 | 49.6 | $-930.39 | -18.0% | $69.61 | -4.2 | done | losing for real |
| always_up | 805 | 45.2 | 50.3 | $-1185.12 | -14.7% | $-185.12 | -4.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1163 | 45.9 | 49.6 | $-1300.72 |
| ETH | 1310 | 46.3 | 48.9 | $-1422.43 |
| SOL | 1366 | 47.4 | 49.3 | $-1307.90 |
| XRP | 1424 | 49.0 | 49.3 | $-833.65 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
