# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 20, 3:35 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 942 windows, 26083 settled trades, 46 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 480 | 35.0 | 34.9 | $-170.56 | -3.6% | $829.44 | -0.6 | done | can't tell from luck |
| value_ev10 | 1182 | 38.1 | 39.1 | $-678.57 | -5.7% | $321.43 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 2665 | 51.1 | 50.6 | $-852.85 | -3.2% | $147.15 | -1.7 | done | can't tell from luck |
| momentum_60m_0.30pct | 2230 | 50.1 | 49.8 | $-941.05 | -4.2% | $58.95 | -2.0 | done | losing for real |
| trend_filter | 1551 | 49.9 | 51.0 | $-1100.13 | -7.1% | $-100.13 | -2.9 | done | losing for real |
| value_ev5 | 1794 | 39.7 | 41.0 | $-1118.64 | -6.2% | $-118.64 | -2.2 | done | losing for real |
| reversal_60m_0.30pct | 2230 | 49.9 | 50.9 | $-1573.78 | -7.1% | $-573.78 | -3.4 | done | losing for real |
| coinflip | 3762 | 50.4 | 50.4 | $-1580.39 | -4.2% | $-580.39 | -2.6 | done | losing for real |
| momentum_15m_0.10pct | 2665 | 48.9 | 50.3 | $-1787.57 | -6.7% | $-787.57 | -3.5 | done | losing for real |
| momentum_5m_0.00pct | 3762 | 50.9 | 51.6 | $-1994.75 | -5.3% | $-994.75 | -3.4 | done | losing for real |
| always_up | 3762 | 46.7 | 49.7 | $-3897.40 | -10.4% | $-2897.40 | -6.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5949 | 48.1 | 49.1 | $-3510.95 |
| ETH | 6493 | 48.1 | 48.6 | $-4147.50 |
| SOL | 6798 | 48.1 | 48.6 | $-4017.32 |
| XRP | 6843 | 48.3 | 48.5 | $-4019.91 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
