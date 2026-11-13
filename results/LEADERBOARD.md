# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 13, 1:50 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 263 windows, 6907 settled trades, 26 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 685 | 55.3 | 52.2 | $+131.33 | +1.9% | $1131.33 | +0.5 | done | can't tell from luck |
| reversal_60m_0.30pct | 553 | 53.2 | 52.1 | $-123.41 | -2.2% | $876.59 | -0.6 | done | can't tell from luck |
| value_ev20 | 120 | 33.3 | 36.7 | $-151.51 | -12.6% | $848.49 | -1.1 | Sun 12:45 PM | too few trades (120/200) |
| trend_filter | 361 | 46.0 | 50.3 | $-470.09 | -13.0% | $529.91 | -2.5 | done | losing for real |
| value_ev10 | 327 | 36.1 | 40.8 | $-479.85 | -14.7% | $520.15 | -2.3 | done | losing for real |
| value_ev5 | 482 | 39.0 | 42.4 | $-580.76 | -12.0% | $419.24 | -2.3 | done | losing for real |
| momentum_60m_0.30pct | 553 | 46.8 | 49.8 | $-599.21 | -10.8% | $400.79 | -2.6 | done | losing for real |
| coinflip | 1047 | 49.4 | 50.8 | $-768.74 | -7.3% | $231.26 | -2.5 | done | losing for real |
| momentum_5m_0.00pct | 1047 | 49.7 | 51.5 | $-824.87 | -7.9% | $175.13 | -2.7 | done | losing for real |
| always_up | 1047 | 47.9 | 50.2 | $-957.08 | -9.1% | $42.92 | -3.0 | done | losing for real |
| momentum_15m_0.10pct | 685 | 44.7 | 49.8 | $-976.20 | -14.3% | $23.80 | -3.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1540 | 46.4 | 49.5 | $-1634.98 |
| ETH | 1722 | 46.9 | 49.1 | $-1690.42 |
| SOL | 1790 | 48.0 | 49.3 | $-1473.18 |
| XRP | 1855 | 48.8 | 49.2 | $-1001.79 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
