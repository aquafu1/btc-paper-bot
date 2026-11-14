# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 14, 6:05 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 328 windows, 8744 settled trades, 58 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 701 | 53.4 | 51.8 | $-81.14 | -1.2% | $918.86 | -0.3 | done | can't tell from luck |
| value_ev20 | 168 | 34.5 | 36.7 | $-174.62 | -10.4% | $825.38 | -1.1 | Sat 10:15 PM | too few trades (168/200) |
| reversal_15m_0.10pct | 868 | 53.0 | 52.0 | $-200.99 | -2.3% | $799.01 | -0.7 | done | can't tell from luck |
| value_ev10 | 420 | 37.9 | 40.4 | $-431.93 | -10.3% | $568.07 | -1.8 | done | can't tell from luck |
| value_ev5 | 627 | 39.7 | 42.1 | $-617.72 | -9.9% | $382.28 | -2.2 | done | losing for real |
| trend_filter | 479 | 44.7 | 50.3 | $-748.15 | -15.6% | $251.85 | -3.5 | done | losing for real |
| coinflip | 1304 | 50.1 | 50.9 | $-760.74 | -5.8% | $239.26 | -2.2 | done | losing for real |
| momentum_60m_0.30pct | 701 | 46.6 | 49.9 | $-786.76 | -11.2% | $213.24 | -3.0 | done | losing for real |
| momentum_15m_0.10pct | 868 | 47.0 | 49.8 | $-848.98 | -9.8% | $151.02 | -2.9 | done | losing for real |
| always_up | 1304 | 47.9 | 50.4 | $-1189.11 | -9.1% | $-189.11 | -3.4 | done | losing for real |
| momentum_5m_0.00pct | 1304 | 48.1 | 51.3 | $-1358.49 | -10.4% | $-358.49 | -3.9 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1953 | 46.4 | 49.3 | $-1964.91 |
| ETH | 2196 | 46.9 | 48.8 | $-2078.97 |
| SOL | 2279 | 47.9 | 49.3 | $-1858.40 |
| XRP | 2316 | 48.6 | 49.1 | $-1296.37 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
