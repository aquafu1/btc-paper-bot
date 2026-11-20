# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 20, 10:50 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 923 windows, 25511 settled trades, 46 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 475 | 35.2 | 34.8 | $-145.74 | -3.1% | $854.26 | -0.5 | done | can't tell from luck |
| value_ev10 | 1161 | 38.2 | 39.1 | $-632.90 | -5.5% | $367.10 | -1.5 | done | can't tell from luck |
| momentum_60m_0.30pct | 2170 | 50.3 | 49.8 | $-830.83 | -3.8% | $169.17 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 2600 | 50.6 | 50.5 | $-1018.79 | -3.9% | $-18.79 | -2.0 | done | can't tell from luck |
| trend_filter | 1517 | 50.0 | 51.0 | $-1025.90 | -6.8% | $-25.90 | -2.7 | done | losing for real |
| value_ev5 | 1760 | 39.8 | 41.0 | $-1059.83 | -6.0% | $-59.83 | -2.1 | done | losing for real |
| momentum_15m_0.10pct | 2600 | 49.4 | 50.3 | $-1463.08 | -5.6% | $-463.08 | -2.9 | done | losing for real |
| reversal_60m_0.30pct | 2170 | 49.7 | 50.9 | $-1570.47 | -7.2% | $-570.47 | -3.4 | done | losing for real |
| coinflip | 3686 | 50.3 | 50.3 | $-1600.90 | -4.3% | $-600.90 | -2.7 | done | losing for real |
| momentum_5m_0.00pct | 3686 | 50.9 | 51.6 | $-1883.49 | -5.1% | $-883.49 | -3.2 | done | losing for real |
| always_up | 3686 | 46.7 | 49.7 | $-3772.84 | -10.2% | $-2772.84 | -6.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5816 | 48.1 | 49.1 | $-3372.84 |
| ETH | 6340 | 48.2 | 48.5 | $-3960.91 |
| SOL | 6658 | 48.1 | 48.6 | $-3930.81 |
| XRP | 6697 | 48.3 | 48.5 | $-3740.20 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
