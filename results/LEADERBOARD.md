# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 17, 8:50 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 627 windows, 17326 settled trades, 49 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1463 | 51.3 | 49.5 | $-147.87 | -1.0% | $852.13 | -0.4 | done | can't tell from luck |
| value_ev20 | 330 | 33.9 | 35.3 | $-274.70 | -8.3% | $725.30 | -1.2 | done | can't tell from luck |
| trend_filter | 1002 | 50.2 | 50.8 | $-551.18 | -5.5% | $448.82 | -1.8 | done | can't tell from luck |
| value_ev10 | 802 | 38.2 | 39.5 | $-604.31 | -7.5% | $395.69 | -1.8 | done | can't tell from luck |
| value_ev5 | 1214 | 40.4 | 41.4 | $-769.30 | -6.3% | $230.70 | -1.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 1776 | 50.8 | 51.0 | $-854.64 | -4.8% | $145.36 | -2.1 | done | losing for real |
| momentum_15m_0.10pct | 1776 | 49.2 | 49.9 | $-965.33 | -5.4% | $34.67 | -2.3 | done | losing for real |
| coinflip | 2500 | 50.0 | 50.5 | $-1221.40 | -4.9% | $-221.40 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 1463 | 48.7 | 51.4 | $-1434.72 | -9.8% | $-434.72 | -3.9 | done | losing for real |
| momentum_5m_0.00pct | 2500 | 50.3 | 51.7 | $-1583.11 | -6.3% | $-583.11 | -3.3 | done | losing for real |
| always_up | 2500 | 47.4 | 49.6 | $-2156.38 | -8.6% | $-1156.38 | -4.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3933 | 48.2 | 49.2 | $-2450.88 |
| ETH | 4336 | 48.1 | 48.6 | $-2671.63 |
| SOL | 4499 | 47.9 | 48.8 | $-3026.73 |
| XRP | 4558 | 48.4 | 48.5 | $-2413.71 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
