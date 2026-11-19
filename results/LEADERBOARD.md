# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 19, 3:15 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 797 windows, 21929 settled trades, 51 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 406 | 33.3 | 34.9 | $-357.20 | -8.8% | $642.80 | -1.3 | done | can't tell from luck |
| value_ev10 | 1002 | 37.8 | 39.2 | $-683.31 | -6.8% | $316.69 | -1.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 1850 | 50.2 | 49.6 | $-685.56 | -3.7% | $314.44 | -1.6 | done | can't tell from luck |
| trend_filter | 1287 | 50.3 | 50.8 | $-727.79 | -5.7% | $272.21 | -2.1 | done | losing for real |
| reversal_15m_0.10pct | 2241 | 50.8 | 50.6 | $-859.23 | -3.8% | $140.77 | -1.8 | done | can't tell from luck |
| value_ev5 | 1512 | 40.1 | 41.1 | $-889.03 | -5.9% | $110.97 | -1.9 | done | can't tell from luck |
| momentum_15m_0.10pct | 2241 | 49.2 | 50.2 | $-1306.66 | -5.8% | $-306.66 | -2.8 | done | losing for real |
| reversal_60m_0.30pct | 1850 | 49.8 | 51.2 | $-1354.97 | -7.3% | $-354.97 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 3180 | 51.3 | 51.7 | $-1379.12 | -4.3% | $-379.12 | -2.5 | done | losing for real |
| coinflip | 3180 | 50.2 | 50.3 | $-1379.67 | -4.3% | $-379.67 | -2.5 | done | losing for real |
| always_up | 3180 | 47.5 | 49.6 | $-2688.96 | -8.5% | $-1688.96 | -4.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4981 | 48.3 | 49.1 | $-2883.91 |
| ETH | 5466 | 48.2 | 48.5 | $-3382.81 |
| SOL | 5715 | 48.3 | 48.6 | $-3160.89 |
| XRP | 5767 | 48.5 | 48.5 | $-2883.88 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
