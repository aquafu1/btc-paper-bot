# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 14, 8:20 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 385 windows, 10527 settled trades, 34 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 196 | 37.2 | 36.6 | $-26.95 | -1.4% | $973.05 | -0.1 | Sat 10:30 PM | too few trades (196/200) |
| value_ev10 | 506 | 39.9 | 40.5 | $-225.02 | -4.4% | $774.98 | -0.8 | done | can't tell from luck |
| value_ev5 | 747 | 41.6 | 42.1 | $-344.11 | -4.6% | $655.89 | -1.1 | done | can't tell from luck |
| momentum_60m_0.30pct | 885 | 49.8 | 49.8 | $-389.07 | -4.4% | $610.93 | -1.3 | done | can't tell from luck |
| trend_filter | 588 | 48.5 | 50.6 | $-501.51 | -8.5% | $498.49 | -2.1 | done | losing for real |
| reversal_15m_0.10pct | 1056 | 51.2 | 52.0 | $-594.18 | -5.6% | $405.82 | -1.9 | done | can't tell from luck |
| momentum_15m_0.10pct | 1056 | 48.8 | 49.7 | $-599.32 | -5.7% | $400.68 | -1.8 | done | can't tell from luck |
| reversal_60m_0.30pct | 885 | 50.2 | 52.0 | $-668.17 | -7.5% | $331.83 | -2.4 | done | losing for real |
| coinflip | 1536 | 49.9 | 50.8 | $-832.50 | -5.4% | $167.50 | -2.2 | done | losing for real |
| momentum_5m_0.00pct | 1536 | 49.3 | 51.6 | $-1203.60 | -7.8% | $-203.60 | -3.2 | done | losing for real |
| always_up | 1536 | 45.8 | 50.7 | $-2055.92 | -13.4% | $-1055.92 | -5.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2376 | 47.4 | 49.4 | $-1843.39 |
| ETH | 2645 | 47.6 | 48.9 | $-1919.81 |
| SOL | 2726 | 47.8 | 49.5 | $-2135.94 |
| XRP | 2780 | 48.6 | 49.2 | $-1541.21 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
