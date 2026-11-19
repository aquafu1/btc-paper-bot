# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 19, 1:50 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 839 windows, 23063 settled trades, 53 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 423 | 33.1 | 34.9 | $-400.80 | -9.5% | $599.20 | -1.5 | done | can't tell from luck |
| reversal_15m_0.10pct | 2357 | 50.9 | 50.6 | $-869.92 | -3.7% | $130.08 | -1.8 | done | can't tell from luck |
| value_ev10 | 1050 | 37.2 | 39.1 | $-879.14 | -8.4% | $120.86 | -2.2 | done | losing for real |
| momentum_60m_0.30pct | 1940 | 49.8 | 49.7 | $-928.09 | -4.8% | $71.91 | -2.1 | done | losing for real |
| trend_filter | 1357 | 49.7 | 50.8 | $-980.66 | -7.2% | $19.34 | -2.7 | done | losing for real |
| value_ev5 | 1592 | 39.6 | 41.1 | $-1159.29 | -7.3% | $-159.29 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 1940 | 50.2 | 51.2 | $-1333.75 | -6.9% | $-333.75 | -3.1 | done | losing for real |
| coinflip | 3349 | 50.3 | 50.3 | $-1470.19 | -4.4% | $-470.19 | -2.6 | done | losing for real |
| momentum_15m_0.10pct | 2357 | 49.1 | 50.3 | $-1493.77 | -6.3% | $-493.77 | -3.1 | done | losing for real |
| momentum_5m_0.00pct | 3349 | 51.2 | 51.7 | $-1575.28 | -4.7% | $-575.28 | -2.8 | done | losing for real |
| always_up | 3349 | 47.2 | 49.6 | $-3105.61 | -9.3% | $-2105.61 | -5.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5239 | 48.1 | 49.1 | $-3330.55 |
| ETH | 5747 | 48.0 | 48.5 | $-3975.77 |
| SOL | 6014 | 48.2 | 48.6 | $-3513.92 |
| XRP | 6063 | 48.4 | 48.5 | $-3376.27 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
