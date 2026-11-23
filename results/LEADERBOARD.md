# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 23, 3:50 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1231 windows, 33635 settled trades, 420 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 660 | 34.4 | 35.3 | $-474.16 | -7.2% | $525.84 | -1.4 | done | can't tell from luck |
| value_ev10 | 1610 | 38.7 | 39.2 | $-797.71 | -5.0% | $202.29 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 3371 | 50.8 | 50.3 | $-1092.97 | -3.2% | $-92.97 | -1.9 | done | can't tell from luck |
| value_ev5 | 2431 | 40.5 | 41.1 | $-1224.50 | -5.0% | $-224.50 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 2822 | 49.5 | 49.4 | $-1281.06 | -4.5% | $-281.06 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 2822 | 50.5 | 51.1 | $-1671.62 | -5.9% | $-671.62 | -3.2 | done | losing for real |
| trend_filter | 1989 | 48.7 | 50.4 | $-1681.43 | -8.5% | $-681.43 | -3.9 | done | losing for real |
| momentum_15m_0.10pct | 3371 | 49.2 | 50.2 | $-2083.75 | -6.2% | $-1083.75 | -3.6 | done | losing for real |
| coinflip | 4853 | 50.0 | 50.1 | $-2205.82 | -4.5% | $-1205.82 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 4853 | 50.3 | 51.4 | $-2939.47 | -6.1% | $-1939.47 | -4.3 | done | losing for real |
| always_up | 4853 | 47.8 | 49.3 | $-3572.97 | -7.4% | $-2572.97 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7853 | 48.0 | 48.9 | $-4566.88 |
| ETH | 8472 | 48.1 | 48.3 | $-4874.35 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
