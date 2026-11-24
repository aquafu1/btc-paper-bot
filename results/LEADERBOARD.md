# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 24, 2:35 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1322 windows, 35012 settled trades, 416 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 689 | 34.4 | 35.3 | $-497.07 | -7.2% | $502.93 | -1.4 | done | can't tell from luck |
| value_ev10 | 1689 | 38.8 | 39.2 | $-769.05 | -4.6% | $230.95 | -1.5 | done | can't tell from luck |
| reversal_15m_0.10pct | 3508 | 50.8 | 50.2 | $-1047.39 | -3.0% | $-47.39 | -1.8 | done | can't tell from luck |
| value_ev5 | 2547 | 40.5 | 41.1 | $-1246.98 | -4.9% | $-246.98 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 2942 | 49.4 | 49.4 | $-1407.12 | -4.8% | $-407.12 | -2.6 | done | losing for real |
| reversal_60m_0.30pct | 2942 | 50.6 | 50.9 | $-1564.71 | -5.3% | $-564.71 | -2.9 | done | losing for real |
| trend_filter | 2085 | 48.7 | 50.5 | $-1773.38 | -8.5% | $-773.38 | -4.0 | done | losing for real |
| momentum_15m_0.10pct | 3508 | 49.2 | 50.2 | $-2171.57 | -6.2% | $-1171.57 | -3.7 | done | losing for real |
| coinflip | 5034 | 49.9 | 50.0 | $-2365.21 | -4.7% | $-1365.21 | -3.4 | done | losing for real |
| momentum_5m_0.00pct | 5034 | 50.3 | 51.4 | $-2993.33 | -5.9% | $-1993.33 | -4.3 | done | losing for real |
| always_up | 5034 | 47.8 | 49.3 | $-3697.54 | -7.3% | $-2697.54 | -5.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 8519 | 47.9 | 48.8 | $-5122.77 |
| ETH | 9183 | 48.2 | 48.2 | $-4826.34 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
