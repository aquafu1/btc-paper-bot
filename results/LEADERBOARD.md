# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 18, 8:20 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 721 windows, 19848 settled trades, 41 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 379 | 33.5 | 34.9 | $-314.03 | -8.3% | $685.97 | -1.2 | done | can't tell from luck |
| reversal_15m_0.10pct | 2034 | 51.7 | 50.8 | $-499.40 | -2.5% | $500.60 | -1.1 | done | can't tell from luck |
| momentum_60m_0.30pct | 1662 | 50.1 | 49.5 | $-572.73 | -3.4% | $427.27 | -1.4 | done | can't tell from luck |
| value_ev10 | 912 | 38.0 | 39.1 | $-592.90 | -6.5% | $407.10 | -1.6 | done | can't tell from luck |
| trend_filter | 1160 | 50.3 | 50.9 | $-656.37 | -5.7% | $343.63 | -2.0 | done | can't tell from luck |
| value_ev5 | 1374 | 40.7 | 41.1 | $-668.40 | -4.9% | $331.60 | -1.5 | done | can't tell from luck |
| reversal_60m_0.30pct | 1662 | 49.9 | 51.3 | $-1211.07 | -7.3% | $-211.07 | -3.0 | done | losing for real |
| coinflip | 2877 | 50.1 | 50.3 | $-1288.12 | -4.5% | $-288.12 | -2.4 | done | losing for real |
| momentum_5m_0.00pct | 2877 | 51.1 | 51.8 | $-1427.55 | -5.0% | $-427.55 | -2.8 | done | losing for real |
| momentum_15m_0.10pct | 2034 | 48.3 | 50.0 | $-1462.17 | -7.2% | $-462.17 | -3.2 | done | losing for real |
| always_up | 2877 | 47.2 | 49.5 | $-2530.23 | -8.8% | $-1530.23 | -4.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4490 | 48.1 | 49.1 | $-2812.43 |
| ETH | 4946 | 48.2 | 48.5 | $-2971.58 |
| SOL | 5173 | 48.2 | 48.7 | $-3027.75 |
| XRP | 5239 | 48.6 | 48.4 | $-2411.21 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
