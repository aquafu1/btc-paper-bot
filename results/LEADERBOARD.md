# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 21, 10:35 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1066 windows, 29512 settled trades, 44 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 551 | 34.5 | 35.1 | $-323.30 | -5.9% | $676.70 | -1.0 | done | can't tell from luck |
| reversal_15m_0.10pct | 2988 | 51.3 | 50.4 | $-755.60 | -2.5% | $244.40 | -1.4 | done | can't tell from luck |
| value_ev10 | 1365 | 37.7 | 39.2 | $-960.20 | -7.0% | $39.80 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 2510 | 49.7 | 49.6 | $-1134.93 | -4.5% | $-134.93 | -2.3 | done | losing for real |
| trend_filter | 1757 | 49.6 | 50.7 | $-1258.73 | -7.2% | $-258.73 | -3.1 | done | losing for real |
| value_ev5 | 2072 | 39.7 | 41.0 | $-1351.78 | -6.5% | $-351.78 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 2510 | 50.3 | 51.0 | $-1603.27 | -6.4% | $-603.27 | -3.3 | done | losing for real |
| coinflip | 4257 | 50.5 | 50.3 | $-1691.03 | -4.0% | $-691.03 | -2.6 | done | losing for real |
| momentum_5m_0.00pct | 4257 | 51.0 | 51.5 | $-2080.94 | -4.9% | $-1080.94 | -3.3 | done | losing for real |
| momentum_15m_0.10pct | 2988 | 48.7 | 50.3 | $-2115.95 | -7.1% | $-1115.95 | -3.9 | done | losing for real |
| always_up | 4257 | 47.3 | 49.4 | $-3736.09 | -8.8% | $-2736.09 | -5.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6740 | 48.4 | 49.0 | $-3435.08 |
| ETH | 7299 | 48.1 | 48.5 | $-4635.84 |
| SOL | 7697 | 48.1 | 48.5 | $-4438.23 |
| XRP | 7776 | 48.3 | 48.3 | $-4502.65 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
