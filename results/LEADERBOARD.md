# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 12, 1:30 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 176 windows, 4503 settled trades, 49 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 439 | 58.1 | 52.3 | $+352.48 | +8.0% | $1352.48 | +1.8 | done | can't tell from luck |
| reversal_60m_0.30pct | 331 | 59.8 | 53.2 | $+320.88 | +9.7% | $1320.88 | +1.9 | done | can't tell from luck |
| value_ev20 | 86 | 33.7 | 36.7 | $-133.13 | -15.5% | $866.87 | -1.2 | Sun 2:15 AM | too few trades (86/200) |
| value_ev10 | 226 | 37.2 | 40.5 | $-302.61 | -13.4% | $697.39 | -1.8 | done | can't tell from luck |
| momentum_5m_0.00pct | 696 | 50.9 | 51.2 | $-333.68 | -4.8% | $666.32 | -1.3 | done | can't tell from luck |
| value_ev5 | 335 | 38.8 | 42.4 | $-429.47 | -12.8% | $570.53 | -2.1 | done | losing for real |
| coinflip | 696 | 49.9 | 50.9 | $-444.39 | -6.4% | $555.61 | -1.7 | done | can't tell from luck |
| trend_filter | 228 | 40.8 | 49.2 | $-447.69 | -19.6% | $552.31 | -3.0 | done | losing for real |
| momentum_60m_0.30pct | 331 | 40.2 | 48.8 | $-694.48 | -21.0% | $305.52 | -3.8 | done | losing for real |
| always_up | 696 | 46.3 | 50.0 | $-823.53 | -11.8% | $176.47 | -3.2 | done | losing for real |
| momentum_15m_0.10pct | 439 | 41.9 | 49.8 | $-828.48 | -18.9% | $171.52 | -4.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 977 | 45.8 | 49.4 | $-986.68 |
| ETH | 1122 | 45.6 | 48.8 | $-1318.17 |
| SOL | 1178 | 47.5 | 48.9 | $-1073.07 |
| XRP | 1226 | 49.8 | 49.0 | $-386.17 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
