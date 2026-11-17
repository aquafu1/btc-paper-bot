# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 17, 3:50 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 655 windows, 18125 settled trades, 30 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 343 | 34.1 | 35.4 | $-267.49 | -7.8% | $732.51 | -1.1 | done | can't tell from luck |
| momentum_60m_0.30pct | 1533 | 50.6 | 49.7 | $-369.39 | -2.4% | $630.61 | -0.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 1858 | 51.6 | 51.0 | $-534.51 | -2.9% | $465.49 | -1.3 | done | can't tell from luck |
| trend_filter | 1051 | 50.3 | 51.0 | $-577.23 | -5.5% | $422.77 | -1.8 | done | can't tell from luck |
| value_ev10 | 838 | 38.2 | 39.5 | $-615.05 | -7.3% | $384.95 | -1.8 | done | can't tell from luck |
| value_ev5 | 1266 | 40.8 | 41.4 | $-690.41 | -5.5% | $309.59 | -1.7 | done | can't tell from luck |
| coinflip | 2615 | 50.1 | 50.5 | $-1180.22 | -4.5% | $-180.22 | -2.3 | done | losing for real |
| reversal_60m_0.30pct | 1533 | 49.4 | 51.3 | $-1240.84 | -8.1% | $-240.84 | -3.2 | done | losing for real |
| momentum_15m_0.10pct | 1858 | 48.4 | 50.0 | $-1285.71 | -6.9% | $-285.71 | -3.0 | done | losing for real |
| momentum_5m_0.00pct | 2615 | 50.7 | 51.8 | $-1446.83 | -5.5% | $-446.83 | -2.9 | done | losing for real |
| always_up | 2615 | 47.5 | 49.7 | $-2184.08 | -8.4% | $-1184.08 | -4.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4106 | 48.3 | 49.3 | $-2487.89 |
| ETH | 4524 | 48.3 | 48.7 | $-2762.91 |
| SOL | 4718 | 48.1 | 48.8 | $-2868.82 |
| XRP | 4777 | 48.5 | 48.6 | $-2272.14 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
