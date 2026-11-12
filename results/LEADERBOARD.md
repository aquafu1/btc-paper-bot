# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 12, 2:15 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 179 windows, 4576 settled trades, 45 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 444 | 57.9 | 52.3 | $+335.86 | +7.6% | $1335.86 | +1.7 | done | can't tell from luck |
| reversal_60m_0.30pct | 338 | 59.8 | 53.1 | $+323.77 | +9.6% | $1323.77 | +1.9 | done | can't tell from luck |
| value_ev20 | 87 | 33.3 | 36.6 | $-143.13 | -16.5% | $856.87 | -1.3 | Sun 2:45 AM | too few trades (87/200) |
| momentum_5m_0.00pct | 708 | 51.4 | 51.3 | $-280.58 | -4.0% | $719.42 | -1.1 | done | can't tell from luck |
| value_ev10 | 231 | 36.4 | 40.5 | $-352.61 | -15.3% | $647.39 | -2.0 | done | losing for real |
| coinflip | 708 | 50.3 | 50.9 | $-404.68 | -5.7% | $595.32 | -1.6 | done | can't tell from luck |
| trend_filter | 230 | 41.3 | 49.3 | $-437.61 | -19.0% | $562.39 | -2.9 | done | losing for real |
| value_ev5 | 340 | 38.2 | 42.4 | $-479.47 | -14.1% | $520.53 | -2.3 | done | losing for real |
| momentum_60m_0.30pct | 338 | 40.2 | 48.9 | $-714.72 | -21.1% | $285.28 | -3.9 | done | losing for real |
| always_up | 708 | 46.5 | 50.0 | $-815.98 | -11.5% | $184.02 | -3.1 | done | losing for real |
| momentum_15m_0.10pct | 444 | 42.1 | 49.8 | $-822.91 | -18.5% | $177.09 | -4.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 997 | 45.8 | 49.4 | $-1008.97 |
| ETH | 1143 | 45.6 | 48.8 | $-1386.33 |
| SOL | 1191 | 47.7 | 49.0 | $-1044.61 |
| XRP | 1245 | 50.0 | 49.0 | $-352.14 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
