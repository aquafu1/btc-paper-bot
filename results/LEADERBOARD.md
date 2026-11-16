# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 16, 4:35 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 514 windows, 14169 settled trades, 70 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 265 | 34.3 | 35.5 | $-188.91 | -7.1% | $811.09 | -0.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 1204 | 51.0 | 49.8 | $-230.20 | -1.9% | $769.80 | -0.7 | done | can't tell from luck |
| value_ev10 | 662 | 38.1 | 39.7 | $-503.23 | -7.6% | $496.77 | -1.6 | done | can't tell from luck |
| trend_filter | 831 | 49.2 | 50.8 | $-609.18 | -7.3% | $390.82 | -2.2 | done | losing for real |
| momentum_15m_0.10pct | 1437 | 49.5 | 49.6 | $-614.62 | -4.3% | $385.38 | -1.6 | done | can't tell from luck |
| value_ev5 | 985 | 39.9 | 41.5 | $-729.96 | -7.4% | $270.04 | -2.0 | done | can't tell from luck |
| reversal_15m_0.10pct | 1437 | 50.5 | 51.6 | $-915.58 | -6.4% | $84.42 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 1204 | 49.0 | 51.4 | $-1071.69 | -8.9% | $-71.69 | -3.2 | done | losing for real |
| coinflip | 2048 | 50.0 | 50.7 | $-1093.69 | -5.3% | $-93.69 | -2.5 | done | losing for real |
| momentum_5m_0.00pct | 2048 | 49.4 | 51.6 | $-1639.93 | -8.0% | $-639.93 | -3.8 | done | losing for real |
| always_up | 2048 | 46.3 | 50.1 | $-2365.87 | -11.6% | $-1365.87 | -5.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3206 | 47.3 | 49.2 | $-2629.12 |
| ETH | 3539 | 48.0 | 48.7 | $-2357.39 |
| SOL | 3691 | 47.6 | 49.0 | $-2775.01 |
| XRP | 3733 | 48.3 | 48.8 | $-2201.35 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
