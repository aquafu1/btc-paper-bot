# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 15, 3:45 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 415 windows, 11407 settled trades, 63 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 209 | 34.9 | 36.4 | $-156.95 | -7.5% | $843.05 | -0.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 976 | 51.0 | 50.1 | $-227.89 | -2.3% | $772.11 | -0.7 | done | can't tell from luck |
| value_ev10 | 535 | 39.8 | 40.4 | $-271.49 | -5.1% | $728.51 | -1.0 | done | can't tell from luck |
| trend_filter | 653 | 50.2 | 50.8 | $-332.59 | -5.1% | $667.41 | -1.3 | done | can't tell from luck |
| value_ev5 | 804 | 41.8 | 42.1 | $-370.32 | -4.6% | $629.68 | -1.1 | done | can't tell from luck |
| momentum_15m_0.10pct | 1149 | 49.3 | 49.9 | $-568.16 | -4.9% | $431.84 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 1149 | 50.7 | 51.8 | $-720.90 | -6.3% | $279.10 | -2.2 | done | losing for real |
| coinflip | 1652 | 50.2 | 50.9 | $-841.95 | -5.1% | $158.05 | -2.1 | done | losing for real |
| reversal_60m_0.30pct | 976 | 49.0 | 51.8 | $-920.83 | -9.4% | $79.17 | -3.1 | done | losing for real |
| momentum_5m_0.00pct | 1652 | 49.8 | 51.6 | $-1141.20 | -6.9% | $-141.20 | -2.9 | done | losing for real |
| always_up | 1652 | 45.9 | 50.7 | $-2118.07 | -12.8% | $-1118.07 | -5.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2580 | 47.8 | 49.4 | $-1855.73 |
| ETH | 2869 | 48.0 | 48.9 | $-1793.83 |
| SOL | 2953 | 47.8 | 49.5 | $-2395.78 |
| XRP | 3005 | 48.8 | 49.3 | $-1624.99 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
