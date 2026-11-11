# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 11, 6:00 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 60 windows, 1513 settled trades, 35 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 109 | 62.4 | 52.1 | $+191.36 | +17.6% | $1191.36 | +1.9 | Wed 6:00 PM | too few trades (109/200) |
| reversal_15m_0.10pct | 142 | 57.0 | 51.8 | $+113.57 | +8.0% | $1113.57 | +1.0 | Wed 11:45 AM | too few trades (142/200) |
| value_ev10 | 81 | 44.4 | 38.7 | $+61.79 | +7.6% | $1061.79 | +0.6 | Thu 3:15 AM | too few trades (81/200) |
| momentum_5m_0.00pct | 232 | 52.6 | 50.6 | $+12.58 | +0.5% | $1012.58 | +0.1 | done | can't tell from luck |
| value_ev20 | 38 | 36.8 | 35.4 | $-3.85 | -1.0% | $996.15 | -0.0 | Fri 7:45 PM | too few trades (38/200) |
| value_ev5 | 113 | 41.6 | 40.5 | $-22.45 | -2.0% | $977.55 | -0.2 | Wed 5:00 PM | too few trades (113/200) |
| trend_filter | 83 | 42.2 | 49.0 | $-139.43 | -16.8% | $860.57 | -1.5 | Thu 2:15 AM | too few trades (83/200) |
| coinflip | 232 | 50.0 | 51.6 | $-151.29 | -6.5% | $848.71 | -1.0 | done | can't tell from luck |
| momentum_15m_0.10pct | 142 | 43.0 | 49.5 | $-214.81 | -15.1% | $785.19 | -1.8 | Wed 11:45 AM | too few trades (142/200) |
| momentum_60m_0.30pct | 109 | 37.6 | 49.1 | $-262.91 | -24.1% | $737.10 | -2.5 | Wed 6:00 PM | too few trades (109/200) |
| always_up | 232 | 42.7 | 49.8 | $-407.42 | -17.6% | $592.58 | -2.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 313 | 47.0 | 49.3 | $-82.03 |
| ETH | 364 | 44.0 | 48.2 | $-372.81 |
| SOL | 416 | 48.1 | 48.0 | $-256.63 |
| XRP | 420 | 50.7 | 48.1 | $-111.40 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
