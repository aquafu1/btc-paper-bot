# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 25, 10:50 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1451 windows, 36811 settled trades, 369 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 744 | 34.3 | 35.3 | $-573.47 | -7.7% | $426.53 | -1.6 | done | can't tell from luck |
| value_ev10 | 1794 | 38.6 | 39.2 | $-886.32 | -4.9% | $113.68 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 3670 | 50.9 | 50.0 | $-990.09 | -2.7% | $9.91 | -1.6 | done | can't tell from luck |
| value_ev5 | 2701 | 40.4 | 41.1 | $-1381.66 | -5.1% | $-381.66 | -2.3 | done | losing for real |
| momentum_60m_0.30pct | 3083 | 49.2 | 49.3 | $-1519.82 | -4.9% | $-519.82 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 3083 | 50.8 | 51.0 | $-1589.67 | -5.2% | $-589.67 | -2.9 | done | losing for real |
| trend_filter | 2184 | 48.6 | 50.3 | $-1867.56 | -8.6% | $-867.56 | -4.1 | done | losing for real |
| momentum_15m_0.10pct | 3670 | 49.1 | 50.2 | $-2281.05 | -6.2% | $-1281.05 | -3.8 | done | losing for real |
| coinflip | 5294 | 50.0 | 50.0 | $-2282.32 | -4.3% | $-1282.32 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 5294 | 50.1 | 51.3 | $-3322.09 | -6.3% | $-2322.09 | -4.7 | done | losing for real |
| always_up | 5294 | 48.0 | 49.2 | $-3546.84 | -6.7% | $-2546.84 | -4.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 9403 | 48.0 | 48.7 | $-5079.63 |
| ETH | 10098 | 48.0 | 48.0 | $-5577.02 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
