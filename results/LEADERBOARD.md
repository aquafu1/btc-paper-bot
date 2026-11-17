# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 17, 1:15 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 597 windows, 16511 settled trades, 50 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1399 | 51.2 | 49.6 | $-201.37 | -1.4% | $798.63 | -0.5 | done | can't tell from luck |
| value_ev20 | 324 | 34.6 | 35.2 | $-214.70 | -6.6% | $785.30 | -0.9 | done | can't tell from luck |
| value_ev10 | 776 | 38.3 | 39.4 | $-530.78 | -6.8% | $469.22 | -1.6 | done | can't tell from luck |
| trend_filter | 955 | 50.3 | 50.9 | $-536.54 | -5.6% | $463.46 | -1.8 | done | can't tell from luck |
| value_ev5 | 1160 | 40.7 | 41.2 | $-615.25 | -5.3% | $384.75 | -1.5 | done | can't tell from luck |
| reversal_15m_0.10pct | 1679 | 50.9 | 51.0 | $-760.63 | -4.5% | $239.37 | -1.9 | done | can't tell from luck |
| momentum_15m_0.10pct | 1679 | 49.1 | 50.0 | $-955.66 | -5.7% | $44.34 | -2.3 | done | losing for real |
| coinflip | 2380 | 50.0 | 50.5 | $-1183.62 | -5.0% | $-183.62 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 1399 | 48.8 | 51.3 | $-1324.05 | -9.5% | $-324.05 | -3.6 | done | losing for real |
| momentum_5m_0.00pct | 2380 | 50.3 | 51.7 | $-1514.54 | -6.4% | $-514.54 | -3.2 | done | losing for real |
| always_up | 2380 | 47.2 | 49.8 | $-2199.05 | -9.2% | $-1199.05 | -4.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3751 | 48.0 | 49.2 | $-2435.00 |
| ETH | 4116 | 48.0 | 48.6 | $-2607.29 |
| SOL | 4292 | 47.9 | 48.7 | $-2836.79 |
| XRP | 4352 | 48.5 | 48.5 | $-2157.11 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
