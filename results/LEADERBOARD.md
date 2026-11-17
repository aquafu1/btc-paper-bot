# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 17, 5:30 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 614 windows, 16959 settled trades, 60 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1431 | 51.1 | 49.7 | $-240.23 | -1.7% | $759.77 | -0.6 | done | can't tell from luck |
| value_ev20 | 327 | 34.3 | 35.2 | $-244.70 | -7.5% | $755.30 | -1.0 | done | can't tell from luck |
| trend_filter | 978 | 50.2 | 51.0 | $-576.92 | -5.9% | $423.08 | -1.9 | done | can't tell from luck |
| value_ev10 | 790 | 38.1 | 39.4 | $-581.87 | -7.4% | $418.13 | -1.7 | done | can't tell from luck |
| value_ev5 | 1192 | 40.3 | 41.3 | $-764.88 | -6.4% | $235.12 | -1.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 1733 | 50.8 | 50.9 | $-774.83 | -4.5% | $225.17 | -1.9 | done | can't tell from luck |
| momentum_15m_0.10pct | 1733 | 49.2 | 50.1 | $-1007.85 | -5.8% | $-7.85 | -2.4 | done | losing for real |
| coinflip | 2448 | 50.1 | 50.5 | $-1195.00 | -4.9% | $-195.00 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 1431 | 48.9 | 51.3 | $-1316.34 | -9.2% | $-316.34 | -3.6 | done | losing for real |
| momentum_5m_0.00pct | 2448 | 50.3 | 51.8 | $-1589.35 | -6.5% | $-589.35 | -3.3 | done | losing for real |
| always_up | 2448 | 47.0 | 49.8 | $-2351.20 | -9.6% | $-1351.20 | -4.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3855 | 48.0 | 49.2 | $-2572.49 |
| ETH | 4243 | 48.0 | 48.6 | $-2799.74 |
| SOL | 4402 | 47.9 | 48.8 | $-2945.22 |
| XRP | 4459 | 48.5 | 48.6 | $-2325.72 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
