# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 17, 12:30 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 594 windows, 16429 settled trades, 51 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1391 | 51.2 | 49.6 | $-212.68 | -1.5% | $787.32 | -0.6 | done | can't tell from luck |
| value_ev20 | 322 | 34.2 | 35.2 | $-257.97 | -8.0% | $742.03 | -1.1 | done | can't tell from luck |
| trend_filter | 954 | 50.2 | 51.0 | $-548.37 | -5.7% | $451.63 | -1.8 | done | can't tell from luck |
| value_ev10 | 770 | 37.8 | 39.4 | $-636.74 | -8.3% | $363.26 | -1.9 | done | can't tell from luck |
| value_ev5 | 1153 | 40.3 | 41.2 | $-733.04 | -6.4% | $266.96 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 1672 | 50.8 | 51.0 | $-791.37 | -4.7% | $208.63 | -2.0 | done | can't tell from luck |
| momentum_15m_0.10pct | 1672 | 49.2 | 49.9 | $-949.79 | -5.7% | $50.21 | -2.3 | done | losing for real |
| coinflip | 2368 | 50.0 | 50.5 | $-1205.37 | -5.1% | $-205.37 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 1391 | 48.8 | 51.3 | $-1344.80 | -9.7% | $-344.80 | -3.7 | done | losing for real |
| momentum_5m_0.00pct | 2368 | 50.2 | 51.8 | $-1591.72 | -6.7% | $-591.72 | -3.4 | done | losing for real |
| always_up | 2368 | 47.3 | 49.8 | $-2179.79 | -9.2% | $-1179.79 | -4.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3730 | 47.9 | 49.2 | $-2565.66 |
| ETH | 4097 | 48.0 | 48.6 | $-2650.31 |
| SOL | 4272 | 47.9 | 48.7 | $-2965.55 |
| XRP | 4330 | 48.5 | 48.6 | $-2270.13 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
