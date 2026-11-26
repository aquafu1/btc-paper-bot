# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 25, 11:20 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1453 windows, 36832 settled trades, 354 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 746 | 34.2 | 35.4 | $-593.47 | -8.0% | $406.53 | -1.7 | done | can't tell from luck |
| value_ev10 | 1796 | 38.6 | 39.2 | $-906.32 | -5.0% | $93.68 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 3670 | 50.9 | 50.0 | $-990.09 | -2.7% | $9.91 | -1.6 | done | can't tell from luck |
| value_ev5 | 2703 | 40.4 | 41.1 | $-1401.66 | -5.2% | $-401.66 | -2.3 | done | losing for real |
| momentum_60m_0.30pct | 3086 | 49.2 | 49.3 | $-1549.82 | -5.0% | $-549.82 | -2.8 | done | losing for real |
| reversal_60m_0.30pct | 3086 | 50.8 | 51.0 | $-1563.10 | -5.1% | $-563.10 | -2.9 | done | losing for real |
| trend_filter | 2184 | 48.6 | 50.3 | $-1867.56 | -8.6% | $-867.56 | -4.1 | done | losing for real |
| coinflip | 5297 | 50.0 | 50.0 | $-2255.75 | -4.3% | $-1255.75 | -3.1 | done | losing for real |
| momentum_15m_0.10pct | 3670 | 49.1 | 50.2 | $-2281.05 | -6.2% | $-1281.05 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 5297 | 50.1 | 51.3 | $-3295.52 | -6.2% | $-2295.52 | -4.7 | done | losing for real |
| always_up | 5297 | 48.0 | 49.2 | $-3576.84 | -6.8% | $-2576.84 | -4.9 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 9416 | 48.0 | 48.7 | $-5099.63 |
| ETH | 10106 | 48.0 | 48.0 | $-5597.32 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
