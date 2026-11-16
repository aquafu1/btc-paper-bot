# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 16, 7:30 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 526 windows, 14524 settled trades, 62 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1240 | 51.5 | 49.8 | $-101.45 | -0.8% | $898.55 | -0.3 | done | can't tell from luck |
| value_ev20 | 274 | 35.4 | 35.7 | $-152.64 | -5.6% | $847.36 | -0.7 | done | can't tell from luck |
| value_ev10 | 676 | 38.3 | 39.8 | $-494.70 | -7.3% | $505.30 | -1.6 | done | can't tell from luck |
| momentum_15m_0.10pct | 1473 | 49.8 | 49.7 | $-543.76 | -3.7% | $456.24 | -1.4 | done | can't tell from luck |
| trend_filter | 851 | 49.5 | 50.7 | $-551.72 | -6.5% | $448.28 | -1.9 | done | can't tell from luck |
| value_ev5 | 1009 | 40.4 | 41.5 | $-638.33 | -6.3% | $361.67 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 1473 | 50.2 | 51.5 | $-1003.62 | -6.8% | $-3.62 | -2.7 | done | losing for real |
| coinflip | 2096 | 50.0 | 50.7 | $-1124.28 | -5.4% | $-124.28 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 1240 | 48.5 | 51.4 | $-1203.22 | -9.7% | $-203.22 | -3.5 | done | losing for real |
| momentum_5m_0.00pct | 2096 | 49.3 | 51.6 | $-1705.60 | -8.1% | $-705.60 | -3.9 | done | losing for real |
| always_up | 2096 | 46.3 | 50.1 | $-2444.13 | -11.7% | $-1444.13 | -5.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3289 | 47.4 | 49.2 | $-2605.92 |
| ETH | 3622 | 48.0 | 48.7 | $-2377.48 |
| SOL | 3788 | 47.7 | 49.0 | $-2737.99 |
| XRP | 3825 | 48.3 | 48.8 | $-2242.08 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
