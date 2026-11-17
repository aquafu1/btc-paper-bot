# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 17, 2:35 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 650 windows, 17965 settled trades, 53 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 339 | 34.5 | 35.3 | $-227.49 | -6.7% | $772.51 | -0.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 1515 | 50.6 | 49.6 | $-347.95 | -2.3% | $652.05 | -0.9 | done | can't tell from luck |
| value_ev10 | 829 | 38.5 | 39.5 | $-550.22 | -6.6% | $449.78 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 1847 | 51.5 | 51.0 | $-559.49 | -3.0% | $440.51 | -1.3 | done | can't tell from luck |
| value_ev5 | 1255 | 41.0 | 41.4 | $-605.58 | -4.8% | $394.42 | -1.5 | done | can't tell from luck |
| trend_filter | 1039 | 50.0 | 50.9 | $-628.38 | -6.0% | $371.62 | -2.0 | done | can't tell from luck |
| coinflip | 2593 | 50.1 | 50.5 | $-1174.84 | -4.5% | $-174.84 | -2.3 | done | losing for real |
| reversal_60m_0.30pct | 1515 | 49.4 | 51.4 | $-1251.98 | -8.3% | $-251.98 | -3.3 | done | losing for real |
| momentum_15m_0.10pct | 1847 | 48.5 | 50.0 | $-1265.75 | -6.9% | $-265.75 | -3.0 | done | losing for real |
| momentum_5m_0.00pct | 2593 | 50.4 | 51.7 | $-1551.87 | -6.0% | $-551.87 | -3.2 | done | losing for real |
| always_up | 2593 | 47.4 | 49.7 | $-2192.81 | -8.5% | $-1192.81 | -4.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4070 | 48.3 | 49.3 | $-2438.91 |
| ETH | 4483 | 48.2 | 48.7 | $-2681.99 |
| SOL | 4673 | 48.0 | 48.8 | $-2864.92 |
| XRP | 4739 | 48.4 | 48.6 | $-2370.56 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
