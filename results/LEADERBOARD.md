# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 20, 11:05 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 924 windows, 25542 settled trades, 38 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 475 | 35.2 | 34.8 | $-145.74 | -3.1% | $854.26 | -0.5 | done | can't tell from luck |
| value_ev10 | 1161 | 38.2 | 39.1 | $-632.90 | -5.5% | $367.10 | -1.5 | done | can't tell from luck |
| momentum_60m_0.30pct | 2174 | 50.2 | 49.8 | $-870.83 | -4.0% | $129.17 | -1.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 2604 | 50.6 | 50.5 | $-1025.58 | -3.9% | $-25.58 | -2.0 | done | losing for real |
| trend_filter | 1519 | 50.0 | 51.0 | $-1045.90 | -6.9% | $-45.90 | -2.8 | done | losing for real |
| value_ev5 | 1761 | 39.8 | 41.0 | $-1047.50 | -5.9% | $-47.50 | -2.1 | done | losing for real |
| momentum_15m_0.10pct | 2604 | 49.4 | 50.3 | $-1457.91 | -5.6% | $-457.91 | -2.9 | done | losing for real |
| reversal_60m_0.30pct | 2174 | 49.8 | 50.9 | $-1532.08 | -7.0% | $-532.08 | -3.4 | done | losing for real |
| coinflip | 3690 | 50.2 | 50.3 | $-1618.06 | -4.4% | $-618.06 | -2.7 | done | losing for real |
| momentum_5m_0.00pct | 3690 | 50.9 | 51.6 | $-1883.63 | -5.1% | $-883.63 | -3.2 | done | losing for real |
| always_up | 3690 | 46.8 | 49.7 | $-3734.46 | -10.1% | $-2734.46 | -6.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5823 | 48.2 | 49.1 | $-3328.63 |
| ETH | 6356 | 48.2 | 48.5 | $-3963.53 |
| SOL | 6658 | 48.1 | 48.6 | $-3930.81 |
| XRP | 6705 | 48.3 | 48.5 | $-3771.60 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
