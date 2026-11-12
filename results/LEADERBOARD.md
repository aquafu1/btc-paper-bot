# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 11, 8:45 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 109 windows, 2792 settled trades, 51 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 213 | 60.1 | 53.0 | $+234.36 | +11.0% | $1234.36 | +1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 271 | 55.0 | 52.0 | $+97.29 | +3.6% | $1097.29 | +0.6 | done | can't tell from luck |
| momentum_5m_0.00pct | 428 | 53.5 | 50.8 | $+71.57 | +1.7% | $1071.57 | +0.4 | done | can't tell from luck |
| value_ev10 | 145 | 40.0 | 40.7 | $-89.56 | -6.2% | $910.44 | -0.6 | Thu 7:45 AM | too few trades (145/200) |
| value_ev20 | 50 | 28.0 | 36.5 | $-123.85 | -24.8% | $876.15 | -1.4 | Sun 12:15 PM | too few trades (50/200) |
| trend_filter | 145 | 42.8 | 49.0 | $-228.02 | -15.7% | $771.98 | -1.9 | Thu 7:45 AM | too few trades (145/200) |
| value_ev5 | 200 | 38.0 | 42.0 | $-261.21 | -13.1% | $738.79 | -1.6 | done | can't tell from luck |
| coinflip | 428 | 49.8 | 51.4 | $-292.18 | -6.8% | $707.82 | -1.5 | done | can't tell from luck |
| momentum_15m_0.10pct | 271 | 45.0 | 50.2 | $-356.42 | -13.2% | $643.58 | -2.2 | done | losing for real |
| always_up | 428 | 47.7 | 50.3 | $-373.14 | -8.7% | $626.86 | -1.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 213 | 39.9 | 49.1 | $-449.02 | -21.1% | $550.98 | -3.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 603 | 46.1 | 49.7 | $-502.24 |
| ETH | 677 | 45.9 | 48.9 | $-604.33 |
| SOL | 748 | 48.8 | 48.6 | $-412.16 |
| XRP | 764 | 50.5 | 49.1 | $-251.45 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
