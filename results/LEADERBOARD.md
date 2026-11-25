# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 25, 7:30 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1390 windows, 35936 settled trades, 388 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 722 | 34.6 | 35.3 | $-497.54 | -6.9% | $502.46 | -1.4 | done | can't tell from luck |
| value_ev10 | 1745 | 38.9 | 39.2 | $-764.97 | -4.4% | $235.03 | -1.5 | done | can't tell from luck |
| reversal_15m_0.10pct | 3589 | 50.8 | 50.1 | $-1048.23 | -2.9% | $-48.23 | -1.7 | done | can't tell from luck |
| value_ev5 | 2627 | 40.5 | 41.1 | $-1281.48 | -4.9% | $-281.48 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 3011 | 49.3 | 49.3 | $-1490.15 | -4.9% | $-490.15 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 3011 | 50.7 | 50.9 | $-1543.13 | -5.1% | $-543.13 | -2.9 | done | losing for real |
| trend_filter | 2132 | 48.5 | 50.4 | $-1875.87 | -8.8% | $-875.87 | -4.2 | done | losing for real |
| momentum_15m_0.10pct | 3589 | 49.2 | 50.2 | $-2193.25 | -6.1% | $-1193.25 | -3.7 | done | losing for real |
| coinflip | 5170 | 50.0 | 50.0 | $-2239.69 | -4.3% | $-1239.69 | -3.1 | done | losing for real |
| momentum_5m_0.00pct | 5170 | 50.2 | 51.3 | $-3194.95 | -6.2% | $-2194.95 | -4.6 | done | losing for real |
| always_up | 5170 | 47.9 | 49.3 | $-3676.25 | -7.1% | $-2676.25 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 8971 | 48.0 | 48.8 | $-5008.64 |
| ETH | 9655 | 48.1 | 48.1 | $-5212.64 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
