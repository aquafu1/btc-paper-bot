# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 21, 2:35 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 986 windows, 27407 settled trades, 54 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 503 | 34.4 | 34.9 | $-265.26 | -5.3% | $734.74 | -0.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 2798 | 51.1 | 50.4 | $-854.44 | -3.1% | $145.56 | -1.6 | done | can't tell from luck |
| value_ev10 | 1254 | 37.6 | 39.1 | $-877.53 | -7.0% | $122.47 | -2.0 | done | losing for real |
| momentum_60m_0.30pct | 2352 | 49.9 | 49.7 | $-1033.57 | -4.4% | $-33.57 | -2.1 | done | losing for real |
| trend_filter | 1643 | 49.7 | 50.9 | $-1162.65 | -7.1% | $-162.65 | -2.9 | done | losing for real |
| value_ev5 | 1896 | 39.6 | 41.0 | $-1244.87 | -6.6% | $-244.87 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 2352 | 50.1 | 50.9 | $-1578.78 | -6.7% | $-578.78 | -3.3 | done | losing for real |
| coinflip | 3937 | 50.3 | 50.3 | $-1721.19 | -4.4% | $-721.19 | -2.8 | done | losing for real |
| momentum_15m_0.10pct | 2798 | 48.9 | 50.3 | $-1912.05 | -6.8% | $-912.05 | -3.7 | done | losing for real |
| momentum_5m_0.00pct | 3937 | 50.9 | 51.5 | $-1997.12 | -5.1% | $-997.12 | -3.3 | done | losing for real |
| always_up | 3937 | 46.7 | 49.6 | $-4021.91 | -10.2% | $-3021.91 | -6.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6255 | 48.2 | 49.1 | $-3567.80 |
| ETH | 6810 | 48.0 | 48.5 | $-4437.19 |
| SOL | 7155 | 48.1 | 48.6 | $-4215.17 |
| XRP | 7187 | 48.1 | 48.5 | $-4449.20 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
