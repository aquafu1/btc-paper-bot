# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 16, 2:00 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 504 windows, 13884 settled trades, 61 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 259 | 34.4 | 35.5 | $-182.41 | -7.0% | $817.59 | -0.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 1177 | 51.1 | 49.9 | $-213.79 | -1.8% | $786.21 | -0.6 | done | can't tell from luck |
| value_ev10 | 652 | 38.2 | 39.8 | $-484.00 | -7.4% | $516.00 | -1.6 | done | can't tell from luck |
| trend_filter | 817 | 49.6 | 50.7 | $-538.44 | -6.6% | $461.56 | -1.9 | done | can't tell from luck |
| momentum_15m_0.10pct | 1405 | 49.8 | 49.7 | $-554.04 | -3.9% | $445.96 | -1.5 | done | can't tell from luck |
| value_ev5 | 968 | 40.1 | 41.6 | $-687.37 | -7.1% | $312.63 | -1.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 1405 | 50.2 | 51.5 | $-945.47 | -6.7% | $54.53 | -2.6 | done | losing for real |
| coinflip | 2008 | 50.0 | 50.7 | $-1065.17 | -5.3% | $-65.17 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 1177 | 48.9 | 51.3 | $-1067.52 | -9.1% | $-67.52 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 2008 | 49.6 | 51.5 | $-1496.95 | -7.5% | $-496.95 | -3.5 | done | losing for real |
| always_up | 2008 | 46.4 | 50.2 | $-2344.13 | -11.7% | $-1344.13 | -5.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3135 | 47.4 | 49.2 | $-2478.53 |
| ETH | 3471 | 48.0 | 48.7 | $-2241.82 |
| SOL | 3622 | 47.6 | 49.1 | $-2751.65 |
| XRP | 3656 | 48.3 | 48.8 | $-2107.28 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
