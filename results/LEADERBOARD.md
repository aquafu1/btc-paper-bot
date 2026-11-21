# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 20, 7:35 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 958 windows, 26558 settled trades, 34 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 488 | 35.2 | 34.9 | $-139.50 | -2.9% | $860.50 | -0.5 | done | can't tell from luck |
| value_ev10 | 1207 | 38.3 | 39.1 | $-624.27 | -5.2% | $375.73 | -1.5 | done | can't tell from luck |
| reversal_15m_0.10pct | 2713 | 51.3 | 50.6 | $-712.88 | -2.6% | $287.12 | -1.4 | done | can't tell from luck |
| momentum_60m_0.30pct | 2268 | 50.1 | 49.7 | $-881.20 | -3.9% | $118.80 | -1.8 | done | can't tell from luck |
| value_ev5 | 1832 | 40.0 | 41.0 | $-1004.11 | -5.5% | $-4.11 | -2.0 | done | can't tell from luck |
| trend_filter | 1588 | 49.9 | 50.8 | $-1045.59 | -6.6% | $-45.59 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 2268 | 49.9 | 51.0 | $-1615.40 | -7.1% | $-615.40 | -3.5 | done | losing for real |
| coinflip | 3827 | 50.2 | 50.4 | $-1764.24 | -4.6% | $-764.24 | -2.9 | done | losing for real |
| momentum_15m_0.10pct | 2713 | 48.7 | 50.2 | $-1923.92 | -7.1% | $-923.92 | -3.7 | done | losing for real |
| momentum_5m_0.00pct | 3827 | 50.8 | 51.5 | $-2002.68 | -5.2% | $-1002.68 | -3.3 | done | losing for real |
| always_up | 3827 | 46.9 | 49.6 | $-3784.30 | -9.9% | $-2784.30 | -6.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6054 | 48.1 | 49.0 | $-3464.25 |
| ETH | 6598 | 48.2 | 48.5 | $-4004.05 |
| SOL | 6934 | 48.2 | 48.6 | $-3835.98 |
| XRP | 6972 | 48.2 | 48.5 | $-4193.82 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
