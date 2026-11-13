# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 12, 10:15 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 201 windows, 5197 settled trades, 61 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 510 | 57.8 | 52.7 | $+324.26 | +6.4% | $1324.26 | +1.5 | done | can't tell from luck |
| reversal_60m_0.30pct | 388 | 57.0 | 52.8 | $+161.99 | +4.2% | $1161.99 | +0.9 | done | can't tell from luck |
| value_ev20 | 99 | 30.3 | 37.1 | $-238.58 | -24.1% | $761.42 | -2.0 | Sun 6:00 AM | too few trades (99/200) |
| momentum_5m_0.00pct | 796 | 51.5 | 51.4 | $-322.92 | -4.1% | $677.08 | -1.2 | done | can't tell from luck |
| trend_filter | 266 | 44.0 | 49.7 | $-401.92 | -15.1% | $598.08 | -2.5 | done | losing for real |
| coinflip | 796 | 50.3 | 51.0 | $-488.49 | -6.1% | $511.51 | -1.8 | done | can't tell from luck |
| value_ev10 | 264 | 35.2 | 41.0 | $-494.03 | -18.7% | $505.97 | -2.7 | done | losing for real |
| value_ev5 | 384 | 38.0 | 42.7 | $-595.55 | -15.5% | $404.45 | -2.8 | done | losing for real |
| momentum_60m_0.30pct | 388 | 43.0 | 49.4 | $-660.40 | -17.0% | $339.60 | -3.4 | done | losing for real |
| momentum_15m_0.10pct | 510 | 42.2 | 49.6 | $-947.66 | -18.6% | $52.34 | -4.3 | done | losing for real |
| always_up | 796 | 45.4 | 50.3 | $-1146.42 | -14.4% | $-146.42 | -4.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1148 | 45.8 | 49.6 | $-1287.78 |
| ETH | 1293 | 46.1 | 48.9 | $-1477.23 |
| SOL | 1345 | 47.6 | 49.2 | $-1244.96 |
| XRP | 1411 | 49.1 | 49.2 | $-799.73 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
