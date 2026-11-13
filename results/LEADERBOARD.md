# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 12, 11:00 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 204 windows, 5282 settled trades, 66 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 518 | 57.5 | 52.8 | $+298.11 | +5.8% | $1298.11 | +1.4 | done | can't tell from luck |
| reversal_60m_0.30pct | 400 | 56.0 | 52.9 | $+93.29 | +2.3% | $1093.29 | +0.5 | done | can't tell from luck |
| value_ev20 | 100 | 31.0 | 37.1 | $-224.01 | -22.4% | $775.99 | -1.9 | Sun 6:15 AM | too few trades (100/200) |
| momentum_5m_0.00pct | 808 | 51.0 | 51.4 | $-401.89 | -5.0% | $598.11 | -1.5 | done | can't tell from luck |
| trend_filter | 269 | 43.9 | 49.6 | $-407.35 | -15.1% | $592.65 | -2.5 | done | losing for real |
| coinflip | 808 | 50.5 | 51.0 | $-455.72 | -5.6% | $544.28 | -1.7 | done | can't tell from luck |
| value_ev10 | 265 | 35.5 | 41.0 | $-479.46 | -18.1% | $520.54 | -2.6 | done | losing for real |
| momentum_60m_0.30pct | 400 | 44.0 | 49.4 | $-597.64 | -14.9% | $402.36 | -3.0 | done | losing for real |
| value_ev5 | 388 | 37.9 | 42.7 | $-610.98 | -15.7% | $389.02 | -2.8 | done | losing for real |
| momentum_15m_0.10pct | 518 | 42.5 | 49.6 | $-929.03 | -17.9% | $70.97 | -4.2 | done | losing for real |
| always_up | 808 | 45.0 | 50.3 | $-1215.12 | -15.0% | $-215.12 | -4.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1170 | 45.8 | 49.6 | $-1328.89 |
| ETH | 1317 | 46.2 | 48.9 | $-1428.33 |
| SOL | 1366 | 47.4 | 49.3 | $-1307.90 |
| XRP | 1429 | 48.9 | 49.3 | $-864.69 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
