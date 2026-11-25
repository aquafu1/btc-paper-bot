# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 25, 5:15 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1429 windows, 36509 settled trades, 451 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 735 | 34.6 | 35.3 | $-515.63 | -7.0% | $484.37 | -1.5 | done | can't tell from luck |
| value_ev10 | 1774 | 38.8 | 39.1 | $-813.63 | -4.6% | $186.37 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 3645 | 50.9 | 50.1 | $-1003.64 | -2.8% | $-3.64 | -1.7 | done | can't tell from luck |
| value_ev5 | 2675 | 40.6 | 41.1 | $-1288.07 | -4.8% | $-288.07 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 3062 | 49.2 | 49.3 | $-1528.56 | -5.0% | $-528.56 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 3062 | 50.8 | 51.0 | $-1548.70 | -5.1% | $-548.70 | -2.9 | done | losing for real |
| trend_filter | 2167 | 48.6 | 50.3 | $-1868.27 | -8.6% | $-868.27 | -4.1 | done | losing for real |
| coinflip | 5248 | 50.1 | 50.0 | $-2189.29 | -4.2% | $-1189.29 | -3.0 | done | losing for real |
| momentum_15m_0.10pct | 3645 | 49.1 | 50.2 | $-2255.49 | -6.2% | $-1255.49 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 5248 | 50.2 | 51.3 | $-3201.88 | -6.1% | $-2201.88 | -4.5 | done | losing for real |
| always_up | 5248 | 47.9 | 49.3 | $-3684.86 | -7.0% | $-2684.86 | -5.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 9253 | 48.1 | 48.7 | $-4921.64 |
| ETH | 9946 | 48.0 | 48.0 | $-5392.15 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
