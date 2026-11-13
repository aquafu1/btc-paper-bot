# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 12, 11:45 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 207 windows, 5376 settled trades, 54 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 528 | 57.4 | 52.8 | $+285.69 | +5.4% | $1285.69 | +1.3 | done | can't tell from luck |
| reversal_60m_0.30pct | 409 | 56.0 | 52.7 | $+125.05 | +3.1% | $1125.05 | +0.7 | done | can't tell from luck |
| value_ev20 | 104 | 33.7 | 36.9 | $-137.53 | -13.2% | $862.47 | -1.1 | Sun 3:30 AM | too few trades (104/200) |
| value_ev10 | 269 | 36.4 | 40.8 | $-392.98 | -14.6% | $607.02 | -2.1 | done | losing for real |
| trend_filter | 277 | 43.7 | 49.8 | $-431.14 | -15.6% | $568.86 | -2.6 | done | losing for real |
| coinflip | 820 | 50.5 | 51.0 | $-434.37 | -5.3% | $565.63 | -1.6 | done | can't tell from luck |
| momentum_5m_0.00pct | 820 | 50.7 | 51.4 | $-436.40 | -5.3% | $563.60 | -1.6 | done | can't tell from luck |
| value_ev5 | 392 | 38.5 | 42.5 | $-524.50 | -13.4% | $475.50 | -2.4 | done | losing for real |
| momentum_60m_0.30pct | 409 | 44.0 | 49.5 | $-613.18 | -15.0% | $386.82 | -3.1 | done | losing for real |
| momentum_15m_0.10pct | 528 | 42.6 | 49.5 | $-917.00 | -17.4% | $83.00 | -4.1 | done | losing for real |
| always_up | 820 | 45.5 | 50.2 | $-1121.41 | -13.7% | $-121.41 | -4.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1192 | 46.0 | 49.6 | $-1248.17 |
| ETH | 1341 | 46.3 | 48.8 | $-1335.15 |
| SOL | 1390 | 47.6 | 49.2 | $-1267.45 |
| XRP | 1453 | 49.2 | 49.2 | $-747.00 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
