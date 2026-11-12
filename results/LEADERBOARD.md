# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 12, 1:00 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 174 windows, 4449 settled trades, 54 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 434 | 58.3 | 52.6 | $+350.00 | +8.1% | $1350.00 | +1.8 | done | can't tell from luck |
| reversal_60m_0.30pct | 328 | 59.8 | 53.1 | $+324.17 | +9.9% | $1324.17 | +1.9 | done | can't tell from luck |
| value_ev20 | 82 | 34.1 | 37.1 | $-121.99 | -14.9% | $878.01 | -1.1 | Sun 6:15 AM | too few trades (82/200) |
| value_ev10 | 222 | 37.4 | 40.8 | $-291.47 | -13.1% | $708.53 | -1.7 | done | can't tell from luck |
| momentum_5m_0.00pct | 688 | 51.0 | 51.1 | $-293.50 | -4.3% | $706.50 | -1.2 | done | can't tell from luck |
| value_ev5 | 329 | 38.6 | 42.6 | $-442.86 | -13.5% | $557.14 | -2.2 | done | losing for real |
| coinflip | 688 | 49.9 | 50.9 | $-443.58 | -6.4% | $556.42 | -1.8 | done | can't tell from luck |
| trend_filter | 228 | 40.8 | 49.2 | $-447.69 | -19.6% | $552.31 | -3.0 | done | losing for real |
| momentum_60m_0.30pct | 328 | 40.2 | 49.1 | $-693.35 | -21.1% | $306.65 | -3.9 | done | losing for real |
| always_up | 688 | 46.7 | 50.1 | $-772.40 | -11.2% | $227.60 | -3.0 | done | losing for real |
| momentum_15m_0.10pct | 434 | 41.7 | 49.6 | $-825.07 | -19.0% | $174.93 | -4.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 965 | 46.0 | 49.5 | $-913.80 |
| ETH | 1109 | 45.8 | 48.9 | $-1242.64 |
| SOL | 1165 | 47.6 | 49.0 | $-1002.24 |
| XRP | 1210 | 49.7 | 49.1 | $-499.06 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
