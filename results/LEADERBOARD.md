# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 15, 6:30 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 474 windows, 12998 settled trades, 52 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 238 | 35.3 | 35.9 | $-125.26 | -5.3% | $874.74 | -0.6 | done | can't tell from luck |
| momentum_60m_0.30pct | 1100 | 50.7 | 50.0 | $-301.76 | -2.7% | $698.24 | -0.9 | done | can't tell from luck |
| value_ev10 | 614 | 39.3 | 40.2 | $-344.93 | -5.6% | $655.07 | -1.2 | done | can't tell from luck |
| momentum_15m_0.10pct | 1310 | 50.0 | 50.1 | $-470.32 | -3.6% | $529.68 | -1.3 | done | can't tell from luck |
| value_ev5 | 908 | 41.2 | 41.9 | $-477.62 | -5.3% | $522.38 | -1.4 | done | can't tell from luck |
| trend_filter | 754 | 49.3 | 50.8 | $-511.85 | -6.8% | $488.15 | -1.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 1310 | 50.0 | 51.4 | $-875.74 | -6.7% | $124.26 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 1100 | 49.3 | 51.4 | $-924.14 | -8.4% | $75.86 | -2.8 | done | losing for real |
| coinflip | 1888 | 49.9 | 50.8 | $-1041.45 | -5.5% | $-41.45 | -2.4 | done | losing for real |
| momentum_5m_0.00pct | 1888 | 49.5 | 51.7 | $-1435.64 | -7.6% | $-435.64 | -3.4 | done | losing for real |
| always_up | 1888 | 46.7 | 50.4 | $-2088.70 | -11.1% | $-1088.70 | -4.9 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2935 | 47.5 | 49.3 | $-2242.32 |
| ETH | 3257 | 48.1 | 48.9 | $-2144.57 |
| SOL | 3385 | 47.7 | 49.3 | $-2507.54 |
| XRP | 3421 | 48.6 | 49.1 | $-1702.97 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
