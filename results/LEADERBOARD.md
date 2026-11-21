# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 21, 12:15 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 977 windows, 27121 settled trades, 72 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 499 | 34.5 | 34.9 | $-249.50 | -5.0% | $750.50 | -0.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 2771 | 51.2 | 50.5 | $-744.76 | -2.7% | $255.24 | -1.4 | done | can't tell from luck |
| value_ev10 | 1238 | 37.8 | 39.1 | $-788.71 | -6.4% | $211.29 | -1.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 2320 | 50.1 | 49.7 | $-935.34 | -4.0% | $64.66 | -1.9 | done | can't tell from luck |
| value_ev5 | 1877 | 39.8 | 41.0 | $-1126.05 | -6.0% | $-126.05 | -2.2 | done | losing for real |
| trend_filter | 1625 | 49.7 | 50.9 | $-1172.26 | -7.2% | $-172.26 | -3.0 | done | losing for real |
| reversal_60m_0.30pct | 2320 | 49.9 | 50.9 | $-1620.75 | -7.0% | $-620.75 | -3.4 | done | losing for real |
| coinflip | 3900 | 50.2 | 50.3 | $-1822.30 | -4.7% | $-822.30 | -2.9 | done | losing for real |
| momentum_15m_0.10pct | 2771 | 48.8 | 50.3 | $-1970.91 | -7.1% | $-970.91 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 3900 | 50.7 | 51.5 | $-2131.48 | -5.5% | $-1131.48 | -3.5 | done | losing for real |
| always_up | 3900 | 46.8 | 49.6 | $-3929.99 | -10.1% | $-2929.99 | -6.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6180 | 48.2 | 49.1 | $-3547.87 |
| ETH | 6744 | 48.0 | 48.5 | $-4400.29 |
| SOL | 7083 | 48.1 | 48.6 | $-4122.68 |
| XRP | 7114 | 48.1 | 48.4 | $-4421.21 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
