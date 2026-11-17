# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 17, 3:15 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 653 windows, 18040 settled trades, 61 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 341 | 34.3 | 35.4 | $-247.49 | -7.3% | $752.51 | -1.0 | done | can't tell from luck |
| momentum_60m_0.30pct | 1523 | 50.4 | 49.6 | $-407.47 | -2.7% | $592.53 | -1.0 | done | can't tell from luck |
| reversal_15m_0.10pct | 1853 | 51.6 | 51.0 | $-554.17 | -3.0% | $445.83 | -1.3 | done | can't tell from luck |
| value_ev10 | 833 | 38.3 | 39.5 | $-590.22 | -7.1% | $409.78 | -1.7 | done | can't tell from luck |
| trend_filter | 1041 | 50.0 | 50.9 | $-611.51 | -5.9% | $388.49 | -1.9 | done | can't tell from luck |
| value_ev5 | 1261 | 40.8 | 41.4 | $-665.58 | -5.3% | $334.42 | -1.6 | done | can't tell from luck |
| coinflip | 2604 | 50.1 | 50.5 | $-1196.31 | -4.6% | $-196.31 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 1523 | 49.6 | 51.4 | $-1210.50 | -7.9% | $-210.50 | -3.2 | done | losing for real |
| momentum_15m_0.10pct | 1853 | 48.4 | 50.0 | $-1288.80 | -7.0% | $-288.80 | -3.0 | done | losing for real |
| momentum_5m_0.00pct | 2604 | 50.6 | 51.7 | $-1471.10 | -5.6% | $-471.10 | -3.0 | done | losing for real |
| always_up | 2604 | 47.4 | 49.7 | $-2233.53 | -8.6% | $-1233.53 | -4.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4090 | 48.3 | 49.3 | $-2505.84 |
| ETH | 4503 | 48.2 | 48.7 | $-2746.90 |
| SOL | 4693 | 48.1 | 48.8 | $-2900.64 |
| XRP | 4754 | 48.5 | 48.6 | $-2323.30 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
