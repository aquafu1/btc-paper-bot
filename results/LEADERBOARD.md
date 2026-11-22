# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 22, 6:50 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1099 windows, 30411 settled trades, 62 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 577 | 34.7 | 35.0 | $-321.49 | -5.6% | $678.51 | -1.0 | done | can't tell from luck |
| value_ev10 | 1414 | 38.2 | 39.1 | $-821.09 | -5.8% | $178.91 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 3070 | 51.1 | 50.5 | $-862.21 | -2.8% | $137.79 | -1.6 | done | can't tell from luck |
| momentum_60m_0.30pct | 2584 | 49.7 | 49.4 | $-1120.95 | -4.3% | $-120.95 | -2.2 | done | losing for real |
| value_ev5 | 2145 | 40.1 | 41.0 | $-1190.70 | -5.6% | $-190.70 | -2.2 | done | losing for real |
| trend_filter | 1800 | 49.3 | 50.5 | $-1327.14 | -7.4% | $-327.14 | -3.2 | done | losing for real |
| reversal_60m_0.30pct | 2584 | 50.3 | 51.1 | $-1628.29 | -6.3% | $-628.29 | -3.3 | done | losing for real |
| coinflip | 4389 | 50.5 | 50.2 | $-1661.89 | -3.8% | $-661.89 | -2.5 | done | losing for real |
| momentum_15m_0.10pct | 3070 | 48.9 | 50.2 | $-2008.77 | -6.5% | $-1008.77 | -3.7 | done | losing for real |
| momentum_5m_0.00pct | 4389 | 50.8 | 51.4 | $-2251.43 | -5.1% | $-1251.43 | -3.5 | done | losing for real |
| always_up | 4389 | 47.5 | 49.3 | $-3502.68 | -8.0% | $-2502.68 | -5.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6967 | 48.4 | 49.0 | $-3379.79 |
| ETH | 7531 | 48.2 | 48.4 | $-4427.56 |
| SOL | 7914 | 48.1 | 48.4 | $-4342.43 |
| XRP | 7999 | 48.2 | 48.2 | $-4546.86 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
