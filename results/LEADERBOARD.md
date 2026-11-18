# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 18, 1:05 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 692 windows, 19142 settled trades, 49 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 368 | 34.0 | 34.9 | $-262.42 | -7.1% | $737.58 | -1.0 | done | can't tell from luck |
| momentum_60m_0.30pct | 1616 | 50.4 | 49.5 | $-438.74 | -2.7% | $561.26 | -1.1 | done | can't tell from luck |
| value_ev10 | 888 | 38.2 | 39.1 | $-558.58 | -6.3% | $441.42 | -1.5 | done | can't tell from luck |
| trend_filter | 1116 | 50.4 | 50.9 | $-581.78 | -5.2% | $418.22 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 1963 | 51.3 | 50.8 | $-635.09 | -3.2% | $364.91 | -1.4 | done | can't tell from luck |
| value_ev5 | 1332 | 40.6 | 41.1 | $-668.70 | -5.0% | $331.30 | -1.6 | done | can't tell from luck |
| reversal_60m_0.30pct | 1616 | 49.6 | 51.3 | $-1267.86 | -7.8% | $-267.86 | -3.2 | done | losing for real |
| coinflip | 2760 | 50.0 | 50.2 | $-1270.92 | -4.6% | $-270.92 | -2.4 | done | losing for real |
| momentum_15m_0.10pct | 1963 | 48.7 | 50.0 | $-1283.72 | -6.5% | $-283.72 | -2.9 | done | losing for real |
| momentum_5m_0.00pct | 2760 | 50.8 | 51.8 | $-1538.42 | -5.6% | $-538.42 | -3.0 | done | losing for real |
| always_up | 2760 | 47.4 | 49.6 | $-2354.43 | -8.5% | $-1354.43 | -4.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4344 | 48.2 | 49.1 | $-2553.30 |
| ETH | 4769 | 48.2 | 48.5 | $-2813.04 |
| SOL | 4988 | 48.1 | 48.6 | $-2965.21 |
| XRP | 5041 | 48.5 | 48.3 | $-2529.11 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
