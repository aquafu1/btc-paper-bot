# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 17, 3:05 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 652 windows, 18035 settled trades, 39 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 341 | 34.3 | 35.4 | $-247.49 | -7.3% | $752.51 | -1.0 | done | can't tell from luck |
| momentum_60m_0.30pct | 1522 | 50.5 | 49.6 | $-397.47 | -2.6% | $602.53 | -1.0 | done | can't tell from luck |
| reversal_15m_0.10pct | 1853 | 51.6 | 51.0 | $-554.17 | -3.0% | $445.83 | -1.3 | done | can't tell from luck |
| value_ev10 | 833 | 38.3 | 39.5 | $-590.22 | -7.1% | $409.78 | -1.7 | done | can't tell from luck |
| trend_filter | 1041 | 50.0 | 50.9 | $-611.51 | -5.9% | $388.49 | -1.9 | done | can't tell from luck |
| value_ev5 | 1261 | 40.8 | 41.4 | $-665.58 | -5.3% | $334.42 | -1.6 | done | can't tell from luck |
| coinflip | 2603 | 50.1 | 50.5 | $-1186.31 | -4.6% | $-186.31 | -2.3 | done | losing for real |
| reversal_60m_0.30pct | 1522 | 49.5 | 51.4 | $-1218.42 | -8.0% | $-218.42 | -3.2 | done | losing for real |
| momentum_15m_0.10pct | 1853 | 48.4 | 50.0 | $-1288.80 | -7.0% | $-288.80 | -3.0 | done | losing for real |
| momentum_5m_0.00pct | 2603 | 50.6 | 51.7 | $-1479.03 | -5.7% | $-479.03 | -3.0 | done | losing for real |
| always_up | 2603 | 47.4 | 49.7 | $-2223.53 | -8.5% | $-1223.53 | -4.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4085 | 48.3 | 49.3 | $-2491.68 |
| ETH | 4503 | 48.2 | 48.7 | $-2746.90 |
| SOL | 4693 | 48.1 | 48.8 | $-2900.64 |
| XRP | 4754 | 48.5 | 48.6 | $-2323.30 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
