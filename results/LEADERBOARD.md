# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 13, 10:00 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 248 windows, 6488 settled trades, 66 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 641 | 55.4 | 52.2 | $+137.29 | +2.1% | $1137.29 | +0.6 | done | can't tell from luck |
| reversal_60m_0.30pct | 515 | 53.4 | 52.1 | $-75.99 | -1.5% | $924.01 | -0.4 | done | can't tell from luck |
| value_ev20 | 114 | 34.2 | 36.7 | $-120.27 | -10.6% | $879.73 | -0.9 | Sun 12:00 PM | too few trades (114/200) |
| value_ev10 | 310 | 37.1 | 40.9 | $-393.26 | -12.7% | $606.74 | -1.9 | done | can't tell from luck |
| trend_filter | 343 | 46.1 | 50.5 | $-439.72 | -12.8% | $560.28 | -2.4 | done | losing for real |
| value_ev5 | 457 | 39.4 | 42.6 | $-525.11 | -11.5% | $474.89 | -2.2 | done | losing for real |
| momentum_60m_0.30pct | 515 | 46.6 | 50.0 | $-579.15 | -11.2% | $420.85 | -2.6 | done | losing for real |
| momentum_5m_0.00pct | 984 | 50.1 | 51.6 | $-689.17 | -7.0% | $310.83 | -2.3 | done | losing for real |
| coinflip | 984 | 49.3 | 50.9 | $-747.29 | -7.6% | $252.71 | -2.5 | done | losing for real |
| momentum_15m_0.10pct | 641 | 44.6 | 50.0 | $-933.26 | -14.6% | $66.74 | -3.8 | done | losing for real |
| always_up | 984 | 46.7 | 50.5 | $-1153.69 | -11.7% | $-153.69 | -3.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1454 | 46.6 | 49.8 | $-1510.42 |
| ETH | 1619 | 46.7 | 49.1 | $-1669.85 |
| SOL | 1679 | 48.1 | 49.4 | $-1374.05 |
| XRP | 1736 | 48.7 | 49.2 | $-965.29 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
