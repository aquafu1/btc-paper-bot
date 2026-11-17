# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 17, 1:20 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 597 windows, 16532 settled trades, 29 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 324 | 34.6 | 35.2 | $-214.70 | -6.6% | $785.30 | -0.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 1401 | 51.1 | 49.6 | $-221.37 | -1.6% | $778.63 | -0.6 | done | can't tell from luck |
| trend_filter | 955 | 50.3 | 50.9 | $-536.54 | -5.6% | $463.46 | -1.8 | done | can't tell from luck |
| value_ev10 | 777 | 38.2 | 39.4 | $-540.78 | -7.0% | $459.22 | -1.6 | done | can't tell from luck |
| value_ev5 | 1161 | 40.7 | 41.2 | $-625.25 | -5.4% | $374.75 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 1682 | 50.8 | 50.9 | $-790.63 | -4.7% | $209.37 | -2.0 | done | can't tell from luck |
| momentum_15m_0.10pct | 1682 | 49.2 | 50.0 | $-938.60 | -5.6% | $61.40 | -2.3 | done | losing for real |
| coinflip | 2383 | 49.9 | 50.5 | $-1197.67 | -5.0% | $-197.67 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 1401 | 48.9 | 51.3 | $-1313.73 | -9.4% | $-313.73 | -3.6 | done | losing for real |
| momentum_5m_0.00pct | 2383 | 50.4 | 51.7 | $-1497.48 | -6.3% | $-497.48 | -3.2 | done | losing for real |
| always_up | 2383 | 47.3 | 49.8 | $-2181.99 | -9.2% | $-1181.99 | -4.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3751 | 48.0 | 49.2 | $-2435.00 |
| ETH | 4125 | 48.0 | 48.6 | $-2617.56 |
| SOL | 4297 | 47.9 | 48.7 | $-2836.59 |
| XRP | 4359 | 48.5 | 48.6 | $-2169.60 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
