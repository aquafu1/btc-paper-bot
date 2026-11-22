# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 22, 11:35 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1118 windows, 30967 settled trades, 27 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 591 | 34.5 | 35.1 | $-359.77 | -6.1% | $640.23 | -1.1 | done | can't tell from luck |
| reversal_15m_0.10pct | 3123 | 51.2 | 50.5 | $-814.31 | -2.6% | $185.69 | -1.5 | done | can't tell from luck |
| value_ev10 | 1447 | 38.1 | 39.2 | $-876.97 | -6.1% | $123.03 | -1.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 2627 | 49.7 | 49.4 | $-1097.73 | -4.2% | $-97.73 | -2.1 | done | losing for real |
| value_ev5 | 2189 | 40.1 | 41.0 | $-1232.09 | -5.6% | $-232.09 | -2.2 | done | losing for real |
| trend_filter | 1836 | 49.1 | 50.4 | $-1411.61 | -7.7% | $-411.61 | -3.4 | done | losing for real |
| reversal_60m_0.30pct | 2627 | 50.3 | 51.1 | $-1686.10 | -6.4% | $-686.10 | -3.4 | done | losing for real |
| coinflip | 4468 | 50.4 | 50.2 | $-1791.11 | -4.0% | $-791.11 | -2.7 | done | losing for real |
| momentum_15m_0.10pct | 3123 | 48.8 | 50.2 | $-2092.07 | -6.7% | $-1092.07 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 4468 | 50.4 | 51.4 | $-2570.25 | -5.8% | $-1570.25 | -4.0 | done | losing for real |
| always_up | 4468 | 47.7 | 49.3 | $-3408.36 | -7.6% | $-2408.36 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7096 | 48.4 | 49.0 | $-3602.88 |
| ETH | 7672 | 48.1 | 48.4 | $-4646.61 |
| SOL | 8055 | 48.0 | 48.4 | $-4527.41 |
| XRP | 8144 | 48.2 | 48.2 | $-4563.49 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
