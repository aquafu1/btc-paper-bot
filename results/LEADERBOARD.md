# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 12, 10:00 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 162 windows, 4143 settled trades, 45 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 305 | 59.7 | 53.1 | $+304.61 | +10.0% | $1304.61 | +1.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 400 | 57.2 | 52.5 | $+253.96 | +6.3% | $1253.96 | +1.3 | done | can't tell from luck |
| value_ev20 | 78 | 35.9 | 37.3 | $-81.99 | -10.5% | $918.01 | -0.8 | Sun 4:15 AM | too few trades (78/200) |
| momentum_5m_0.00pct | 640 | 51.6 | 51.1 | $-214.03 | -3.3% | $785.97 | -0.9 | done | can't tell from luck |
| value_ev10 | 211 | 38.4 | 40.9 | $-232.16 | -11.0% | $767.84 | -1.4 | done | can't tell from luck |
| coinflip | 640 | 50.6 | 50.9 | $-313.85 | -4.9% | $686.15 | -1.3 | done | can't tell from luck |
| value_ev5 | 310 | 39.4 | 42.6 | $-365.80 | -11.8% | $634.20 | -1.9 | done | can't tell from luck |
| trend_filter | 214 | 40.7 | 48.9 | $-423.00 | -19.8% | $577.00 | -2.9 | done | losing for real |
| momentum_60m_0.30pct | 305 | 40.3 | 49.1 | $-625.52 | -20.5% | $374.48 | -3.6 | done | losing for real |
| momentum_15m_0.10pct | 400 | 42.8 | 49.7 | $-681.88 | -17.0% | $318.12 | -3.5 | done | losing for real |
| always_up | 640 | 45.8 | 50.2 | $-838.31 | -13.1% | $161.69 | -3.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 900 | 46.1 | 49.5 | $-815.80 |
| ETH | 1033 | 45.6 | 48.9 | $-1178.58 |
| SOL | 1087 | 47.7 | 49.0 | $-918.83 |
| XRP | 1123 | 50.3 | 49.1 | $-304.75 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
