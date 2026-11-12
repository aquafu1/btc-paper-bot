# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 11, 7:15 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 103 windows, 2635 settled trades, 43 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 199 | 58.8 | 52.9 | $+168.87 | +8.5% | $1168.87 | +1.3 | Wed 7:15 PM | too few trades (199/200) |
| reversal_15m_0.10pct | 253 | 56.1 | 52.1 | $+141.56 | +5.6% | $1141.56 | +0.9 | done | can't tell from luck |
| momentum_5m_0.00pct | 404 | 53.0 | 50.8 | $+25.86 | +0.6% | $1025.86 | +0.1 | done | can't tell from luck |
| value_ev10 | 139 | 38.8 | 40.6 | $-119.31 | -8.6% | $880.69 | -0.9 | Thu 7:15 AM | too few trades (139/200) |
| value_ev20 | 50 | 28.0 | 36.5 | $-123.85 | -24.8% | $876.15 | -1.4 | Sun 6:15 AM | too few trades (50/200) |
| trend_filter | 141 | 43.3 | 49.0 | $-208.60 | -14.8% | $791.40 | -1.7 | Thu 6:45 AM | too few trades (141/200) |
| coinflip | 404 | 50.2 | 51.4 | $-239.53 | -5.9% | $760.47 | -1.2 | done | can't tell from luck |
| value_ev5 | 189 | 37.0 | 41.9 | $-283.38 | -15.0% | $716.62 | -1.8 | Wed 8:45 PM | too few trades (189/200) |
| momentum_60m_0.30pct | 199 | 41.2 | 49.1 | $-371.39 | -18.7% | $628.61 | -2.6 | Wed 7:15 PM | too few trades (199/200) |
| momentum_15m_0.10pct | 253 | 43.9 | 50.0 | $-377.22 | -14.9% | $622.78 | -2.4 | done | losing for real |
| always_up | 404 | 47.3 | 50.3 | $-385.37 | -9.5% | $614.63 | -1.9 | done | can't tell from luck |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 567 | 46.0 | 49.8 | $-459.81 |
| ETH | 644 | 46.0 | 48.9 | $-556.64 |
| SOL | 702 | 48.3 | 48.4 | $-471.43 |
| XRP | 722 | 50.3 | 49.1 | $-284.48 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
