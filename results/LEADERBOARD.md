# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 19, 6:50 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 859 windows, 23686 settled trades, 36 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 444 | 34.5 | 34.8 | $-237.85 | -5.4% | $762.15 | -0.8 | done | can't tell from luck |
| value_ev10 | 1082 | 37.8 | 39.0 | $-716.18 | -6.6% | $283.82 | -1.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 2003 | 50.2 | 49.7 | $-787.52 | -3.9% | $212.48 | -1.8 | done | can't tell from luck |
| trend_filter | 1394 | 50.1 | 50.9 | $-896.12 | -6.4% | $103.88 | -2.5 | done | losing for real |
| reversal_15m_0.10pct | 2418 | 50.7 | 50.5 | $-924.94 | -3.8% | $75.06 | -1.9 | done | can't tell from luck |
| value_ev5 | 1637 | 39.8 | 41.0 | $-1029.50 | -6.3% | $-29.50 | -2.1 | done | losing for real |
| momentum_15m_0.10pct | 2418 | 49.3 | 50.4 | $-1435.19 | -5.9% | $-435.19 | -2.9 | done | losing for real |
| reversal_60m_0.30pct | 2003 | 49.8 | 51.0 | $-1479.22 | -7.4% | $-479.22 | -3.4 | done | losing for real |
| coinflip | 3429 | 50.2 | 50.3 | $-1522.94 | -4.4% | $-522.94 | -2.6 | done | losing for real |
| momentum_5m_0.00pct | 3429 | 51.2 | 51.7 | $-1617.09 | -4.7% | $-617.09 | -2.9 | done | losing for real |
| always_up | 3429 | 47.0 | 49.5 | $-3287.90 | -9.6% | $-2287.90 | -5.6 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5401 | 48.3 | 49.0 | $-2974.16 |
| ETH | 5894 | 48.1 | 48.5 | $-3873.03 |
| SOL | 6184 | 48.2 | 48.5 | $-3572.13 |
| XRP | 6207 | 48.3 | 48.5 | $-3515.14 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
