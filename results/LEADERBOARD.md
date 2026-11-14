# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 14, 2:50 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 363 windows, 9807 settled trades, 39 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 189 | 38.1 | 36.4 | $+15.78 | +0.8% | $1015.78 | +0.1 | Sat 8:30 PM | too few trades (189/200) |
| value_ev10 | 476 | 41.2 | 40.3 | $-53.22 | -1.1% | $946.78 | -0.2 | done | can't tell from luck |
| value_ev5 | 705 | 42.4 | 42.0 | $-179.55 | -2.5% | $820.45 | -0.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 972 | 51.9 | 52.1 | $-432.20 | -4.4% | $567.80 | -1.5 | done | can't tell from luck |
| momentum_60m_0.30pct | 805 | 49.1 | 49.8 | $-468.91 | -5.8% | $531.09 | -1.7 | done | can't tell from luck |
| trend_filter | 542 | 48.3 | 50.6 | $-475.35 | -8.8% | $524.65 | -2.1 | done | losing for real |
| reversal_60m_0.30pct | 805 | 50.9 | 52.0 | $-477.12 | -5.9% | $522.88 | -1.8 | done | can't tell from luck |
| momentum_15m_0.10pct | 972 | 48.1 | 49.6 | $-646.35 | -6.6% | $353.65 | -2.1 | done | losing for real |
| coinflip | 1447 | 50.1 | 50.8 | $-724.28 | -5.0% | $275.72 | -1.9 | done | can't tell from luck |
| momentum_5m_0.00pct | 1447 | 49.4 | 51.6 | $-1106.90 | -7.6% | $-106.90 | -3.0 | done | losing for real |
| always_up | 1447 | 45.9 | 50.7 | $-1877.41 | -13.0% | $-877.41 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2201 | 47.3 | 49.3 | $-1744.19 |
| ETH | 2468 | 47.7 | 48.8 | $-1710.76 |
| SOL | 2538 | 48.1 | 49.4 | $-1765.46 |
| XRP | 2600 | 48.9 | 49.1 | $-1205.10 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
