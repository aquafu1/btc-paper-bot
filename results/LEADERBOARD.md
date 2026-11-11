# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 11, 12:20 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 85 windows, 2171 settled trades, 35 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_5m_0.00pct | 334 | 56.3 | 50.8 | $+250.19 | +7.5% | $1250.19 | +1.4 | done | can't tell from luck |
| reversal_60m_0.30pct | 159 | 59.7 | 52.9 | $+165.45 | +10.4% | $1165.45 | +1.4 | Wed 5:45 PM | too few trades (159/200) |
| reversal_15m_0.10pct | 207 | 56.0 | 52.2 | $+108.87 | +5.3% | $1108.87 | +0.8 | done | can't tell from luck |
| value_ev10 | 116 | 42.2 | 40.1 | $-3.12 | -0.3% | $996.88 | -0.0 | Thu 3:30 AM | too few trades (116/200) |
| value_ev20 | 43 | 32.6 | 35.9 | $-53.85 | -12.5% | $946.15 | -0.6 | Sat 5:00 PM | too few trades (43/200) |
| trend_filter | 119 | 47.1 | 48.7 | $-75.75 | -6.4% | $924.25 | -0.7 | Thu 2:45 AM | too few trades (119/200) |
| value_ev5 | 159 | 40.3 | 41.6 | $-118.55 | -7.5% | $881.45 | -0.8 | Wed 5:45 PM | too few trades (159/200) |
| coinflip | 334 | 50.0 | 51.5 | $-203.59 | -6.1% | $796.41 | -1.2 | done | can't tell from luck |
| momentum_15m_0.10pct | 207 | 44.0 | 49.5 | $-288.93 | -14.0% | $711.07 | -2.0 | done | losing for real |
| momentum_60m_0.30pct | 159 | 40.3 | 48.7 | $-313.47 | -19.7% | $686.53 | -2.5 | Wed 5:45 PM | too few trades (159/200) |
| always_up | 334 | 46.4 | 50.1 | $-344.24 | -10.3% | $655.76 | -1.9 | done | can't tell from luck |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 465 | 48.0 | 49.7 | $-130.06 |
| ETH | 524 | 47.1 | 48.5 | $-243.57 |
| SOL | 584 | 50.0 | 48.4 | $-174.82 |
| XRP | 598 | 49.7 | 48.6 | $-328.53 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
