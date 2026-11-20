# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 20, 3:50 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 895 windows, 24718 settled trades, 32 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 463 | 35.6 | 34.9 | $-91.30 | -2.0% | $908.70 | -0.3 | done | can't tell from luck |
| value_ev10 | 1136 | 38.3 | 39.1 | $-594.14 | -5.2% | $405.86 | -1.4 | done | can't tell from luck |
| momentum_60m_0.30pct | 2086 | 49.9 | 49.8 | $-958.73 | -4.6% | $41.27 | -2.1 | done | losing for real |
| trend_filter | 1459 | 50.1 | 51.0 | $-967.94 | -6.6% | $32.06 | -2.6 | done | losing for real |
| value_ev5 | 1717 | 40.0 | 41.0 | $-987.05 | -5.7% | $12.95 | -2.0 | done | losing for real |
| reversal_15m_0.10pct | 2523 | 50.4 | 50.4 | $-1037.52 | -4.1% | $-37.52 | -2.1 | done | losing for real |
| reversal_60m_0.30pct | 2086 | 50.1 | 50.9 | $-1342.90 | -6.4% | $-342.90 | -3.0 | done | losing for real |
| momentum_15m_0.10pct | 2523 | 49.6 | 50.4 | $-1353.90 | -5.4% | $-353.90 | -2.7 | done | losing for real |
| coinflip | 3575 | 50.2 | 50.3 | $-1555.15 | -4.4% | $-555.15 | -2.6 | done | losing for real |
| momentum_5m_0.00pct | 3575 | 51.4 | 51.7 | $-1564.83 | -4.4% | $-564.83 | -2.7 | done | losing for real |
| always_up | 3575 | 46.9 | 49.6 | $-3527.52 | -9.9% | $-2527.52 | -5.9 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5634 | 48.3 | 49.1 | $-2973.56 |
| ETH | 6152 | 48.3 | 48.5 | $-3722.68 |
| SOL | 6456 | 48.2 | 48.6 | $-3607.01 |
| XRP | 6476 | 48.3 | 48.5 | $-3677.75 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
