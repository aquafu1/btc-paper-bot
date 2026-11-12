# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 12, 1:35 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 176 windows, 4510 settled trades, 42 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 440 | 58.0 | 52.3 | $+342.48 | +7.8% | $1342.48 | +1.7 | done | can't tell from luck |
| reversal_60m_0.30pct | 332 | 59.6 | 53.2 | $+310.88 | +9.4% | $1310.88 | +1.8 | done | can't tell from luck |
| value_ev20 | 86 | 33.7 | 36.7 | $-133.13 | -15.5% | $866.87 | -1.2 | Sun 3:00 AM | too few trades (86/200) |
| value_ev10 | 226 | 37.2 | 40.5 | $-302.61 | -13.4% | $697.39 | -1.8 | done | can't tell from luck |
| momentum_5m_0.00pct | 697 | 50.8 | 51.2 | $-343.68 | -4.9% | $656.32 | -1.3 | done | can't tell from luck |
| value_ev5 | 335 | 38.8 | 42.4 | $-429.47 | -12.8% | $570.53 | -2.1 | done | losing for real |
| coinflip | 697 | 49.9 | 50.9 | $-434.71 | -6.2% | $565.29 | -1.7 | done | can't tell from luck |
| trend_filter | 228 | 40.8 | 49.2 | $-447.69 | -19.6% | $552.31 | -3.0 | done | losing for real |
| momentum_60m_0.30pct | 332 | 40.4 | 48.9 | $-684.80 | -20.6% | $315.20 | -3.8 | done | losing for real |
| momentum_15m_0.10pct | 440 | 42.0 | 49.8 | $-818.80 | -18.6% | $181.20 | -4.0 | done | losing for real |
| always_up | 697 | 46.2 | 50.0 | $-833.53 | -12.0% | $166.47 | -3.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 984 | 45.7 | 49.4 | $-997.65 |
| ETH | 1122 | 45.6 | 48.8 | $-1318.17 |
| SOL | 1178 | 47.5 | 48.9 | $-1073.07 |
| XRP | 1226 | 49.8 | 49.0 | $-386.17 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
