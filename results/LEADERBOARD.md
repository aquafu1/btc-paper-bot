# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 14, 6:45 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 379 windows, 10311 settled trades, 57 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 196 | 37.2 | 36.6 | $-26.95 | -1.4% | $973.05 | -0.1 | Sat 8:45 PM | too few trades (196/200) |
| value_ev10 | 501 | 39.9 | 40.5 | $-219.12 | -4.4% | $780.88 | -0.8 | done | can't tell from luck |
| value_ev5 | 740 | 41.5 | 42.1 | $-362.45 | -4.9% | $637.55 | -1.1 | done | can't tell from luck |
| momentum_60m_0.30pct | 860 | 49.7 | 49.7 | $-386.52 | -4.5% | $613.48 | -1.3 | done | can't tell from luck |
| trend_filter | 572 | 48.6 | 50.4 | $-462.00 | -8.1% | $538.00 | -2.0 | done | can't tell from luck |
| reversal_15m_0.10pct | 1029 | 51.6 | 52.2 | $-529.29 | -5.1% | $470.71 | -1.7 | done | can't tell from luck |
| momentum_15m_0.10pct | 1029 | 48.4 | 49.6 | $-617.96 | -6.0% | $382.04 | -1.9 | done | can't tell from luck |
| reversal_60m_0.30pct | 860 | 50.3 | 52.1 | $-624.32 | -7.3% | $375.68 | -2.2 | done | losing for real |
| coinflip | 1508 | 49.8 | 50.8 | $-849.87 | -5.6% | $150.13 | -2.2 | done | losing for real |
| momentum_5m_0.00pct | 1508 | 49.5 | 51.5 | $-1129.49 | -7.5% | $-129.49 | -3.0 | done | losing for real |
| always_up | 1508 | 45.9 | 50.8 | $-1983.02 | -13.2% | $-983.02 | -5.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2322 | 47.4 | 49.4 | $-1792.70 |
| ETH | 2593 | 47.6 | 48.9 | $-1886.23 |
| SOL | 2671 | 47.8 | 49.4 | $-2034.71 |
| XRP | 2725 | 48.6 | 49.1 | $-1477.35 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
