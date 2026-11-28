# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 27, 7:20 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1629 windows, 39111 settled trades, 348 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 832 | 34.4 | 35.2 | $-620.56 | -7.5% | $379.44 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 3851 | 50.8 | 50.0 | $-1014.09 | -2.6% | $-14.09 | -1.6 | done | can't tell from luck |
| value_ev10 | 1961 | 38.3 | 39.0 | $-1113.90 | -5.7% | $-113.90 | -2.1 | done | losing for real |
| reversal_60m_0.30pct | 3222 | 51.0 | 50.9 | $-1499.85 | -4.7% | $-499.85 | -2.7 | done | losing for real |
| value_ev5 | 2931 | 40.4 | 41.0 | $-1546.44 | -5.3% | $-546.44 | -2.4 | done | losing for real |
| momentum_60m_0.30pct | 3222 | 49.0 | 49.2 | $-1738.45 | -5.4% | $-738.45 | -3.0 | done | losing for real |
| trend_filter | 2294 | 48.5 | 50.3 | $-2019.36 | -8.8% | $-1019.36 | -4.3 | done | losing for real |
| momentum_15m_0.10pct | 3851 | 49.2 | 50.2 | $-2356.42 | -6.1% | $-1356.42 | -3.8 | done | losing for real |
| coinflip | 5649 | 50.0 | 49.9 | $-2369.69 | -4.2% | $-1369.69 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 5649 | 50.2 | 51.3 | $-3429.61 | -6.1% | $-2429.61 | -4.7 | done | losing for real |
| always_up | 5649 | 48.2 | 49.1 | $-3573.03 | -6.3% | $-2573.03 | -4.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 10458 | 48.0 | 48.6 | $-5854.90 |
| ETH | 11343 | 48.0 | 47.6 | $-5842.27 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
