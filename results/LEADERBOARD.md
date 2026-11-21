# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 21, 7:15 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1005 windows, 27955 settled trades, 63 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 518 | 34.2 | 35.0 | $-312.56 | -6.0% | $687.44 | -1.0 | done | can't tell from luck |
| reversal_15m_0.10pct | 2847 | 51.0 | 50.4 | $-893.77 | -3.1% | $106.23 | -1.7 | done | can't tell from luck |
| value_ev10 | 1282 | 37.4 | 39.1 | $-934.13 | -7.3% | $65.87 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 2404 | 50.0 | 49.7 | $-1030.71 | -4.3% | $-30.71 | -2.1 | done | losing for real |
| trend_filter | 1674 | 49.6 | 50.8 | $-1230.99 | -7.4% | $-230.99 | -3.1 | done | losing for real |
| value_ev5 | 1943 | 39.5 | 41.0 | $-1302.38 | -6.7% | $-302.38 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 2404 | 50.0 | 50.9 | $-1652.52 | -6.9% | $-652.52 | -3.5 | done | losing for real |
| coinflip | 4012 | 50.4 | 50.4 | $-1705.80 | -4.3% | $-705.80 | -2.7 | done | losing for real |
| momentum_15m_0.10pct | 2847 | 49.0 | 50.3 | $-1921.45 | -6.7% | $-921.45 | -3.6 | done | losing for real |
| momentum_5m_0.00pct | 4012 | 50.7 | 51.5 | $-2262.50 | -5.6% | $-1262.50 | -3.7 | done | losing for real |
| always_up | 4012 | 47.1 | 49.5 | $-3782.59 | -9.4% | $-2782.59 | -6.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6372 | 48.2 | 49.0 | $-3659.56 |
| ETH | 6942 | 48.0 | 48.5 | $-4525.20 |
| SOL | 7308 | 48.2 | 48.6 | $-4133.73 |
| XRP | 7333 | 48.1 | 48.4 | $-4710.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
