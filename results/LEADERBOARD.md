# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 13, 9:20 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 293 windows, 7776 settled trades, 63 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 768 | 53.8 | 51.9 | $-65.89 | -0.9% | $934.11 | -0.3 | done | can't tell from luck |
| value_ev20 | 146 | 35.6 | 36.4 | $-114.69 | -7.9% | $885.31 | -0.7 | Sun 2:00 AM | too few trades (146/200) |
| reversal_60m_0.30pct | 626 | 52.6 | 51.9 | $-202.25 | -3.2% | $797.75 | -0.8 | done | can't tell from luck |
| value_ev10 | 377 | 38.5 | 40.4 | $-343.14 | -9.1% | $656.86 | -1.5 | done | can't tell from luck |
| trend_filter | 420 | 46.4 | 50.1 | $-501.97 | -12.0% | $498.03 | -2.5 | done | losing for real |
| value_ev5 | 553 | 40.0 | 42.1 | $-521.67 | -9.4% | $478.33 | -2.0 | done | can't tell from luck |
| momentum_60m_0.30pct | 626 | 47.4 | 49.7 | $-590.68 | -9.4% | $409.32 | -2.4 | done | losing for real |
| coinflip | 1164 | 50.2 | 50.9 | $-656.96 | -5.6% | $343.04 | -2.0 | done | can't tell from luck |
| momentum_15m_0.10pct | 768 | 46.2 | 49.7 | $-862.44 | -11.2% | $137.56 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 1164 | 49.3 | 51.3 | $-929.38 | -8.0% | $70.62 | -2.8 | done | losing for real |
| always_up | 1164 | 47.6 | 50.3 | $-1117.78 | -9.6% | $-117.78 | -3.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1733 | 46.8 | 49.3 | $-1574.54 |
| ETH | 1942 | 47.3 | 48.7 | $-1705.53 |
| SOL | 2022 | 48.3 | 49.3 | $-1556.64 |
| XRP | 2079 | 48.8 | 49.0 | $-1070.15 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
