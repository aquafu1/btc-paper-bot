# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 21, 4:20 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1041 windows, 28903 settled trades, 41 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 541 | 34.6 | 35.1 | $-305.47 | -5.6% | $694.53 | -1.0 | done | can't tell from luck |
| reversal_15m_0.10pct | 2933 | 51.2 | 50.5 | $-831.53 | -2.8% | $168.47 | -1.5 | done | can't tell from luck |
| value_ev10 | 1338 | 37.4 | 39.2 | $-1031.50 | -7.7% | $-31.50 | -2.3 | done | losing for real |
| momentum_60m_0.30pct | 2470 | 49.8 | 49.6 | $-1127.09 | -4.6% | $-127.09 | -2.3 | done | losing for real |
| trend_filter | 1727 | 49.3 | 50.7 | $-1356.95 | -7.9% | $-356.95 | -3.4 | done | losing for real |
| value_ev5 | 2023 | 39.3 | 41.0 | $-1463.37 | -7.2% | $-463.37 | -2.8 | done | losing for real |
| reversal_60m_0.30pct | 2470 | 50.2 | 51.0 | $-1610.82 | -6.5% | $-610.82 | -3.3 | done | losing for real |
| coinflip | 4156 | 50.5 | 50.3 | $-1679.14 | -4.0% | $-679.14 | -2.6 | done | losing for real |
| momentum_15m_0.10pct | 2933 | 48.8 | 50.3 | $-2022.31 | -6.9% | $-1022.31 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 4156 | 50.8 | 51.5 | $-2266.58 | -5.5% | $-1266.58 | -3.6 | done | losing for real |
| always_up | 4156 | 47.4 | 49.4 | $-3614.74 | -8.7% | $-2614.74 | -5.6 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6589 | 48.3 | 49.0 | $-3566.26 |
| ETH | 7158 | 48.1 | 48.5 | $-4452.27 |
| SOL | 7548 | 48.1 | 48.5 | $-4492.49 |
| XRP | 7608 | 48.1 | 48.3 | $-4798.48 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
