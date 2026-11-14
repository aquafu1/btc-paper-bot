# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 13, 9:45 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 295 windows, 7839 settled trades, 61 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 776 | 53.7 | 51.9 | $-67.12 | -0.9% | $932.88 | -0.3 | done | can't tell from luck |
| value_ev20 | 147 | 35.4 | 36.4 | $-124.69 | -8.5% | $875.31 | -0.8 | Sun 1:45 AM | too few trades (147/200) |
| reversal_60m_0.30pct | 632 | 52.1 | 51.9 | $-262.25 | -4.1% | $737.75 | -1.1 | done | can't tell from luck |
| value_ev10 | 380 | 38.2 | 40.4 | $-373.14 | -9.8% | $626.86 | -1.6 | done | can't tell from luck |
| trend_filter | 423 | 46.8 | 50.2 | $-483.71 | -11.4% | $516.29 | -2.4 | done | losing for real |
| momentum_60m_0.30pct | 632 | 47.9 | 49.7 | $-543.54 | -8.6% | $456.46 | -2.2 | done | losing for real |
| value_ev5 | 557 | 39.7 | 42.1 | $-561.67 | -10.1% | $438.33 | -2.1 | done | losing for real |
| coinflip | 1172 | 50.3 | 50.9 | $-650.25 | -5.5% | $349.75 | -2.0 | done | can't tell from luck |
| momentum_15m_0.10pct | 776 | 46.3 | 49.8 | $-878.57 | -11.3% | $121.43 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 1172 | 49.3 | 51.3 | $-945.52 | -8.1% | $54.48 | -2.9 | done | losing for real |
| always_up | 1172 | 47.3 | 50.3 | $-1197.78 | -10.2% | $-197.78 | -3.6 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1750 | 46.7 | 49.3 | $-1638.98 |
| ETH | 1960 | 47.2 | 48.7 | $-1753.67 |
| SOL | 2038 | 48.3 | 49.3 | $-1572.16 |
| XRP | 2091 | 48.7 | 49.0 | $-1123.44 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
