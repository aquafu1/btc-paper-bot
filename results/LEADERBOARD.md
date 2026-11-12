# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 12, 2:35 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 180 windows, 4601 settled trades, 39 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 447 | 57.9 | 52.4 | $+339.41 | +7.6% | $1339.41 | +1.7 | done | can't tell from luck |
| reversal_60m_0.30pct | 339 | 59.9 | 53.1 | $+331.62 | +9.8% | $1331.62 | +1.9 | done | can't tell from luck |
| value_ev20 | 87 | 33.3 | 36.6 | $-143.13 | -16.5% | $856.87 | -1.3 | Sun 3:30 AM | too few trades (87/200) |
| momentum_5m_0.00pct | 712 | 51.5 | 51.3 | $-262.17 | -3.7% | $737.83 | -1.0 | done | can't tell from luck |
| value_ev10 | 233 | 36.5 | 40.6 | $-349.22 | -15.0% | $650.78 | -2.0 | done | losing for real |
| coinflip | 712 | 50.3 | 50.9 | $-403.45 | -5.7% | $596.55 | -1.6 | done | can't tell from luck |
| trend_filter | 230 | 41.3 | 49.3 | $-437.61 | -19.0% | $562.39 | -2.9 | done | losing for real |
| value_ev5 | 343 | 38.2 | 42.4 | $-486.08 | -14.2% | $513.92 | -2.4 | done | losing for real |
| momentum_60m_0.30pct | 339 | 40.1 | 48.9 | $-724.72 | -21.4% | $275.28 | -4.0 | done | losing for real |
| momentum_15m_0.10pct | 447 | 42.1 | 49.7 | $-829.53 | -18.6% | $170.47 | -4.0 | done | losing for real |
| always_up | 712 | 46.3 | 49.9 | $-832.60 | -11.7% | $167.40 | -3.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1003 | 45.7 | 49.4 | $-1053.27 |
| ETH | 1150 | 45.8 | 48.7 | $-1316.03 |
| SOL | 1196 | 47.6 | 49.0 | $-1077.43 |
| XRP | 1252 | 50.1 | 49.1 | $-350.76 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
