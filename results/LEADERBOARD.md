# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 27, 6:45 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1579 windows, 38454 settled trades, 387 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 807 | 34.3 | 35.1 | $-601.63 | -7.5% | $398.37 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 3800 | 50.9 | 50.0 | $-971.13 | -2.6% | $28.87 | -1.6 | done | can't tell from luck |
| value_ev10 | 1907 | 38.5 | 39.0 | $-980.92 | -5.1% | $19.08 | -1.8 | done | can't tell from luck |
| value_ev5 | 2863 | 40.4 | 41.0 | $-1450.29 | -5.1% | $-450.29 | -2.3 | done | losing for real |
| reversal_60m_0.30pct | 3185 | 51.0 | 50.9 | $-1513.91 | -4.8% | $-513.91 | -2.7 | done | losing for real |
| momentum_60m_0.30pct | 3185 | 49.0 | 49.2 | $-1668.08 | -5.2% | $-668.08 | -2.9 | done | losing for real |
| trend_filter | 2263 | 48.6 | 50.3 | $-1972.39 | -8.7% | $-972.39 | -4.2 | done | losing for real |
| momentum_15m_0.10pct | 3800 | 49.1 | 50.2 | $-2359.22 | -6.2% | $-1359.22 | -3.9 | done | losing for real |
| coinflip | 5548 | 50.0 | 49.9 | $-2362.60 | -4.3% | $-1362.60 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 5548 | 50.1 | 51.3 | $-3464.24 | -6.2% | $-2464.24 | -4.8 | done | losing for real |
| always_up | 5548 | 48.2 | 49.1 | $-3557.45 | -6.4% | $-2557.45 | -4.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 10167 | 47.9 | 48.6 | $-5748.48 |
| ETH | 10977 | 48.0 | 47.7 | $-5569.16 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
