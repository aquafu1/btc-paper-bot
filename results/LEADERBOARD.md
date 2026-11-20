# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 20, 10:45 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 923 windows, 25495 settled trades, 62 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 475 | 35.2 | 34.8 | $-145.74 | -3.1% | $854.26 | -0.5 | done | can't tell from luck |
| value_ev10 | 1161 | 38.2 | 39.1 | $-632.90 | -5.5% | $367.10 | -1.5 | done | can't tell from luck |
| momentum_60m_0.30pct | 2168 | 50.3 | 49.8 | $-810.83 | -3.7% | $189.17 | -1.7 | done | can't tell from luck |
| trend_filter | 1515 | 50.1 | 51.0 | $-1005.90 | -6.6% | $-5.90 | -2.7 | done | losing for real |
| reversal_15m_0.10pct | 2598 | 50.5 | 50.5 | $-1033.73 | -4.0% | $-33.73 | -2.0 | done | losing for real |
| value_ev5 | 1760 | 39.8 | 41.0 | $-1059.83 | -6.0% | $-59.83 | -2.1 | done | losing for real |
| momentum_15m_0.10pct | 2598 | 49.5 | 50.3 | $-1443.08 | -5.6% | $-443.08 | -2.9 | done | losing for real |
| coinflip | 3684 | 50.3 | 50.3 | $-1580.90 | -4.3% | $-580.90 | -2.6 | done | losing for real |
| reversal_60m_0.30pct | 2168 | 49.7 | 50.9 | $-1585.41 | -7.3% | $-585.41 | -3.5 | done | losing for real |
| momentum_5m_0.00pct | 3684 | 51.0 | 51.7 | $-1863.49 | -5.1% | $-863.49 | -3.2 | done | losing for real |
| always_up | 3684 | 46.7 | 49.7 | $-3787.78 | -10.3% | $-2787.78 | -6.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5808 | 48.2 | 49.1 | $-3346.61 |
| ETH | 6340 | 48.2 | 48.5 | $-3960.91 |
| SOL | 6650 | 48.1 | 48.6 | $-3901.86 |
| XRP | 6697 | 48.3 | 48.5 | $-3740.20 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
