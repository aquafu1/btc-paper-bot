# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 16, 8:30 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 578 windows, 15992 settled trades, 58 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1360 | 51.1 | 49.6 | $-268.07 | -2.0% | $731.93 | -0.7 | done | can't tell from luck |
| value_ev20 | 310 | 33.5 | 35.2 | $-314.56 | -10.1% | $685.44 | -1.4 | done | can't tell from luck |
| trend_filter | 928 | 50.4 | 51.0 | $-514.64 | -5.5% | $485.36 | -1.7 | done | can't tell from luck |
| value_ev10 | 749 | 37.7 | 39.4 | $-677.94 | -9.1% | $322.06 | -2.1 | done | losing for real |
| reversal_15m_0.10pct | 1626 | 51.1 | 51.0 | $-733.41 | -4.5% | $266.59 | -1.9 | done | can't tell from luck |
| value_ev5 | 1121 | 40.1 | 41.3 | $-823.91 | -7.3% | $176.09 | -2.1 | done | losing for real |
| momentum_15m_0.10pct | 1626 | 48.9 | 49.9 | $-1007.49 | -6.2% | $-7.49 | -2.5 | done | losing for real |
| coinflip | 2304 | 49.9 | 50.5 | $-1236.96 | -5.4% | $-236.96 | -2.6 | done | losing for real |
| reversal_60m_0.30pct | 1360 | 48.9 | 51.3 | $-1299.88 | -9.6% | $-299.88 | -3.6 | done | losing for real |
| momentum_5m_0.00pct | 2304 | 50.2 | 51.9 | $-1623.49 | -7.0% | $-623.49 | -3.5 | done | losing for real |
| always_up | 2304 | 47.0 | 49.9 | $-2314.22 | -10.0% | $-1314.22 | -4.9 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3623 | 47.8 | 49.3 | $-2661.00 |
| ETH | 3989 | 48.0 | 48.6 | $-2733.06 |
| SOL | 4164 | 47.8 | 48.8 | $-3133.61 |
| XRP | 4216 | 48.5 | 48.6 | $-2286.91 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
