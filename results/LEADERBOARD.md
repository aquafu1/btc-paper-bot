# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 23, 8:20 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1249 windows, 33879 settled trades, 412 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 664 | 34.2 | 35.3 | $-514.16 | -7.7% | $485.84 | -1.5 | done | can't tell from luck |
| value_ev10 | 1624 | 38.4 | 39.2 | $-900.67 | -5.5% | $99.33 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 3396 | 50.8 | 50.3 | $-1090.81 | -3.2% | $-90.81 | -1.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 2840 | 49.4 | 49.4 | $-1342.61 | -4.7% | $-342.61 | -2.5 | done | losing for real |
| value_ev5 | 2453 | 40.2 | 41.1 | $-1364.24 | -5.6% | $-364.24 | -2.3 | done | losing for real |
| reversal_60m_0.30pct | 2840 | 50.6 | 51.1 | $-1643.74 | -5.8% | $-643.74 | -3.2 | done | losing for real |
| trend_filter | 2002 | 48.7 | 50.4 | $-1710.75 | -8.5% | $-710.75 | -3.9 | done | losing for real |
| momentum_15m_0.10pct | 3396 | 49.2 | 50.2 | $-2122.57 | -6.3% | $-1122.57 | -3.7 | done | losing for real |
| coinflip | 4888 | 50.0 | 50.1 | $-2213.65 | -4.5% | $-1213.65 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 4888 | 50.3 | 51.4 | $-2938.36 | -6.0% | $-1938.36 | -4.3 | done | losing for real |
| always_up | 4888 | 47.9 | 49.3 | $-3605.90 | -7.4% | $-2605.90 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7968 | 47.9 | 48.9 | $-4813.19 |
| ETH | 8601 | 48.1 | 48.3 | $-5050.06 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
