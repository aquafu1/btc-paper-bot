# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 24, 6:45 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1291 windows, 34521 settled trades, 407 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 679 | 33.9 | 35.3 | $-569.22 | -8.4% | $430.78 | -1.7 | done | can't tell from luck |
| value_ev10 | 1662 | 38.6 | 39.2 | $-837.27 | -5.0% | $162.73 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 3464 | 50.8 | 50.2 | $-1091.79 | -3.2% | $-91.79 | -1.9 | done | can't tell from luck |
| value_ev5 | 2509 | 40.4 | 41.1 | $-1304.95 | -5.2% | $-304.95 | -2.2 | done | losing for real |
| momentum_60m_0.30pct | 2893 | 49.5 | 49.4 | $-1348.94 | -4.7% | $-348.94 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 2893 | 50.5 | 51.0 | $-1640.87 | -5.7% | $-640.87 | -3.1 | done | losing for real |
| trend_filter | 2041 | 48.9 | 50.5 | $-1658.41 | -8.1% | $-658.41 | -3.8 | done | losing for real |
| momentum_15m_0.10pct | 3464 | 49.2 | 50.3 | $-2151.20 | -6.2% | $-1151.20 | -3.7 | done | losing for real |
| coinflip | 4972 | 50.0 | 50.1 | $-2265.30 | -4.6% | $-1265.30 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 4972 | 50.5 | 51.4 | $-2803.61 | -5.6% | $-1803.61 | -4.1 | done | losing for real |
| always_up | 4972 | 47.9 | 49.3 | $-3613.01 | -7.3% | $-2613.01 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 8281 | 48.0 | 48.8 | $-4847.47 |
| ETH | 8930 | 48.2 | 48.2 | $-4852.86 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
