# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 22, 12:00 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1072 windows, 29656 settled trades, 68 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 553 | 34.4 | 35.1 | $-343.30 | -6.2% | $656.70 | -1.1 | done | can't tell from luck |
| reversal_15m_0.10pct | 3005 | 51.3 | 50.5 | $-761.69 | -2.5% | $238.31 | -1.4 | done | can't tell from luck |
| value_ev10 | 1368 | 37.6 | 39.2 | $-969.47 | -7.1% | $30.53 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 2520 | 49.8 | 49.6 | $-1071.47 | -4.3% | $-71.47 | -2.1 | done | losing for real |
| trend_filter | 1765 | 49.6 | 50.7 | $-1236.23 | -7.0% | $-236.23 | -3.0 | done | losing for real |
| value_ev5 | 2080 | 39.7 | 41.0 | $-1347.46 | -6.5% | $-347.46 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 2520 | 50.2 | 51.0 | $-1666.19 | -6.6% | $-666.19 | -3.4 | done | losing for real |
| coinflip | 4280 | 50.5 | 50.3 | $-1684.85 | -3.9% | $-684.85 | -2.6 | done | losing for real |
| momentum_5m_0.00pct | 4280 | 51.0 | 51.5 | $-2077.48 | -4.9% | $-1077.48 | -3.3 | done | losing for real |
| momentum_15m_0.10pct | 3005 | 48.7 | 50.3 | $-2124.40 | -7.1% | $-1124.40 | -3.9 | done | losing for real |
| always_up | 4280 | 47.1 | 49.4 | $-3849.80 | -9.0% | $-2849.80 | -5.9 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6766 | 48.4 | 49.0 | $-3452.77 |
| ETH | 7337 | 48.1 | 48.5 | $-4613.19 |
| SOL | 7735 | 48.1 | 48.5 | $-4483.65 |
| XRP | 7818 | 48.2 | 48.3 | $-4582.72 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
