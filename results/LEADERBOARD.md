# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 24, 12:00 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1312 windows, 34863 settled trades, 419 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 687 | 34.2 | 35.3 | $-530.82 | -7.7% | $469.18 | -1.5 | done | can't tell from luck |
| value_ev10 | 1681 | 38.8 | 39.2 | $-787.65 | -4.7% | $212.35 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 3495 | 50.9 | 50.2 | $-1012.48 | -2.9% | $-12.48 | -1.7 | done | can't tell from luck |
| value_ev5 | 2537 | 40.5 | 41.1 | $-1271.76 | -5.0% | $-271.76 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 2927 | 49.4 | 49.4 | $-1376.48 | -4.7% | $-376.48 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 2927 | 50.6 | 50.9 | $-1596.45 | -5.5% | $-596.45 | -3.0 | done | losing for real |
| trend_filter | 2072 | 48.8 | 50.5 | $-1723.54 | -8.3% | $-723.54 | -3.9 | done | losing for real |
| momentum_15m_0.10pct | 3495 | 49.1 | 50.2 | $-2207.43 | -6.3% | $-1207.43 | -3.8 | done | losing for real |
| coinflip | 5014 | 49.9 | 50.0 | $-2306.18 | -4.6% | $-1306.18 | -3.3 | done | losing for real |
| momentum_5m_0.00pct | 5014 | 50.4 | 51.4 | $-2930.07 | -5.8% | $-1930.07 | -4.3 | done | losing for real |
| always_up | 5014 | 47.9 | 49.3 | $-3618.71 | -7.2% | $-2618.71 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 8447 | 47.9 | 48.8 | $-4997.99 |
| ETH | 9106 | 48.2 | 48.2 | $-4779.34 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
