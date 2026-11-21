# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 21, 1:35 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1030 windows, 28645 settled trades, 39 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 530 | 34.7 | 35.1 | $-278.51 | -5.3% | $721.49 | -0.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 2916 | 51.1 | 50.5 | $-874.36 | -3.0% | $125.64 | -1.6 | done | can't tell from luck |
| value_ev10 | 1316 | 37.6 | 39.2 | $-940.06 | -7.1% | $59.94 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 2460 | 49.8 | 49.6 | $-1072.65 | -4.4% | $-72.65 | -2.2 | done | losing for real |
| trend_filter | 1715 | 49.4 | 50.7 | $-1281.06 | -7.5% | $-281.06 | -3.2 | done | losing for real |
| value_ev5 | 1993 | 39.5 | 41.0 | $-1378.88 | -6.9% | $-378.88 | -2.6 | done | losing for real |
| reversal_60m_0.30pct | 2460 | 50.2 | 51.0 | $-1642.07 | -6.7% | $-642.07 | -3.4 | done | losing for real |
| coinflip | 4113 | 50.5 | 50.3 | $-1666.24 | -4.1% | $-666.24 | -2.6 | done | losing for real |
| momentum_15m_0.10pct | 2916 | 48.9 | 50.3 | $-1953.27 | -6.7% | $-953.27 | -3.7 | done | losing for real |
| momentum_5m_0.00pct | 4113 | 50.7 | 51.5 | $-2226.30 | -5.4% | $-1226.30 | -3.6 | done | losing for real |
| always_up | 4113 | 47.4 | 49.5 | $-3561.73 | -8.7% | $-2561.73 | -5.6 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6535 | 48.3 | 49.1 | $-3558.63 |
| ETH | 7109 | 48.2 | 48.5 | $-4348.27 |
| SOL | 7476 | 48.2 | 48.6 | $-4274.36 |
| XRP | 7525 | 48.1 | 48.4 | $-4693.89 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
