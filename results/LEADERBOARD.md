# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 14, 3:50 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 367 windows, 9935 settled trades, 46 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 189 | 38.1 | 36.4 | $+15.78 | +0.8% | $1015.78 | +0.1 | Sat 9:30 PM | too few trades (189/200) |
| value_ev10 | 483 | 41.2 | 40.4 | $-66.39 | -1.4% | $933.61 | -0.2 | done | can't tell from luck |
| value_ev5 | 713 | 42.5 | 42.1 | $-186.26 | -2.6% | $813.74 | -0.6 | done | can't tell from luck |
| momentum_60m_0.30pct | 819 | 49.3 | 49.7 | $-409.36 | -5.0% | $590.64 | -1.4 | done | can't tell from luck |
| trend_filter | 552 | 48.7 | 50.5 | $-423.22 | -7.7% | $576.78 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 987 | 51.6 | 52.1 | $-492.29 | -5.0% | $507.71 | -1.7 | done | can't tell from luck |
| reversal_60m_0.30pct | 819 | 50.7 | 52.1 | $-530.18 | -6.5% | $469.82 | -1.9 | done | can't tell from luck |
| momentum_15m_0.10pct | 987 | 48.4 | 49.6 | $-579.19 | -5.9% | $420.81 | -1.8 | done | can't tell from luck |
| coinflip | 1462 | 49.9 | 50.8 | $-775.81 | -5.3% | $224.19 | -2.1 | done | losing for real |
| momentum_5m_0.00pct | 1462 | 49.5 | 51.6 | $-1070.53 | -7.3% | $-70.53 | -2.9 | done | losing for real |
| always_up | 1462 | 45.8 | 50.7 | $-1940.48 | -13.3% | $-940.48 | -5.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2228 | 47.3 | 49.3 | $-1751.00 |
| ETH | 2503 | 47.7 | 48.9 | $-1729.01 |
| SOL | 2570 | 48.1 | 49.4 | $-1752.62 |
| XRP | 2634 | 48.9 | 49.1 | $-1225.31 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
