# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 11, 3:05 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 48 windows, 1194 settled trades, 69 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 82 | 62.2 | 51.2 | $+152.07 | +18.5% | $1152.07 | +1.7 | Wed 7:30 PM | too few trades (82/200) |
| momentum_5m_0.00pct | 184 | 53.8 | 51.3 | $+27.53 | +1.5% | $1027.53 | +0.2 | Wed 3:45 AM | too few trades (184/200) |
| value_ev10 | 69 | 43.5 | 39.2 | $+26.12 | +3.8% | $1026.12 | +0.3 | Thu 12:45 AM | too few trades (69/200) |
| reversal_15m_0.10pct | 113 | 52.2 | 51.3 | $+1.54 | +0.1% | $1001.54 | +0.0 | Wed 11:45 AM | too few trades (113/200) |
| value_ev20 | 29 | 34.5 | 35.8 | $-24.27 | -8.4% | $975.73 | -0.3 | Fri 10:45 PM | too few trades (29/200) |
| momentum_15m_0.10pct | 113 | 47.8 | 50.0 | $-60.10 | -5.3% | $939.90 | -0.5 | Wed 11:45 AM | too few trades (113/200) |
| value_ev5 | 91 | 39.6 | 40.4 | $-62.15 | -6.8% | $937.85 | -0.6 | Wed 4:45 PM | too few trades (91/200) |
| coinflip | 184 | 51.1 | 51.4 | $-80.23 | -4.4% | $919.77 | -0.6 | Wed 3:45 AM | too few trades (184/200) |
| trend_filter | 63 | 42.9 | 50.4 | $-111.85 | -17.8% | $888.15 | -1.4 | Thu 4:00 AM | too few trades (63/200) |
| momentum_60m_0.30pct | 82 | 37.8 | 50.2 | $-212.94 | -26.0% | $787.06 | -2.4 | Wed 7:30 PM | too few trades (82/200) |
| always_up | 184 | 40.8 | 49.7 | $-399.36 | -21.7% | $600.64 | -3.0 | Wed 3:45 AM | too few trades (184/200) |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 246 | 45.9 | 49.1 | $-155.52 |
| ETH | 287 | 43.9 | 47.9 | $-345.26 |
| SOL | 330 | 47.9 | 48.3 | $-176.74 |
| XRP | 331 | 51.1 | 48.6 | $-66.12 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
