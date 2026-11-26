# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 26, 11:20 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1501 windows, 37451 settled trades, 359 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 760 | 34.3 | 35.4 | $-579.35 | -7.6% | $420.65 | -1.6 | done | can't tell from luck |
| value_ev10 | 1826 | 38.4 | 39.2 | $-987.14 | -5.4% | $12.86 | -1.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 3726 | 50.8 | 50.1 | $-1043.29 | -2.8% | $-43.29 | -1.7 | done | can't tell from luck |
| value_ev5 | 2756 | 40.5 | 41.1 | $-1375.02 | -5.0% | $-375.02 | -2.2 | done | losing for real |
| reversal_60m_0.30pct | 3129 | 51.1 | 51.0 | $-1437.96 | -4.6% | $-437.96 | -2.6 | done | losing for real |
| momentum_60m_0.30pct | 3129 | 48.9 | 49.2 | $-1697.92 | -5.4% | $-697.92 | -3.0 | done | losing for real |
| trend_filter | 2220 | 48.6 | 50.3 | $-1899.92 | -8.6% | $-899.92 | -4.1 | done | losing for real |
| momentum_15m_0.10pct | 3726 | 49.2 | 50.2 | $-2229.93 | -6.0% | $-1229.93 | -3.7 | done | losing for real |
| coinflip | 5393 | 50.0 | 50.0 | $-2349.10 | -4.4% | $-1349.10 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 5393 | 50.2 | 51.3 | $-3309.97 | -6.1% | $-2309.97 | -4.6 | done | losing for real |
| always_up | 5393 | 48.0 | 49.2 | $-3564.43 | -6.6% | $-2564.43 | -4.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 9704 | 48.0 | 48.7 | $-5316.10 |
| ETH | 10437 | 48.0 | 47.9 | $-5573.72 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
