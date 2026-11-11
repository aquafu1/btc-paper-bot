# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 11, 8:35 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 70 windows, 1749 settled trades, 40 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_5m_0.00pct | 275 | 56.4 | 51.0 | $+198.66 | +7.2% | $1198.66 | +1.2 | done | can't tell from luck |
| reversal_60m_0.30pct | 120 | 60.0 | 52.1 | $+153.07 | +12.8% | $1153.07 | +1.4 | Wed 8:00 PM | too few trades (120/200) |
| reversal_15m_0.10pct | 163 | 55.8 | 51.6 | $+99.55 | +6.1% | $1099.55 | +0.8 | Wed 12:30 PM | too few trades (163/200) |
| value_ev10 | 94 | 43.6 | 39.4 | $+42.23 | +4.5% | $1042.23 | +0.4 | Thu 4:00 AM | too few trades (94/200) |
| value_ev20 | 41 | 34.1 | 35.7 | $-33.85 | -8.3% | $966.15 | -0.4 | Sat 3:30 AM | too few trades (41/200) |
| value_ev5 | 131 | 41.2 | 41.1 | $-52.67 | -4.0% | $947.33 | -0.4 | Wed 5:45 PM | too few trades (131/200) |
| trend_filter | 92 | 45.7 | 49.1 | $-92.85 | -10.1% | $907.15 | -0.9 | Thu 4:45 AM | too few trades (92/200) |
| coinflip | 275 | 50.2 | 51.5 | $-159.33 | -5.8% | $840.67 | -1.0 | done | can't tell from luck |
| momentum_15m_0.10pct | 163 | 44.2 | 49.9 | $-220.37 | -13.5% | $779.63 | -1.7 | Wed 12:30 PM | too few trades (163/200) |
| momentum_60m_0.30pct | 120 | 40.0 | 49.2 | $-241.37 | -20.1% | $758.63 | -2.2 | Wed 8:00 PM | too few trades (120/200) |
| always_up | 275 | 42.9 | 50.2 | $-479.85 | -17.4% | $520.15 | -2.9 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 355 | 47.0 | 49.7 | $-125.12 |
| ETH | 419 | 46.5 | 48.6 | $-218.90 |
| SOL | 481 | 48.6 | 48.2 | $-262.94 |
| XRP | 494 | 50.4 | 48.4 | $-179.81 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
