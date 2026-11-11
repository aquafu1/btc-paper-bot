# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 11, 1:15 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 89 windows, 2256 settled trades, 55 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_5m_0.00pct | 348 | 56.3 | 50.9 | $+254.13 | +7.3% | $1254.13 | +1.4 | done | can't tell from luck |
| reversal_60m_0.30pct | 167 | 59.3 | 52.8 | $+157.15 | +9.4% | $1157.15 | +1.3 | Wed 5:30 PM | too few trades (167/200) |
| reversal_15m_0.10pct | 215 | 55.8 | 52.4 | $+94.35 | +4.4% | $1094.35 | +0.7 | done | can't tell from luck |
| value_ev10 | 117 | 41.9 | 40.1 | $-13.12 | -1.1% | $986.88 | -0.1 | Thu 4:30 AM | too few trades (117/200) |
| value_ev20 | 44 | 31.8 | 36.0 | $-63.85 | -14.5% | $936.15 | -0.8 | Sat 6:15 PM | too few trades (44/200) |
| trend_filter | 125 | 47.2 | 48.8 | $-83.31 | -6.7% | $916.69 | -0.7 | Thu 2:15 AM | too few trades (125/200) |
| value_ev5 | 162 | 39.5 | 41.6 | $-148.55 | -9.2% | $851.45 | -1.0 | Wed 6:15 PM | too few trades (162/200) |
| coinflip | 348 | 50.0 | 51.6 | $-225.47 | -6.5% | $774.53 | -1.3 | done | can't tell from luck |
| momentum_15m_0.10pct | 215 | 44.2 | 49.4 | $-289.52 | -13.5% | $710.48 | -2.0 | done | can't tell from luck |
| momentum_60m_0.30pct | 167 | 40.7 | 48.9 | $-324.01 | -19.4% | $675.99 | -2.5 | Wed 5:30 PM | too few trades (167/200) |
| always_up | 348 | 46.0 | 50.1 | $-398.00 | -11.4% | $602.00 | -2.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 483 | 48.4 | 49.9 | $-116.19 |
| ETH | 547 | 47.0 | 48.7 | $-295.68 |
| SOL | 606 | 49.7 | 48.5 | $-244.19 |
| XRP | 620 | 49.4 | 48.7 | $-384.15 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
