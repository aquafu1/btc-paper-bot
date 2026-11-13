# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 13, 6:45 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 235 windows, 6137 settled trades, 43 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 601 | 56.2 | 52.6 | $+221.26 | +3.7% | $1221.26 | +1.0 | done | can't tell from luck |
| reversal_60m_0.30pct | 482 | 54.1 | 52.3 | $-3.08 | -0.1% | $996.92 | -0.0 | done | can't tell from luck |
| value_ev20 | 113 | 34.5 | 36.6 | $-110.27 | -9.8% | $889.73 | -0.8 | Sun 7:15 AM | too few trades (113/200) |
| value_ev10 | 301 | 37.9 | 40.8 | $-325.09 | -10.8% | $674.91 | -1.6 | done | can't tell from luck |
| value_ev5 | 437 | 39.6 | 42.5 | $-462.65 | -10.6% | $537.35 | -2.0 | done | can't tell from luck |
| trend_filter | 324 | 44.8 | 50.1 | $-466.22 | -14.4% | $533.78 | -2.6 | done | losing for real |
| momentum_60m_0.30pct | 482 | 45.9 | 49.8 | $-573.00 | -11.9% | $427.00 | -2.7 | done | losing for real |
| coinflip | 932 | 49.5 | 50.9 | $-638.61 | -6.9% | $361.39 | -2.2 | done | losing for real |
| momentum_5m_0.00pct | 932 | 49.7 | 51.4 | $-676.45 | -7.3% | $323.55 | -2.3 | done | losing for real |
| momentum_15m_0.10pct | 601 | 43.8 | 49.7 | $-918.95 | -15.3% | $81.05 | -3.8 | done | losing for real |
| always_up | 932 | 47.5 | 50.4 | $-927.31 | -9.9% | $72.69 | -3.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1373 | 46.3 | 49.7 | $-1424.98 |
| ETH | 1528 | 46.7 | 49.0 | $-1508.06 |
| SOL | 1586 | 48.1 | 49.3 | $-1231.34 |
| XRP | 1650 | 49.0 | 49.1 | $-716.00 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
