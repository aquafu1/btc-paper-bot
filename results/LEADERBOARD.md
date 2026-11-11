# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 11, 5:50 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 59 windows, 1492 settled trades, 37 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 108 | 62.0 | 52.1 | $+183.41 | +17.0% | $1183.41 | +1.8 | Wed 5:45 PM | too few trades (108/200) |
| reversal_15m_0.10pct | 140 | 57.1 | 51.7 | $+115.63 | +8.3% | $1115.63 | +1.0 | Wed 11:45 AM | too few trades (140/200) |
| value_ev10 | 81 | 44.4 | 38.7 | $+61.79 | +7.6% | $1061.79 | +0.6 | Thu 2:30 AM | too few trades (81/200) |
| momentum_5m_0.00pct | 228 | 53.1 | 50.7 | $+31.66 | +1.4% | $1031.66 | +0.2 | done | can't tell from luck |
| value_ev20 | 38 | 36.8 | 35.4 | $-3.85 | -1.0% | $996.15 | -0.0 | Fri 6:15 PM | too few trades (38/200) |
| value_ev5 | 111 | 41.4 | 40.3 | $-20.40 | -1.8% | $979.60 | -0.2 | Wed 5:00 PM | too few trades (111/200) |
| trend_filter | 82 | 42.7 | 48.9 | $-129.43 | -15.8% | $870.57 | -1.4 | Thu 2:15 AM | too few trades (82/200) |
| coinflip | 228 | 50.0 | 51.6 | $-145.16 | -6.4% | $854.84 | -1.0 | done | can't tell from luck |
| momentum_15m_0.10pct | 140 | 42.9 | 49.5 | $-215.73 | -15.4% | $784.27 | -1.8 | Wed 11:45 AM | too few trades (140/200) |
| momentum_60m_0.30pct | 108 | 38.0 | 49.1 | $-252.91 | -23.4% | $747.10 | -2.4 | Wed 5:45 PM | too few trades (108/200) |
| always_up | 228 | 42.1 | 49.7 | $-419.24 | -18.4% | $580.76 | -2.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 310 | 46.8 | 49.2 | $-87.88 |
| ETH | 358 | 44.1 | 48.1 | $-354.64 |
| SOL | 413 | 47.9 | 48.0 | $-258.52 |
| XRP | 411 | 50.9 | 48.0 | $-93.19 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
