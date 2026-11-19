# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 19, 8:15 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 817 windows, 22404 settled trades, 59 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 413 | 33.4 | 35.0 | $-341.28 | -8.3% | $658.72 | -1.3 | done | can't tell from luck |
| value_ev10 | 1022 | 37.8 | 39.2 | $-709.76 | -6.9% | $290.24 | -1.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 1874 | 50.1 | 49.6 | $-748.10 | -4.0% | $251.90 | -1.7 | done | can't tell from luck |
| trend_filter | 1312 | 50.1 | 50.9 | $-835.49 | -6.4% | $164.51 | -2.4 | done | losing for real |
| reversal_15m_0.10pct | 2291 | 50.8 | 50.6 | $-889.16 | -3.9% | $110.84 | -1.9 | done | can't tell from luck |
| value_ev5 | 1547 | 40.1 | 41.1 | $-923.94 | -6.0% | $76.06 | -2.0 | done | can't tell from luck |
| momentum_15m_0.10pct | 2291 | 49.2 | 50.2 | $-1324.83 | -5.8% | $-324.83 | -2.8 | done | losing for real |
| reversal_60m_0.30pct | 1874 | 49.9 | 51.2 | $-1335.74 | -7.1% | $-335.74 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 3260 | 51.3 | 51.7 | $-1439.26 | -4.4% | $-439.26 | -2.6 | done | losing for real |
| coinflip | 3260 | 50.1 | 50.3 | $-1474.99 | -4.5% | $-474.99 | -2.6 | done | losing for real |
| always_up | 3260 | 47.5 | 49.7 | $-2795.53 | -8.6% | $-1795.53 | -4.9 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5081 | 48.3 | 49.1 | $-2941.72 |
| ETH | 5576 | 48.2 | 48.6 | $-3523.28 |
| SOL | 5843 | 48.2 | 48.6 | $-3291.43 |
| XRP | 5904 | 48.5 | 48.5 | $-3061.67 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
