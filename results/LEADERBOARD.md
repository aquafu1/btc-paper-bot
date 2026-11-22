# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 22, 5:50 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1143 windows, 31602 settled trades, 36 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 609 | 34.5 | 35.2 | $-402.50 | -6.6% | $597.50 | -1.2 | done | can't tell from luck |
| value_ev10 | 1484 | 38.0 | 39.2 | $-976.39 | -6.6% | $23.61 | -2.1 | done | losing for real |
| reversal_15m_0.10pct | 3177 | 50.9 | 50.4 | $-986.31 | -3.1% | $13.69 | -1.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 2667 | 49.6 | 49.5 | $-1179.37 | -4.4% | $-179.37 | -2.3 | done | losing for real |
| value_ev5 | 2243 | 40.0 | 41.1 | $-1359.10 | -6.1% | $-359.10 | -2.4 | done | losing for real |
| trend_filter | 1877 | 49.0 | 50.5 | $-1510.99 | -8.1% | $-510.99 | -3.6 | done | losing for real |
| reversal_60m_0.30pct | 2667 | 50.4 | 51.1 | $-1650.98 | -6.2% | $-650.98 | -3.3 | done | losing for real |
| coinflip | 4567 | 50.3 | 50.2 | $-1878.49 | -4.1% | $-878.49 | -2.8 | done | losing for real |
| momentum_15m_0.10pct | 3177 | 49.1 | 50.2 | $-1984.61 | -6.2% | $-984.61 | -3.6 | done | losing for real |
| momentum_5m_0.00pct | 4567 | 50.2 | 51.4 | $-2858.46 | -6.3% | $-1858.46 | -4.4 | done | losing for real |
| always_up | 4567 | 47.9 | 49.4 | $-3371.00 | -7.4% | $-2371.00 | -5.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7243 | 48.3 | 49.0 | $-3825.51 |
| ETH | 7833 | 48.1 | 48.4 | $-4680.18 |
| SOL | 8230 | 48.1 | 48.4 | $-4608.46 |
| XRP | 8296 | 48.1 | 48.3 | $-5044.05 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
