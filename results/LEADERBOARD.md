# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 11, 12:30 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 86 windows, 2183 settled trades, 42 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_5m_0.00pct | 336 | 56.5 | 50.8 | $+268.98 | +8.0% | $1268.98 | +1.5 | done | can't tell from luck |
| reversal_60m_0.30pct | 161 | 60.2 | 52.9 | $+184.25 | +11.4% | $1184.25 | +1.5 | Wed 5:30 PM | too few trades (161/200) |
| reversal_15m_0.10pct | 208 | 55.8 | 52.2 | $+98.87 | +4.8% | $1098.87 | +0.7 | done | can't tell from luck |
| value_ev10 | 116 | 42.2 | 40.1 | $-3.12 | -0.3% | $996.88 | -0.0 | Thu 3:30 AM | too few trades (116/200) |
| value_ev20 | 43 | 32.6 | 35.9 | $-53.85 | -12.5% | $946.15 | -0.6 | Sat 5:00 PM | too few trades (43/200) |
| trend_filter | 119 | 47.1 | 48.7 | $-75.75 | -6.4% | $924.25 | -0.7 | Thu 2:45 AM | too few trades (119/200) |
| value_ev5 | 159 | 40.3 | 41.6 | $-118.55 | -7.5% | $881.45 | -0.8 | Wed 5:45 PM | too few trades (159/200) |
| coinflip | 336 | 50.0 | 51.5 | $-203.91 | -6.1% | $796.09 | -1.2 | done | can't tell from luck |
| momentum_15m_0.10pct | 208 | 44.2 | 49.5 | $-279.81 | -13.5% | $720.19 | -1.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 161 | 39.8 | 48.7 | $-333.47 | -20.7% | $666.53 | -2.6 | Wed 5:30 PM | too few trades (161/200) |
| always_up | 336 | 46.1 | 50.1 | $-364.24 | -10.8% | $635.76 | -2.0 | done | can't tell from luck |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 470 | 48.1 | 49.8 | $-121.03 |
| ETH | 531 | 47.1 | 48.6 | $-256.22 |
| SOL | 584 | 50.0 | 48.4 | $-174.82 |
| XRP | 598 | 49.7 | 48.6 | $-328.53 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
