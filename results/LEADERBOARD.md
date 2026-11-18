# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 17, 11:45 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 687 windows, 19004 settled trades, 64 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 360 | 34.4 | 35.0 | $-213.12 | -5.9% | $786.88 | -0.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 1604 | 50.4 | 49.5 | $-422.64 | -2.6% | $577.36 | -1.0 | done | can't tell from luck |
| value_ev10 | 878 | 38.5 | 39.2 | $-489.28 | -5.6% | $510.72 | -1.3 | done | can't tell from luck |
| trend_filter | 1108 | 50.4 | 50.9 | $-590.30 | -5.3% | $409.70 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 1955 | 51.5 | 50.9 | $-598.51 | -3.1% | $401.49 | -1.4 | done | can't tell from luck |
| value_ev5 | 1320 | 40.8 | 41.1 | $-604.58 | -4.6% | $395.42 | -1.4 | done | can't tell from luck |
| coinflip | 2740 | 50.2 | 50.3 | $-1169.53 | -4.3% | $-169.53 | -2.2 | done | losing for real |
| reversal_60m_0.30pct | 1604 | 49.6 | 51.3 | $-1263.87 | -7.9% | $-263.87 | -3.2 | done | losing for real |
| momentum_15m_0.10pct | 1955 | 48.5 | 49.9 | $-1288.04 | -6.6% | $-288.04 | -2.9 | done | losing for real |
| momentum_5m_0.00pct | 2740 | 50.8 | 51.8 | $-1515.86 | -5.5% | $-515.86 | -3.0 | done | losing for real |
| always_up | 2740 | 47.5 | 49.6 | $-2271.04 | -8.3% | $-1271.04 | -4.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4320 | 48.3 | 49.1 | $-2460.57 |
| ETH | 4734 | 48.3 | 48.6 | $-2802.40 |
| SOL | 4953 | 48.2 | 48.6 | $-2853.26 |
| XRP | 4997 | 48.6 | 48.5 | $-2310.52 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
