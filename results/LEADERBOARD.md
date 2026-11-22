# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 21, 10:20 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1065 windows, 29483 settled trades, 53 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 551 | 34.5 | 35.1 | $-323.30 | -5.9% | $676.70 | -1.0 | done | can't tell from luck |
| reversal_15m_0.10pct | 2984 | 51.3 | 50.4 | $-731.67 | -2.5% | $268.33 | -1.3 | done | can't tell from luck |
| value_ev10 | 1363 | 37.7 | 39.2 | $-940.20 | -6.9% | $59.80 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 2509 | 49.7 | 49.6 | $-1124.93 | -4.5% | $-124.93 | -2.2 | done | losing for real |
| trend_filter | 1757 | 49.6 | 50.7 | $-1258.73 | -7.2% | $-258.73 | -3.1 | done | losing for real |
| value_ev5 | 2070 | 39.7 | 41.0 | $-1331.78 | -6.4% | $-331.78 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 2509 | 50.3 | 51.0 | $-1611.51 | -6.4% | $-611.51 | -3.3 | done | losing for real |
| coinflip | 4252 | 50.5 | 50.3 | $-1717.36 | -4.0% | $-717.36 | -2.7 | done | losing for real |
| momentum_5m_0.00pct | 4252 | 50.9 | 51.5 | $-2125.52 | -5.0% | $-1125.52 | -3.4 | done | losing for real |
| momentum_15m_0.10pct | 2984 | 48.7 | 50.3 | $-2136.21 | -7.2% | $-1136.21 | -4.0 | done | losing for real |
| always_up | 4252 | 47.2 | 49.4 | $-3764.60 | -8.9% | $-2764.60 | -5.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6728 | 48.4 | 49.0 | $-3439.81 |
| ETH | 7292 | 48.1 | 48.5 | $-4620.58 |
| SOL | 7692 | 48.1 | 48.5 | $-4471.13 |
| XRP | 7771 | 48.3 | 48.3 | $-4534.27 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
