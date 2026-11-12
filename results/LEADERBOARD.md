# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 12, 3:15 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 183 windows, 4666 settled trades, 43 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 343 | 59.8 | 53.0 | $+335.32 | +9.8% | $1335.32 | +1.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 453 | 57.8 | 52.4 | $+333.98 | +7.4% | $1333.98 | +1.7 | done | can't tell from luck |
| value_ev20 | 88 | 34.1 | 36.7 | $-128.58 | -14.6% | $871.42 | -1.1 | Sun 4:00 AM | too few trades (88/200) |
| momentum_5m_0.00pct | 724 | 51.4 | 51.3 | $-274.81 | -3.8% | $725.19 | -1.1 | done | can't tell from luck |
| value_ev10 | 235 | 37.0 | 40.6 | $-320.73 | -13.6% | $679.27 | -1.8 | done | can't tell from luck |
| coinflip | 724 | 50.3 | 50.9 | $-397.10 | -5.5% | $602.90 | -1.5 | done | can't tell from luck |
| value_ev5 | 346 | 38.7 | 42.4 | $-446.22 | -12.9% | $553.78 | -2.1 | done | losing for real |
| trend_filter | 233 | 41.2 | 49.4 | $-448.40 | -19.2% | $551.60 | -2.9 | done | losing for real |
| momentum_60m_0.30pct | 343 | 40.2 | 49.0 | $-730.36 | -21.3% | $269.64 | -4.0 | done | losing for real |
| momentum_15m_0.10pct | 453 | 42.2 | 49.7 | $-823.94 | -18.2% | $176.06 | -3.9 | done | losing for real |
| always_up | 724 | 46.1 | 50.0 | $-878.97 | -12.1% | $121.03 | -3.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1017 | 45.6 | 49.4 | $-1064.01 |
| ETH | 1164 | 46.0 | 48.8 | $-1278.70 |
| SOL | 1210 | 47.6 | 49.0 | $-1056.56 |
| XRP | 1275 | 50.0 | 49.1 | $-380.54 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
