# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 20, 7:35 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 910 windows, 25137 settled trades, 34 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 471 | 35.0 | 34.8 | $-171.30 | -3.6% | $828.70 | -0.6 | done | can't tell from luck |
| value_ev10 | 1154 | 38.1 | 39.1 | $-648.14 | -5.6% | $351.86 | -1.5 | done | can't tell from luck |
| momentum_60m_0.30pct | 2129 | 50.0 | 49.8 | $-933.59 | -4.4% | $66.41 | -2.0 | done | losing for real |
| trend_filter | 1491 | 49.9 | 51.0 | $-1028.38 | -6.9% | $-28.38 | -2.7 | done | losing for real |
| reversal_15m_0.10pct | 2559 | 50.6 | 50.5 | $-1034.15 | -4.0% | $-34.15 | -2.0 | done | losing for real |
| value_ev5 | 1743 | 39.8 | 41.0 | $-1052.52 | -6.0% | $-52.52 | -2.1 | done | losing for real |
| momentum_15m_0.10pct | 2559 | 49.4 | 50.3 | $-1410.47 | -5.5% | $-410.47 | -2.8 | done | losing for real |
| reversal_60m_0.30pct | 2129 | 50.0 | 50.8 | $-1418.70 | -6.7% | $-418.70 | -3.1 | done | losing for real |
| coinflip | 3634 | 50.2 | 50.3 | $-1582.96 | -4.4% | $-582.96 | -2.6 | done | losing for real |
| momentum_5m_0.00pct | 3634 | 51.1 | 51.6 | $-1738.62 | -4.8% | $-738.62 | -3.0 | done | losing for real |
| always_up | 3634 | 46.8 | 49.6 | $-3672.70 | -10.1% | $-2672.70 | -6.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5725 | 48.2 | 49.1 | $-3218.46 |
| ETH | 6253 | 48.2 | 48.5 | $-3871.49 |
| SOL | 6556 | 48.1 | 48.6 | $-3854.05 |
| XRP | 6603 | 48.3 | 48.5 | $-3747.51 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
