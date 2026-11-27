# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 27, 5:00 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1620 windows, 38991 settled trades, 351 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 824 | 34.2 | 35.2 | $-651.33 | -7.9% | $348.67 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 3845 | 50.9 | 50.0 | $-994.52 | -2.6% | $5.48 | -1.6 | done | can't tell from luck |
| value_ev10 | 1951 | 38.3 | 39.0 | $-1124.66 | -5.8% | $-124.66 | -2.1 | done | losing for real |
| reversal_60m_0.30pct | 3216 | 51.1 | 50.9 | $-1470.99 | -4.6% | $-470.99 | -2.7 | done | losing for real |
| value_ev5 | 2918 | 40.3 | 41.0 | $-1564.04 | -5.4% | $-564.04 | -2.5 | done | losing for real |
| momentum_60m_0.30pct | 3216 | 48.9 | 49.2 | $-1750.53 | -5.4% | $-750.53 | -3.1 | done | losing for real |
| trend_filter | 2286 | 48.5 | 50.4 | $-2048.85 | -9.0% | $-1048.85 | -4.4 | done | losing for real |
| coinflip | 5630 | 50.1 | 49.9 | $-2315.79 | -4.1% | $-1315.79 | -3.1 | done | losing for real |
| momentum_15m_0.10pct | 3845 | 49.1 | 50.2 | $-2384.56 | -6.2% | $-1384.56 | -3.9 | done | losing for real |
| momentum_5m_0.00pct | 5630 | 50.2 | 51.3 | $-3471.91 | -6.2% | $-2471.91 | -4.8 | done | losing for real |
| always_up | 5630 | 48.1 | 49.1 | $-3655.75 | -6.5% | $-2655.75 | -4.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 10410 | 47.9 | 48.6 | $-5909.87 |
| ETH | 11271 | 47.9 | 47.7 | $-5938.82 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
