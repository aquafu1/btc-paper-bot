# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 13, 12:50 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 211 windows, 5487 settled trades, 60 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 541 | 57.1 | 52.7 | $+287.21 | +5.3% | $1287.21 | +1.3 | done | can't tell from luck |
| reversal_60m_0.30pct | 421 | 55.8 | 52.7 | $+123.79 | +2.9% | $1123.79 | +0.6 | done | can't tell from luck |
| value_ev20 | 104 | 33.7 | 36.9 | $-137.53 | -13.2% | $862.47 | -1.1 | Sun 5:30 AM | too few trades (104/200) |
| value_ev10 | 271 | 36.9 | 40.8 | $-360.93 | -13.3% | $639.07 | -1.9 | done | can't tell from luck |
| trend_filter | 284 | 43.7 | 49.9 | $-450.83 | -15.9% | $549.17 | -2.7 | done | losing for real |
| coinflip | 836 | 50.1 | 51.0 | $-488.82 | -5.8% | $511.18 | -1.7 | done | can't tell from luck |
| value_ev5 | 396 | 38.9 | 42.5 | $-491.97 | -12.4% | $508.03 | -2.2 | done | losing for real |
| momentum_5m_0.00pct | 836 | 50.4 | 51.5 | $-512.28 | -6.1% | $487.72 | -1.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 421 | 44.2 | 49.5 | $-605.83 | -14.4% | $394.17 | -3.0 | done | losing for real |
| momentum_15m_0.10pct | 541 | 42.9 | 49.6 | $-918.11 | -17.0% | $81.89 | -4.0 | done | losing for real |
| always_up | 836 | 46.1 | 50.2 | $-1027.35 | -12.3% | $-27.35 | -3.6 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1219 | 45.9 | 49.7 | $-1302.79 |
| ETH | 1370 | 46.4 | 48.8 | $-1310.40 |
| SOL | 1414 | 47.5 | 49.3 | $-1288.38 |
| XRP | 1484 | 49.3 | 49.2 | $-681.09 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
