# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 22, 7:30 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1150 windows, 31765 settled trades, 54 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 613 | 34.6 | 35.2 | $-387.85 | -6.3% | $612.15 | -1.2 | done | can't tell from luck |
| value_ev10 | 1497 | 38.2 | 39.2 | $-901.32 | -6.0% | $98.68 | -1.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 3189 | 51.0 | 50.4 | $-941.89 | -3.0% | $58.11 | -1.7 | done | can't tell from luck |
| momentum_60m_0.30pct | 2679 | 49.6 | 49.5 | $-1191.17 | -4.4% | $-191.17 | -2.3 | done | losing for real |
| value_ev5 | 2260 | 40.2 | 41.1 | $-1247.31 | -5.5% | $-247.31 | -2.2 | done | losing for real |
| trend_filter | 1883 | 48.9 | 50.5 | $-1532.30 | -8.1% | $-532.30 | -3.6 | done | losing for real |
| reversal_60m_0.30pct | 2679 | 50.4 | 51.0 | $-1641.51 | -6.1% | $-641.51 | -3.3 | done | losing for real |
| coinflip | 4592 | 50.3 | 50.2 | $-1893.09 | -4.1% | $-893.09 | -2.8 | done | losing for real |
| momentum_15m_0.10pct | 3189 | 49.0 | 50.2 | $-2011.48 | -6.3% | $-1011.48 | -3.6 | done | losing for real |
| momentum_5m_0.00pct | 4592 | 50.2 | 51.4 | $-2881.73 | -6.3% | $-1881.73 | -4.4 | done | losing for real |
| always_up | 4592 | 47.9 | 49.4 | $-3358.09 | -7.3% | $-2358.09 | -4.9 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7279 | 48.3 | 49.0 | $-3753.03 |
| ETH | 7869 | 48.1 | 48.4 | $-4651.89 |
| SOL | 8271 | 48.1 | 48.4 | $-4611.47 |
| XRP | 8346 | 48.1 | 48.2 | $-4971.36 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
