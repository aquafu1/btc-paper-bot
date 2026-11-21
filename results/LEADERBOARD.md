# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 21, 3:20 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1037 windows, 28811 settled trades, 40 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 535 | 34.8 | 35.1 | $-274.76 | -5.1% | $725.24 | -0.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 2930 | 51.2 | 50.5 | $-801.53 | -2.7% | $198.47 | -1.5 | done | can't tell from luck |
| value_ev10 | 1328 | 37.5 | 39.2 | $-982.06 | -7.4% | $17.94 | -2.2 | done | losing for real |
| momentum_60m_0.30pct | 2466 | 49.7 | 49.6 | $-1132.65 | -4.6% | $-132.65 | -2.3 | done | losing for real |
| trend_filter | 1723 | 49.3 | 50.7 | $-1345.73 | -7.8% | $-345.73 | -3.3 | done | losing for real |
| value_ev5 | 2010 | 39.5 | 41.0 | $-1383.93 | -6.9% | $-383.93 | -2.6 | done | losing for real |
| reversal_60m_0.30pct | 2466 | 50.3 | 51.0 | $-1592.08 | -6.5% | $-592.08 | -3.3 | done | losing for real |
| coinflip | 4141 | 50.5 | 50.3 | $-1645.58 | -4.0% | $-645.58 | -2.6 | done | losing for real |
| momentum_15m_0.10pct | 2930 | 48.8 | 50.3 | $-2037.63 | -7.0% | $-1037.63 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 4141 | 50.7 | 51.5 | $-2307.50 | -5.6% | $-1307.50 | -3.7 | done | losing for real |
| always_up | 4141 | 47.4 | 49.5 | $-3571.24 | -8.6% | $-2571.24 | -5.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6573 | 48.3 | 49.0 | $-3613.49 |
| ETH | 7141 | 48.1 | 48.5 | $-4433.23 |
| SOL | 7523 | 48.1 | 48.6 | $-4352.03 |
| XRP | 7574 | 48.1 | 48.3 | $-4675.94 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
