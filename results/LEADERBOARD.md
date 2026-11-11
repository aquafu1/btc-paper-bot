# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 11, 2:05 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 92 windows, 2339 settled trades, 50 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_5m_0.00pct | 361 | 55.7 | 50.9 | $+217.71 | +6.0% | $1217.71 | +1.2 | done | can't tell from luck |
| reversal_60m_0.30pct | 174 | 58.6 | 52.7 | $+146.43 | +8.4% | $1146.43 | +1.2 | Wed 5:30 PM | too few trades (174/200) |
| reversal_15m_0.10pct | 225 | 56.4 | 52.4 | $+124.18 | +5.5% | $1124.18 | +0.9 | done | can't tell from luck |
| value_ev10 | 120 | 40.8 | 40.2 | $-43.12 | -3.6% | $956.88 | -0.3 | Thu 5:15 AM | too few trades (120/200) |
| value_ev20 | 45 | 31.1 | 36.1 | $-73.85 | -16.4% | $926.15 | -0.9 | Sat 8:30 PM | too few trades (45/200) |
| trend_filter | 127 | 47.2 | 48.8 | $-84.96 | -6.7% | $915.04 | -0.7 | Thu 3:15 AM | too few trades (127/200) |
| value_ev5 | 166 | 38.6 | 41.7 | $-188.55 | -11.4% | $811.45 | -1.3 | Wed 6:45 PM | too few trades (166/200) |
| coinflip | 361 | 49.9 | 51.6 | $-241.78 | -6.7% | $758.22 | -1.3 | done | can't tell from luck |
| momentum_60m_0.30pct | 174 | 41.4 | 49.0 | $-318.56 | -18.3% | $681.44 | -2.4 | Wed 5:30 PM | too few trades (174/200) |
| momentum_15m_0.10pct | 225 | 43.6 | 49.5 | $-332.32 | -14.8% | $667.68 | -2.2 | done | losing for real |
| always_up | 361 | 45.7 | 50.1 | $-432.70 | -12.0% | $567.30 | -2.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 503 | 47.5 | 49.8 | $-226.84 |
| ETH | 568 | 46.7 | 48.7 | $-360.20 |
| SOL | 627 | 49.6 | 48.6 | $-258.78 |
| XRP | 641 | 49.5 | 48.8 | $-381.70 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
