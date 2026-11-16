# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 16, 4:45 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 563 windows, 15603 settled trades, 58 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1327 | 51.2 | 49.7 | $-256.30 | -1.9% | $743.70 | -0.7 | done | can't tell from luck |
| value_ev20 | 306 | 33.0 | 35.2 | $-355.92 | -11.6% | $644.08 | -1.6 | done | can't tell from luck |
| trend_filter | 904 | 50.6 | 51.1 | $-502.43 | -5.6% | $497.57 | -1.7 | done | can't tell from luck |
| value_ev10 | 741 | 37.5 | 39.4 | $-706.41 | -9.5% | $293.59 | -2.2 | done | losing for real |
| momentum_15m_0.10pct | 1582 | 49.4 | 49.8 | $-819.74 | -5.2% | $180.26 | -2.1 | done | losing for real |
| value_ev5 | 1102 | 39.7 | 41.2 | $-901.53 | -8.2% | $98.47 | -2.3 | done | losing for real |
| reversal_15m_0.10pct | 1582 | 50.6 | 51.1 | $-943.09 | -6.0% | $56.91 | -2.4 | done | losing for real |
| coinflip | 2244 | 49.9 | 50.5 | $-1259.86 | -5.6% | $-259.86 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 1327 | 48.8 | 51.2 | $-1293.90 | -9.8% | $-293.90 | -3.7 | done | losing for real |
| momentum_5m_0.00pct | 2244 | 50.4 | 51.9 | $-1538.71 | -6.9% | $-538.71 | -3.4 | done | losing for real |
| always_up | 2244 | 47.2 | 49.9 | $-2235.56 | -10.0% | $-1235.56 | -4.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3528 | 47.6 | 49.2 | $-2716.15 |
| ETH | 3888 | 47.9 | 48.6 | $-2753.51 |
| SOL | 4074 | 47.8 | 48.7 | $-3023.46 |
| XRP | 4113 | 48.5 | 48.6 | $-2320.33 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
