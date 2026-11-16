# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 15, 9:20 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 485 windows, 13344 settled trades, 39 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 247 | 34.8 | 35.8 | $-149.21 | -6.0% | $850.79 | -0.7 | done | can't tell from luck |
| momentum_60m_0.30pct | 1134 | 51.0 | 49.8 | $-197.26 | -1.7% | $802.74 | -0.6 | done | can't tell from luck |
| value_ev10 | 630 | 38.9 | 40.1 | $-380.56 | -6.0% | $619.44 | -1.3 | done | can't tell from luck |
| momentum_15m_0.10pct | 1346 | 50.1 | 49.9 | $-433.21 | -3.2% | $566.79 | -1.2 | done | can't tell from luck |
| value_ev5 | 928 | 40.9 | 41.8 | $-496.74 | -5.4% | $503.26 | -1.4 | done | can't tell from luck |
| trend_filter | 780 | 49.4 | 50.6 | $-528.05 | -6.8% | $471.95 | -1.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 1346 | 49.9 | 51.6 | $-961.77 | -7.1% | $38.23 | -2.7 | done | losing for real |
| coinflip | 1933 | 50.0 | 50.8 | $-1015.78 | -5.3% | $-15.78 | -2.3 | done | losing for real |
| reversal_60m_0.30pct | 1134 | 49.0 | 51.6 | $-1027.97 | -9.1% | $-27.97 | -3.1 | done | losing for real |
| momentum_5m_0.00pct | 1933 | 49.5 | 51.6 | $-1468.28 | -7.6% | $-468.28 | -3.5 | done | losing for real |
| always_up | 1933 | 46.5 | 50.4 | $-2237.47 | -11.6% | $-1237.47 | -5.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3009 | 47.4 | 49.3 | $-2414.14 |
| ETH | 3344 | 48.0 | 48.8 | $-2192.72 |
| SOL | 3473 | 47.8 | 49.3 | $-2442.10 |
| XRP | 3518 | 48.5 | 49.0 | $-1847.35 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
