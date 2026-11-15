# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 14, 6:50 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 379 windows, 10334 settled trades, 34 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 196 | 37.2 | 36.6 | $-26.95 | -1.4% | $973.05 | -0.1 | Sat 9:00 PM | too few trades (196/200) |
| value_ev10 | 503 | 40.0 | 40.5 | $-217.29 | -4.3% | $782.71 | -0.8 | done | can't tell from luck |
| value_ev5 | 742 | 41.5 | 42.1 | $-360.61 | -4.9% | $639.39 | -1.1 | done | can't tell from luck |
| momentum_60m_0.30pct | 862 | 49.8 | 49.7 | $-365.75 | -4.2% | $634.25 | -1.3 | done | can't tell from luck |
| trend_filter | 572 | 48.6 | 50.4 | $-462.00 | -8.1% | $538.00 | -2.0 | done | can't tell from luck |
| reversal_15m_0.10pct | 1032 | 51.6 | 52.2 | $-518.52 | -5.0% | $481.48 | -1.7 | done | can't tell from luck |
| momentum_15m_0.10pct | 1032 | 48.4 | 49.6 | $-630.65 | -6.1% | $369.35 | -2.0 | done | can't tell from luck |
| reversal_60m_0.30pct | 862 | 50.2 | 52.1 | $-644.32 | -7.5% | $355.68 | -2.3 | done | losing for real |
| coinflip | 1511 | 49.8 | 50.8 | $-860.94 | -5.7% | $139.06 | -2.3 | done | losing for real |
| momentum_5m_0.00pct | 1511 | 49.4 | 51.5 | $-1142.18 | -7.6% | $-142.18 | -3.0 | done | losing for real |
| always_up | 1511 | 45.9 | 50.8 | $-1972.25 | -13.1% | $-972.25 | -5.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2329 | 47.4 | 49.4 | $-1828.09 |
| ETH | 2600 | 47.6 | 48.9 | $-1880.49 |
| SOL | 2671 | 47.8 | 49.4 | $-2034.71 |
| XRP | 2734 | 48.6 | 49.1 | $-1458.17 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
