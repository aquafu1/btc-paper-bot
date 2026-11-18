# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 17, 11:05 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 684 windows, 18915 settled trades, 51 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 356 | 34.3 | 35.0 | $-234.96 | -6.6% | $765.04 | -0.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 1599 | 50.3 | 49.5 | $-438.83 | -2.7% | $561.17 | -1.1 | done | can't tell from luck |
| value_ev10 | 872 | 38.4 | 39.2 | $-516.96 | -5.9% | $483.04 | -1.4 | done | can't tell from luck |
| reversal_15m_0.10pct | 1944 | 51.6 | 50.9 | $-575.02 | -3.0% | $424.98 | -1.3 | done | can't tell from luck |
| trend_filter | 1101 | 50.2 | 50.8 | $-601.27 | -5.5% | $398.73 | -1.8 | done | can't tell from luck |
| value_ev5 | 1313 | 40.7 | 41.2 | $-643.26 | -4.9% | $356.74 | -1.5 | done | can't tell from luck |
| coinflip | 2729 | 50.1 | 50.4 | $-1225.11 | -4.5% | $-225.11 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 1599 | 49.7 | 51.4 | $-1238.41 | -7.7% | $-238.41 | -3.2 | done | losing for real |
| momentum_15m_0.10pct | 1944 | 48.4 | 49.9 | $-1336.73 | -6.9% | $-336.73 | -3.0 | done | losing for real |
| momentum_5m_0.00pct | 2729 | 50.8 | 51.8 | $-1486.84 | -5.4% | $-486.84 | -2.9 | done | losing for real |
| always_up | 2729 | 47.3 | 49.6 | $-2406.24 | -8.8% | $-1406.24 | -4.6 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4295 | 48.2 | 49.2 | $-2569.82 |
| ETH | 4710 | 48.2 | 48.6 | $-2848.93 |
| SOL | 4932 | 48.1 | 48.6 | $-2959.49 |
| XRP | 4978 | 48.5 | 48.4 | $-2325.41 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
