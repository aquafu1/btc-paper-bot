# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 20, 8:00 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 912 windows, 25171 settled trades, 57 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 471 | 35.0 | 34.8 | $-171.30 | -3.6% | $828.70 | -0.6 | done | can't tell from luck |
| value_ev10 | 1154 | 38.1 | 39.1 | $-648.14 | -5.6% | $351.86 | -1.5 | done | can't tell from luck |
| momentum_60m_0.30pct | 2132 | 50.0 | 49.8 | $-925.76 | -4.3% | $74.24 | -2.0 | done | losing for real |
| trend_filter | 1494 | 49.9 | 51.0 | $-1020.55 | -6.8% | $-20.55 | -2.7 | done | losing for real |
| value_ev5 | 1744 | 39.8 | 41.0 | $-1062.52 | -6.1% | $-62.52 | -2.1 | done | losing for real |
| reversal_15m_0.10pct | 2562 | 50.5 | 50.5 | $-1064.15 | -4.2% | $-64.15 | -2.1 | done | losing for real |
| momentum_15m_0.10pct | 2562 | 49.5 | 50.3 | $-1381.28 | -5.4% | $-381.28 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 2132 | 50.0 | 50.8 | $-1428.62 | -6.7% | $-428.62 | -3.2 | done | losing for real |
| coinflip | 3640 | 50.3 | 50.3 | $-1563.91 | -4.3% | $-563.91 | -2.6 | done | losing for real |
| momentum_5m_0.00pct | 3640 | 51.1 | 51.6 | $-1739.43 | -4.8% | $-739.43 | -3.0 | done | losing for real |
| always_up | 3640 | 46.7 | 49.7 | $-3695.01 | -10.2% | $-2695.01 | -6.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5732 | 48.2 | 49.1 | $-3252.93 |
| ETH | 6259 | 48.2 | 48.5 | $-3871.27 |
| SOL | 6569 | 48.1 | 48.6 | $-3847.37 |
| XRP | 6611 | 48.3 | 48.5 | $-3729.12 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
