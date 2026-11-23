# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 23, 4:35 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1186 windows, 32785 settled trades, 47 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 640 | 35.0 | 35.3 | $-348.79 | -5.4% | $651.21 | -1.0 | done | can't tell from luck |
| value_ev10 | 1556 | 38.7 | 39.2 | $-754.05 | -4.8% | $245.95 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 3284 | 50.8 | 50.3 | $-1075.94 | -3.3% | $-75.94 | -1.9 | done | can't tell from luck |
| value_ev5 | 2355 | 40.3 | 41.1 | $-1237.52 | -5.3% | $-237.52 | -2.2 | done | losing for real |
| momentum_60m_0.30pct | 2758 | 49.6 | 49.4 | $-1245.21 | -4.5% | $-245.21 | -2.4 | done | losing for real |
| trend_filter | 1939 | 48.8 | 50.5 | $-1625.94 | -8.4% | $-625.94 | -3.8 | done | losing for real |
| reversal_60m_0.30pct | 2758 | 50.4 | 51.1 | $-1669.74 | -6.1% | $-669.74 | -3.3 | done | losing for real |
| momentum_15m_0.10pct | 3284 | 49.2 | 50.3 | $-1993.85 | -6.1% | $-993.85 | -3.5 | done | losing for real |
| coinflip | 4737 | 50.1 | 50.2 | $-2133.46 | -4.5% | $-1133.46 | -3.1 | done | losing for real |
| momentum_5m_0.00pct | 4737 | 50.1 | 51.4 | $-3030.33 | -6.4% | $-2030.33 | -4.5 | done | losing for real |
| always_up | 4737 | 47.9 | 49.3 | $-3431.63 | -7.2% | $-2431.63 | -5.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7526 | 48.2 | 48.9 | $-4146.03 |
| ETH | 8126 | 48.0 | 48.4 | $-4927.83 |
| SOL | 8530 | 48.2 | 48.4 | $-4385.86 |
| XRP | 8603 | 48.1 | 48.2 | $-5086.76 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
