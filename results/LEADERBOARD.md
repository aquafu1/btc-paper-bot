# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 14, 12:20 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 353 windows, 9489 settled trades, 75 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 184 | 37.5 | 36.6 | $-38.35 | -2.1% | $961.65 | -0.2 | Sat 8:15 PM | too few trades (184/200) |
| value_ev10 | 456 | 40.1 | 40.3 | $-189.48 | -4.2% | $810.52 | -0.7 | done | can't tell from luck |
| value_ev5 | 678 | 41.6 | 42.0 | $-332.85 | -4.9% | $667.15 | -1.1 | done | can't tell from luck |
| reversal_15m_0.10pct | 942 | 52.1 | 52.0 | $-380.93 | -4.0% | $619.07 | -1.3 | done | can't tell from luck |
| reversal_60m_0.30pct | 776 | 51.3 | 52.0 | $-417.17 | -5.4% | $582.83 | -1.6 | done | can't tell from luck |
| trend_filter | 523 | 48.0 | 50.4 | $-470.01 | -9.0% | $529.99 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 776 | 48.7 | 49.7 | $-494.12 | -6.4% | $505.88 | -1.8 | done | can't tell from luck |
| coinflip | 1404 | 50.1 | 50.8 | $-725.37 | -5.2% | $274.63 | -2.0 | done | can't tell from luck |
| momentum_15m_0.10pct | 942 | 47.9 | 49.7 | $-730.62 | -7.8% | $269.38 | -2.4 | done | losing for real |
| momentum_5m_0.00pct | 1404 | 49.4 | 51.5 | $-1068.56 | -7.6% | $-68.56 | -3.0 | done | losing for real |
| always_up | 1404 | 46.6 | 50.6 | $-1642.93 | -11.7% | $-642.93 | -4.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2126 | 47.3 | 49.3 | $-1707.87 |
| ETH | 2390 | 47.6 | 48.7 | $-1749.79 |
| SOL | 2460 | 48.1 | 49.4 | $-1808.93 |
| XRP | 2513 | 48.9 | 49.1 | $-1223.80 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
