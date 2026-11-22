# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 22, 1:05 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1076 windows, 29767 settled trades, 57 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 556 | 34.4 | 35.1 | $-347.14 | -6.2% | $652.86 | -1.1 | done | can't tell from luck |
| reversal_15m_0.10pct | 3016 | 51.3 | 50.5 | $-787.73 | -2.6% | $212.27 | -1.4 | done | can't tell from luck |
| value_ev10 | 1374 | 37.6 | 39.2 | $-981.22 | -7.1% | $18.78 | -2.2 | done | losing for real |
| momentum_60m_0.30pct | 2529 | 49.7 | 49.6 | $-1135.32 | -4.5% | $-135.32 | -2.3 | done | losing for real |
| trend_filter | 1771 | 49.5 | 50.6 | $-1270.08 | -7.2% | $-270.08 | -3.1 | done | losing for real |
| value_ev5 | 2088 | 39.7 | 41.0 | $-1379.21 | -6.6% | $-379.21 | -2.6 | done | losing for real |
| reversal_60m_0.30pct | 2529 | 50.3 | 51.0 | $-1623.89 | -6.4% | $-623.89 | -3.3 | done | losing for real |
| coinflip | 4296 | 50.5 | 50.3 | $-1693.90 | -3.9% | $-693.90 | -2.6 | done | losing for real |
| momentum_5m_0.00pct | 4296 | 51.0 | 51.5 | $-2084.11 | -4.9% | $-1084.11 | -3.3 | done | losing for real |
| momentum_15m_0.10pct | 3016 | 48.7 | 50.3 | $-2129.19 | -7.1% | $-1129.19 | -3.9 | done | losing for real |
| always_up | 4296 | 47.3 | 49.4 | $-3748.93 | -8.7% | $-2748.93 | -5.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6791 | 48.4 | 49.0 | $-3491.66 |
| ETH | 7368 | 48.2 | 48.5 | $-4541.99 |
| SOL | 7763 | 48.1 | 48.5 | $-4485.98 |
| XRP | 7845 | 48.2 | 48.3 | $-4661.08 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
