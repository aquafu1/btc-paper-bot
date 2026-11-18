# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 18, 6:15 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 713 windows, 19655 settled trades, 48 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 376 | 33.8 | 34.8 | $-284.03 | -7.6% | $715.97 | -1.1 | done | can't tell from luck |
| reversal_15m_0.10pct | 2013 | 51.7 | 50.8 | $-491.48 | -2.4% | $508.52 | -1.1 | done | can't tell from luck |
| momentum_60m_0.30pct | 1652 | 50.2 | 49.5 | $-516.37 | -3.1% | $483.63 | -1.3 | done | can't tell from luck |
| value_ev10 | 906 | 38.2 | 39.0 | $-552.57 | -6.1% | $447.43 | -1.5 | done | can't tell from luck |
| value_ev5 | 1363 | 40.8 | 41.0 | $-615.69 | -4.5% | $384.31 | -1.4 | done | can't tell from luck |
| trend_filter | 1148 | 50.4 | 51.0 | $-619.46 | -5.4% | $380.54 | -1.9 | done | can't tell from luck |
| coinflip | 2844 | 50.2 | 50.3 | $-1207.89 | -4.2% | $-207.89 | -2.3 | done | losing for real |
| reversal_60m_0.30pct | 1652 | 49.8 | 51.3 | $-1259.69 | -7.6% | $-259.69 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 2844 | 51.1 | 51.8 | $-1404.19 | -4.9% | $-404.19 | -2.7 | done | losing for real |
| momentum_15m_0.10pct | 2013 | 48.3 | 50.0 | $-1448.15 | -7.2% | $-448.15 | -3.2 | done | losing for real |
| always_up | 2844 | 47.3 | 49.5 | $-2442.22 | -8.6% | $-1442.22 | -4.6 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4456 | 48.2 | 49.0 | $-2696.33 |
| ETH | 4889 | 48.4 | 48.5 | $-2787.19 |
| SOL | 5127 | 48.2 | 48.7 | $-2915.02 |
| XRP | 5183 | 48.6 | 48.4 | $-2443.20 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
