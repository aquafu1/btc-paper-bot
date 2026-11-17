# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 17, 11:45 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 639 windows, 17670 settled trades, 48 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1495 | 51.1 | 49.6 | $-193.57 | -1.3% | $806.43 | -0.5 | done | can't tell from luck |
| value_ev20 | 333 | 34.2 | 35.3 | $-246.80 | -7.4% | $753.20 | -1.0 | done | can't tell from luck |
| trend_filter | 1020 | 50.5 | 50.8 | $-507.93 | -5.0% | $492.07 | -1.6 | done | can't tell from luck |
| value_ev10 | 812 | 38.4 | 39.5 | $-551.51 | -6.8% | $448.49 | -1.6 | done | can't tell from luck |
| value_ev5 | 1233 | 40.9 | 41.4 | $-646.63 | -5.2% | $353.37 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 1819 | 51.1 | 51.0 | $-696.20 | -3.8% | $303.80 | -1.7 | done | can't tell from luck |
| momentum_15m_0.10pct | 1819 | 48.9 | 50.0 | $-1110.98 | -6.1% | $-110.98 | -2.6 | done | losing for real |
| coinflip | 2548 | 50.1 | 50.5 | $-1171.73 | -4.6% | $-171.73 | -2.3 | done | losing for real |
| reversal_60m_0.30pct | 1495 | 48.9 | 51.4 | $-1378.94 | -9.2% | $-378.94 | -3.7 | done | losing for real |
| momentum_5m_0.00pct | 2548 | 50.7 | 51.7 | $-1379.63 | -5.4% | $-379.63 | -2.8 | done | losing for real |
| always_up | 2548 | 47.3 | 49.7 | $-2246.29 | -8.8% | $-1246.29 | -4.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4016 | 48.4 | 49.3 | $-2345.13 |
| ETH | 4420 | 48.3 | 48.6 | $-2601.36 |
| SOL | 4585 | 48.0 | 48.8 | $-2936.81 |
| XRP | 4649 | 48.5 | 48.5 | $-2246.91 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
