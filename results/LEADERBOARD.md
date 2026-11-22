# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 22, 4:00 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1088 windows, 30086 settled trades, 76 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 565 | 34.7 | 35.2 | $-301.63 | -5.3% | $698.37 | -1.0 | done | can't tell from luck |
| reversal_15m_0.10pct | 3041 | 51.1 | 50.5 | $-851.80 | -2.8% | $148.20 | -1.5 | done | can't tell from luck |
| value_ev10 | 1392 | 37.9 | 39.2 | $-887.02 | -6.4% | $112.98 | -1.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 2556 | 49.8 | 49.5 | $-1026.95 | -4.0% | $-26.95 | -2.0 | done | losing for real |
| trend_filter | 1786 | 49.6 | 50.6 | $-1245.66 | -7.0% | $-245.66 | -3.0 | done | losing for real |
| value_ev5 | 2117 | 39.9 | 41.1 | $-1261.64 | -6.0% | $-261.64 | -2.3 | done | losing for real |
| coinflip | 4344 | 50.6 | 50.3 | $-1592.88 | -3.7% | $-592.88 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 2556 | 50.2 | 51.1 | $-1706.50 | -6.7% | $-706.50 | -3.5 | done | losing for real |
| momentum_15m_0.10pct | 3041 | 48.9 | 50.3 | $-2019.80 | -6.6% | $-1019.80 | -3.7 | done | losing for real |
| momentum_5m_0.00pct | 4344 | 50.9 | 51.5 | $-2146.83 | -4.9% | $-1146.83 | -3.4 | done | losing for real |
| always_up | 4344 | 47.5 | 49.4 | $-3497.58 | -8.1% | $-2497.58 | -5.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6870 | 48.5 | 49.0 | $-3334.46 |
| ETH | 7452 | 48.2 | 48.5 | $-4377.35 |
| SOL | 7843 | 48.1 | 48.5 | $-4409.91 |
| XRP | 7921 | 48.3 | 48.3 | $-4416.56 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
