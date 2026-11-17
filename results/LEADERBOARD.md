# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 17, 8:30 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 626 windows, 17299 settled trades, 57 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1463 | 51.3 | 49.5 | $-147.87 | -1.0% | $852.13 | -0.4 | done | can't tell from luck |
| value_ev20 | 329 | 34.0 | 35.3 | $-264.70 | -8.0% | $735.30 | -1.1 | done | can't tell from luck |
| trend_filter | 1002 | 50.2 | 50.8 | $-551.18 | -5.5% | $448.82 | -1.8 | done | can't tell from luck |
| value_ev10 | 800 | 38.2 | 39.5 | $-584.31 | -7.3% | $415.69 | -1.7 | done | can't tell from luck |
| value_ev5 | 1210 | 40.6 | 41.4 | $-729.30 | -6.0% | $270.70 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 1772 | 50.8 | 51.1 | $-830.50 | -4.7% | $169.50 | -2.0 | done | losing for real |
| momentum_15m_0.10pct | 1772 | 49.2 | 49.9 | $-972.93 | -5.5% | $27.07 | -2.3 | done | losing for real |
| coinflip | 2496 | 50.0 | 50.5 | $-1228.99 | -4.9% | $-228.99 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 1463 | 48.7 | 51.4 | $-1434.72 | -9.8% | $-434.72 | -3.9 | done | losing for real |
| momentum_5m_0.00pct | 2496 | 50.3 | 51.7 | $-1559.06 | -6.2% | $-559.06 | -3.2 | done | losing for real |
| always_up | 2496 | 47.5 | 49.7 | $-2116.38 | -8.5% | $-1116.38 | -4.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3927 | 48.2 | 49.2 | $-2422.77 |
| ETH | 4330 | 48.2 | 48.6 | $-2643.03 |
| SOL | 4492 | 48.0 | 48.8 | $-2972.58 |
| XRP | 4550 | 48.4 | 48.5 | $-2381.55 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
