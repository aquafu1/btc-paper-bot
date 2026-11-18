# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 17, 11:15 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 685 windows, 18937 settled trades, 67 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 357 | 34.5 | 35.0 | $-211.04 | -5.9% | $788.96 | -0.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 1600 | 50.3 | 49.5 | $-448.83 | -2.8% | $551.17 | -1.1 | done | can't tell from luck |
| value_ev10 | 873 | 38.5 | 39.2 | $-493.04 | -5.6% | $506.96 | -1.4 | done | can't tell from luck |
| reversal_15m_0.10pct | 1947 | 51.7 | 50.9 | $-518.51 | -2.7% | $481.49 | -1.2 | done | can't tell from luck |
| value_ev5 | 1314 | 40.8 | 41.1 | $-619.34 | -4.7% | $380.66 | -1.4 | done | can't tell from luck |
| trend_filter | 1103 | 50.1 | 50.9 | $-621.27 | -5.6% | $378.73 | -1.9 | done | can't tell from luck |
| coinflip | 2732 | 50.1 | 50.3 | $-1196.65 | -4.4% | $-196.65 | -2.3 | done | losing for real |
| reversal_60m_0.30pct | 1600 | 49.7 | 51.3 | $-1223.87 | -7.6% | $-223.87 | -3.1 | done | losing for real |
| momentum_15m_0.10pct | 1947 | 48.3 | 49.9 | $-1366.73 | -7.0% | $-366.73 | -3.1 | done | losing for real |
| momentum_5m_0.00pct | 2732 | 50.7 | 51.8 | $-1516.84 | -5.6% | $-516.84 | -3.0 | done | losing for real |
| always_up | 2732 | 47.4 | 49.6 | $-2349.73 | -8.6% | $-1349.73 | -4.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4304 | 48.3 | 49.1 | $-2456.34 |
| ETH | 4718 | 48.2 | 48.6 | $-2830.74 |
| SOL | 4937 | 48.1 | 48.6 | $-2953.38 |
| XRP | 4978 | 48.5 | 48.4 | $-2325.41 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
