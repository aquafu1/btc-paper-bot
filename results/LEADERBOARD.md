# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 21, 4:00 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 992 windows, 27579 settled trades, 51 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 505 | 34.3 | 34.9 | $-285.26 | -5.6% | $714.74 | -0.9 | done | can't tell from luck |
| value_ev10 | 1259 | 37.5 | 39.1 | $-901.38 | -7.2% | $98.62 | -2.1 | done | losing for real |
| reversal_15m_0.10pct | 2817 | 50.9 | 50.4 | $-907.92 | -3.2% | $92.08 | -1.7 | done | can't tell from luck |
| momentum_60m_0.30pct | 2371 | 49.9 | 49.7 | $-1056.76 | -4.5% | $-56.76 | -2.2 | done | losing for real |
| trend_filter | 1652 | 49.6 | 50.9 | $-1195.81 | -7.2% | $-195.81 | -3.0 | done | losing for real |
| value_ev5 | 1907 | 39.5 | 41.0 | $-1264.56 | -6.6% | $-264.56 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 2371 | 50.1 | 50.9 | $-1571.50 | -6.6% | $-571.50 | -3.3 | done | losing for real |
| coinflip | 3960 | 50.2 | 50.3 | $-1797.17 | -4.5% | $-797.17 | -2.9 | done | losing for real |
| momentum_15m_0.10pct | 2817 | 49.1 | 50.4 | $-1864.40 | -6.6% | $-864.40 | -3.6 | done | losing for real |
| momentum_5m_0.00pct | 3960 | 50.8 | 51.5 | $-2100.22 | -5.3% | $-1100.22 | -3.4 | done | losing for real |
| always_up | 3960 | 46.9 | 49.6 | $-3897.22 | -9.8% | $-2897.22 | -6.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6289 | 48.2 | 49.1 | $-3565.20 |
| ETH | 6851 | 48.0 | 48.5 | $-4461.37 |
| SOL | 7205 | 48.1 | 48.6 | $-4229.78 |
| XRP | 7234 | 48.1 | 48.5 | $-4585.85 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
