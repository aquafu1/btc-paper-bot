# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 13, 2:05 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 264 windows, 6930 settled trades, 34 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 685 | 55.3 | 52.2 | $+131.33 | +1.9% | $1131.33 | +0.5 | done | can't tell from luck |
| reversal_60m_0.30pct | 555 | 53.0 | 52.2 | $-143.41 | -2.6% | $856.59 | -0.6 | done | can't tell from luck |
| value_ev20 | 120 | 33.3 | 36.7 | $-151.51 | -12.6% | $848.49 | -1.1 | Sun 1:15 PM | too few trades (120/200) |
| value_ev10 | 330 | 36.7 | 40.8 | $-438.64 | -13.3% | $561.36 | -2.1 | done | losing for real |
| trend_filter | 361 | 46.0 | 50.3 | $-470.09 | -13.0% | $529.91 | -2.5 | done | losing for real |
| value_ev5 | 486 | 39.3 | 42.4 | $-549.55 | -11.3% | $450.45 | -2.2 | done | losing for real |
| momentum_60m_0.30pct | 555 | 47.0 | 49.8 | $-573.55 | -10.3% | $426.45 | -2.5 | done | losing for real |
| coinflip | 1051 | 49.4 | 50.8 | $-765.59 | -7.3% | $234.41 | -2.4 | done | losing for real |
| momentum_5m_0.00pct | 1051 | 49.6 | 51.5 | $-847.26 | -8.1% | $152.74 | -2.7 | done | losing for real |
| always_up | 1051 | 48.0 | 50.2 | $-908.27 | -8.6% | $91.73 | -2.9 | done | losing for real |
| momentum_15m_0.10pct | 685 | 44.7 | 49.8 | $-976.20 | -14.3% | $23.80 | -3.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1544 | 46.5 | 49.6 | $-1622.16 |
| ETH | 1729 | 46.9 | 49.1 | $-1664.62 |
| SOL | 1795 | 48.1 | 49.3 | $-1421.02 |
| XRP | 1862 | 48.9 | 49.2 | $-984.92 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
