# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 21, 5:20 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 997 windows, 27709 settled trades, 56 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 509 | 34.0 | 34.9 | $-325.26 | -6.4% | $674.74 | -1.1 | done | can't tell from luck |
| reversal_15m_0.10pct | 2828 | 51.1 | 50.4 | $-816.85 | -2.9% | $183.15 | -1.5 | done | can't tell from luck |
| value_ev10 | 1265 | 37.4 | 39.1 | $-938.79 | -7.4% | $61.21 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 2380 | 49.7 | 49.7 | $-1126.46 | -4.7% | $-126.46 | -2.3 | done | losing for real |
| trend_filter | 1661 | 49.4 | 50.8 | $-1264.66 | -7.6% | $-264.66 | -3.2 | done | losing for real |
| value_ev5 | 1918 | 39.5 | 41.0 | $-1289.34 | -6.7% | $-289.34 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 2380 | 50.3 | 50.9 | $-1529.38 | -6.4% | $-529.38 | -3.2 | done | losing for real |
| coinflip | 3980 | 50.3 | 50.3 | $-1744.57 | -4.4% | $-744.57 | -2.8 | done | losing for real |
| momentum_15m_0.10pct | 2828 | 48.9 | 50.3 | $-1974.40 | -7.0% | $-974.40 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 3980 | 50.7 | 51.5 | $-2227.38 | -5.6% | $-1227.38 | -3.6 | done | losing for real |
| always_up | 3980 | 46.9 | 49.6 | $-3914.92 | -9.8% | $-2914.92 | -6.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6317 | 48.2 | 49.1 | $-3564.04 |
| ETH | 6884 | 48.0 | 48.5 | $-4541.93 |
| SOL | 7244 | 48.1 | 48.6 | $-4330.40 |
| XRP | 7264 | 48.0 | 48.4 | $-4715.62 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
