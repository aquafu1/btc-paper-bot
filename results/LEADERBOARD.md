# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 21, 9:30 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1062 windows, 29381 settled trades, 63 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 547 | 34.6 | 35.1 | $-310.90 | -5.7% | $689.10 | -1.0 | done | can't tell from luck |
| reversal_15m_0.10pct | 2973 | 51.2 | 50.4 | $-818.64 | -2.8% | $181.36 | -1.5 | done | can't tell from luck |
| value_ev10 | 1359 | 37.7 | 39.2 | $-927.80 | -6.8% | $72.20 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 2497 | 49.8 | 49.6 | $-1119.06 | -4.5% | $-119.06 | -2.2 | done | losing for real |
| trend_filter | 1750 | 49.5 | 50.7 | $-1302.86 | -7.4% | $-302.86 | -3.2 | done | losing for real |
| value_ev5 | 2065 | 39.8 | 41.0 | $-1309.38 | -6.3% | $-309.38 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 2497 | 50.2 | 51.0 | $-1616.92 | -6.5% | $-616.92 | -3.3 | done | losing for real |
| coinflip | 4240 | 50.4 | 50.3 | $-1733.31 | -4.1% | $-733.31 | -2.7 | done | losing for real |
| momentum_15m_0.10pct | 2973 | 48.8 | 50.3 | $-2044.52 | -6.9% | $-1044.52 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 4240 | 50.8 | 51.5 | $-2209.78 | -5.2% | $-1209.78 | -3.5 | done | losing for real |
| always_up | 4240 | 47.2 | 49.4 | $-3770.00 | -8.9% | $-2770.00 | -5.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6704 | 48.4 | 49.0 | $-3439.30 |
| ETH | 7268 | 48.1 | 48.5 | $-4621.60 |
| SOL | 7667 | 48.1 | 48.5 | $-4476.73 |
| XRP | 7742 | 48.2 | 48.3 | $-4625.54 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
