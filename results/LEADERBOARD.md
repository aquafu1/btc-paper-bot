# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 15, 7:20 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 477 windows, 13097 settled trades, 49 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 239 | 35.1 | 35.9 | $-135.26 | -5.7% | $864.74 | -0.7 | done | can't tell from luck |
| momentum_60m_0.30pct | 1108 | 50.7 | 49.9 | $-298.12 | -2.7% | $701.88 | -0.9 | done | can't tell from luck |
| value_ev10 | 617 | 39.1 | 40.2 | $-374.93 | -6.1% | $625.07 | -1.3 | done | can't tell from luck |
| momentum_15m_0.10pct | 1323 | 50.1 | 50.0 | $-444.47 | -3.4% | $555.53 | -1.2 | done | can't tell from luck |
| trend_filter | 763 | 49.4 | 50.7 | $-502.26 | -6.6% | $497.74 | -1.9 | done | can't tell from luck |
| value_ev5 | 913 | 41.0 | 41.9 | $-527.62 | -5.8% | $472.38 | -1.5 | done | can't tell from luck |
| reversal_15m_0.10pct | 1323 | 49.9 | 51.4 | $-924.80 | -7.0% | $75.20 | -2.6 | done | losing for real |
| reversal_60m_0.30pct | 1108 | 49.3 | 51.5 | $-939.39 | -8.5% | $60.61 | -2.9 | done | losing for real |
| coinflip | 1901 | 49.9 | 50.8 | $-1047.33 | -5.5% | $-47.33 | -2.4 | done | losing for real |
| momentum_5m_0.00pct | 1901 | 49.7 | 51.7 | $-1393.59 | -7.3% | $-393.59 | -3.3 | done | losing for real |
| always_up | 1901 | 46.6 | 50.4 | $-2153.96 | -11.3% | $-1153.96 | -5.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2956 | 47.4 | 49.3 | $-2305.10 |
| ETH | 3290 | 48.1 | 48.9 | $-2183.87 |
| SOL | 3406 | 47.7 | 49.3 | $-2509.97 |
| XRP | 3445 | 48.6 | 49.1 | $-1742.79 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
