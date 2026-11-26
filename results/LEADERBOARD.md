# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 26, 3:05 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1468 windows, 37029 settled trades, 352 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 749 | 34.0 | 35.4 | $-623.47 | -8.3% | $376.53 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 3691 | 50.9 | 50.1 | $-970.60 | -2.6% | $29.40 | -1.6 | done | can't tell from luck |
| value_ev10 | 1805 | 38.4 | 39.2 | $-980.25 | -5.4% | $19.75 | -1.9 | done | can't tell from luck |
| value_ev5 | 2720 | 40.4 | 41.1 | $-1454.27 | -5.3% | $-454.27 | -2.4 | done | losing for real |
| momentum_60m_0.30pct | 3097 | 49.2 | 49.2 | $-1542.10 | -5.0% | $-542.10 | -2.8 | done | losing for real |
| reversal_60m_0.30pct | 3097 | 50.8 | 51.0 | $-1583.76 | -5.1% | $-583.76 | -2.9 | done | losing for real |
| trend_filter | 2198 | 48.7 | 50.3 | $-1868.29 | -8.5% | $-868.29 | -4.1 | done | losing for real |
| momentum_15m_0.10pct | 3691 | 49.1 | 50.2 | $-2326.80 | -6.3% | $-1326.80 | -3.9 | done | losing for real |
| coinflip | 5327 | 49.9 | 50.0 | $-2406.46 | -4.5% | $-1406.46 | -3.3 | done | losing for real |
| momentum_5m_0.00pct | 5327 | 50.1 | 51.3 | $-3333.30 | -6.3% | $-2333.30 | -4.7 | done | losing for real |
| always_up | 5327 | 48.0 | 49.2 | $-3564.01 | -6.7% | $-2564.01 | -4.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 9510 | 48.0 | 48.7 | $-5236.72 |
| ETH | 10209 | 47.9 | 48.0 | $-5832.36 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
