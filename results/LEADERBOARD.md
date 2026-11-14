# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 13, 9:30 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 294 windows, 7802 settled trades, 66 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 772 | 54.0 | 51.9 | $-27.12 | -0.4% | $972.88 | -0.1 | done | can't tell from luck |
| value_ev20 | 146 | 35.6 | 36.4 | $-114.69 | -7.9% | $885.31 | -0.7 | Sun 2:15 AM | too few trades (146/200) |
| reversal_60m_0.30pct | 629 | 52.3 | 51.9 | $-232.25 | -3.7% | $767.75 | -1.0 | done | can't tell from luck |
| value_ev10 | 377 | 38.5 | 40.4 | $-343.14 | -9.1% | $656.86 | -1.5 | done | can't tell from luck |
| trend_filter | 420 | 46.4 | 50.1 | $-501.97 | -12.0% | $498.03 | -2.5 | done | losing for real |
| value_ev5 | 553 | 40.0 | 42.1 | $-521.67 | -9.4% | $478.33 | -2.0 | done | can't tell from luck |
| momentum_60m_0.30pct | 629 | 47.7 | 49.7 | $-561.80 | -8.9% | $438.20 | -2.3 | done | losing for real |
| coinflip | 1168 | 50.2 | 50.9 | $-657.39 | -5.6% | $342.61 | -2.0 | done | can't tell from luck |
| momentum_15m_0.10pct | 772 | 46.0 | 49.8 | $-902.44 | -11.7% | $97.56 | -3.3 | done | losing for real |
| momentum_5m_0.00pct | 1168 | 49.1 | 51.3 | $-969.38 | -8.3% | $30.62 | -2.9 | done | losing for real |
| always_up | 1168 | 47.4 | 50.3 | $-1157.78 | -9.9% | $-157.78 | -3.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1740 | 46.7 | 49.3 | $-1605.92 |
| ETH | 1949 | 47.3 | 48.7 | $-1717.63 |
| SOL | 2029 | 48.3 | 49.3 | $-1565.83 |
| XRP | 2084 | 48.7 | 49.0 | $-1100.26 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
