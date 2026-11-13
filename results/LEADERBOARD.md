# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 13, 4:30 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 226 windows, 5915 settled trades, 58 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 584 | 55.8 | 52.6 | $+166.34 | +2.8% | $1166.34 | +0.7 | done | can't tell from luck |
| reversal_60m_0.30pct | 460 | 54.3 | 52.3 | $+16.78 | +0.4% | $1016.78 | +0.1 | done | can't tell from luck |
| value_ev20 | 112 | 33.9 | 36.6 | $-124.82 | -11.1% | $875.18 | -0.9 | Sun 4:15 AM | too few trades (112/200) |
| value_ev10 | 295 | 37.6 | 40.7 | $-330.78 | -11.2% | $669.22 | -1.6 | done | can't tell from luck |
| trend_filter | 306 | 45.4 | 50.3 | $-411.56 | -13.4% | $588.44 | -2.4 | done | losing for real |
| value_ev5 | 426 | 39.4 | 42.5 | $-461.66 | -10.8% | $538.34 | -2.0 | done | can't tell from luck |
| momentum_5m_0.00pct | 896 | 50.6 | 51.6 | $-519.23 | -5.8% | $480.77 | -1.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 460 | 45.7 | 49.8 | $-568.92 | -12.4% | $431.08 | -2.7 | done | losing for real |
| coinflip | 896 | 49.7 | 51.0 | $-583.46 | -6.5% | $416.54 | -2.0 | done | losing for real |
| momentum_15m_0.10pct | 584 | 44.2 | 49.7 | $-849.84 | -14.6% | $150.16 | -3.6 | done | losing for real |
| always_up | 896 | 47.2 | 50.3 | $-924.29 | -10.3% | $75.71 | -3.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1325 | 46.6 | 49.7 | $-1290.98 |
| ETH | 1473 | 46.7 | 48.9 | $-1422.89 |
| SOL | 1529 | 47.9 | 49.3 | $-1277.08 |
| XRP | 1588 | 49.3 | 49.1 | $-600.50 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
