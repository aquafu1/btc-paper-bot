# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 21, 5:00 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 996 windows, 27690 settled trades, 42 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 509 | 34.0 | 34.9 | $-325.26 | -6.4% | $674.74 | -1.1 | done | can't tell from luck |
| reversal_15m_0.10pct | 2825 | 51.1 | 50.4 | $-847.72 | -3.0% | $152.28 | -1.6 | done | can't tell from luck |
| value_ev10 | 1265 | 37.4 | 39.1 | $-938.79 | -7.4% | $61.21 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 2380 | 49.7 | 49.7 | $-1126.46 | -4.7% | $-126.46 | -2.3 | done | losing for real |
| trend_filter | 1661 | 49.4 | 50.8 | $-1264.66 | -7.6% | $-264.66 | -3.2 | done | losing for real |
| value_ev5 | 1917 | 39.5 | 41.0 | $-1300.50 | -6.8% | $-300.50 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 2380 | 50.3 | 50.9 | $-1529.38 | -6.4% | $-529.38 | -3.2 | done | losing for real |
| coinflip | 3976 | 50.3 | 50.3 | $-1740.45 | -4.4% | $-740.45 | -2.8 | done | losing for real |
| momentum_15m_0.10pct | 2825 | 48.9 | 50.3 | $-1944.40 | -6.9% | $-944.40 | -3.7 | done | losing for real |
| momentum_5m_0.00pct | 3976 | 50.7 | 51.5 | $-2223.26 | -5.6% | $-1223.26 | -3.6 | done | losing for real |
| always_up | 3976 | 46.8 | 49.6 | $-3953.57 | -9.9% | $-2953.57 | -6.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6312 | 48.2 | 49.1 | $-3557.27 |
| ETH | 6878 | 48.0 | 48.5 | $-4545.43 |
| SOL | 7239 | 48.1 | 48.6 | $-4352.80 |
| XRP | 7261 | 48.0 | 48.4 | $-4738.95 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
