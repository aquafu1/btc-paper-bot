# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 20, 11:00 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 924 windows, 25526 settled trades, 54 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 475 | 35.2 | 34.8 | $-145.74 | -3.1% | $854.26 | -0.5 | done | can't tell from luck |
| value_ev10 | 1161 | 38.2 | 39.1 | $-632.90 | -5.5% | $367.10 | -1.5 | done | can't tell from luck |
| momentum_60m_0.30pct | 2172 | 50.2 | 49.8 | $-850.83 | -3.9% | $149.17 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 2602 | 50.6 | 50.5 | $-1005.58 | -3.9% | $-5.58 | -2.0 | done | can't tell from luck |
| trend_filter | 1518 | 50.0 | 51.0 | $-1035.90 | -6.8% | $-35.90 | -2.7 | done | losing for real |
| value_ev5 | 1760 | 39.8 | 41.0 | $-1059.83 | -6.0% | $-59.83 | -2.1 | done | losing for real |
| momentum_15m_0.10pct | 2602 | 49.4 | 50.3 | $-1483.08 | -5.7% | $-483.08 | -2.9 | done | losing for real |
| reversal_60m_0.30pct | 2172 | 49.8 | 50.9 | $-1557.26 | -7.2% | $-557.26 | -3.4 | done | losing for real |
| coinflip | 3688 | 50.2 | 50.3 | $-1620.90 | -4.4% | $-620.90 | -2.7 | done | losing for real |
| momentum_5m_0.00pct | 3688 | 50.9 | 51.6 | $-1886.48 | -5.1% | $-886.48 | -3.2 | done | losing for real |
| always_up | 3688 | 46.8 | 49.7 | $-3759.63 | -10.2% | $-2759.63 | -6.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5816 | 48.1 | 49.1 | $-3372.84 |
| ETH | 6347 | 48.2 | 48.5 | $-3962.85 |
| SOL | 6658 | 48.1 | 48.6 | $-3930.81 |
| XRP | 6705 | 48.3 | 48.5 | $-3771.60 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
