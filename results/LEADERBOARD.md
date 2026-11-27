# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 27, 6:50 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1579 windows, 38463 settled trades, 378 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 807 | 34.3 | 35.1 | $-601.63 | -7.5% | $398.37 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 3800 | 50.9 | 50.0 | $-971.13 | -2.6% | $28.87 | -1.6 | done | can't tell from luck |
| value_ev10 | 1907 | 38.5 | 39.0 | $-980.92 | -5.1% | $19.08 | -1.8 | done | can't tell from luck |
| value_ev5 | 2863 | 40.4 | 41.0 | $-1450.29 | -5.1% | $-450.29 | -2.3 | done | losing for real |
| reversal_60m_0.30pct | 3186 | 51.0 | 50.9 | $-1497.76 | -4.7% | $-497.76 | -2.7 | done | losing for real |
| momentum_60m_0.30pct | 3186 | 49.0 | 49.2 | $-1678.08 | -5.3% | $-678.08 | -3.0 | done | losing for real |
| trend_filter | 2264 | 48.5 | 50.3 | $-1982.39 | -8.8% | $-982.39 | -4.3 | done | losing for real |
| coinflip | 5550 | 50.0 | 49.9 | $-2340.87 | -4.2% | $-1340.87 | -3.2 | done | losing for real |
| momentum_15m_0.10pct | 3800 | 49.1 | 50.2 | $-2359.22 | -6.2% | $-1359.22 | -3.9 | done | losing for real |
| momentum_5m_0.00pct | 5550 | 50.1 | 51.3 | $-3468.66 | -6.2% | $-2468.66 | -4.8 | done | losing for real |
| always_up | 5550 | 48.2 | 49.1 | $-3551.30 | -6.4% | $-2551.30 | -4.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 10170 | 47.9 | 48.6 | $-5747.32 |
| ETH | 10983 | 48.0 | 47.7 | $-5550.70 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
