# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 22, 8:15 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1153 windows, 31845 settled trades, 55 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 614 | 34.5 | 35.2 | $-397.85 | -6.5% | $602.15 | -1.2 | done | can't tell from luck |
| value_ev10 | 1503 | 38.3 | 39.2 | $-861.63 | -5.7% | $138.37 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 3197 | 50.9 | 50.4 | $-1007.24 | -3.2% | $-7.24 | -1.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 2683 | 49.7 | 49.5 | $-1179.10 | -4.4% | $-179.10 | -2.3 | done | losing for real |
| value_ev5 | 2269 | 40.3 | 41.1 | $-1219.73 | -5.4% | $-219.73 | -2.2 | done | losing for real |
| trend_filter | 1887 | 49.0 | 50.5 | $-1523.87 | -8.1% | $-523.87 | -3.6 | done | losing for real |
| reversal_60m_0.30pct | 2683 | 50.3 | 51.0 | $-1666.85 | -6.2% | $-666.85 | -3.3 | done | losing for real |
| coinflip | 4604 | 50.2 | 50.2 | $-1923.14 | -4.2% | $-923.14 | -2.9 | done | losing for real |
| momentum_15m_0.10pct | 3197 | 49.1 | 50.2 | $-1959.43 | -6.1% | $-959.43 | -3.5 | done | losing for real |
| momentum_5m_0.00pct | 4604 | 50.1 | 51.4 | $-2926.18 | -6.4% | $-1926.18 | -4.4 | done | losing for real |
| always_up | 4604 | 47.8 | 49.3 | $-3463.43 | -7.5% | $-2463.43 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7296 | 48.3 | 49.0 | $-3759.73 |
| ETH | 7890 | 48.1 | 48.4 | $-4660.44 |
| SOL | 8286 | 48.0 | 48.4 | $-4608.51 |
| XRP | 8373 | 48.0 | 48.2 | $-5099.75 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
