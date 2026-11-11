# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 11, 10:05 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 76 windows, 1915 settled trades, 37 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_5m_0.00pct | 299 | 56.9 | 50.9 | $+246.77 | +8.3% | $1246.77 | +1.5 | done | can't tell from luck |
| reversal_60m_0.30pct | 135 | 62.2 | 52.8 | $+209.52 | +15.5% | $1209.52 | +1.9 | Wed 7:15 PM | too few trades (135/200) |
| reversal_15m_0.10pct | 179 | 58.1 | 52.1 | $+164.17 | +9.2% | $1164.17 | +1.3 | Wed 12:15 PM | too few trades (179/200) |
| value_ev10 | 104 | 41.3 | 39.7 | $-20.48 | -2.0% | $979.52 | -0.2 | Thu 3:30 AM | too few trades (104/200) |
| value_ev20 | 43 | 32.6 | 35.9 | $-53.85 | -12.5% | $946.15 | -0.6 | Sat 6:30 AM | too few trades (43/200) |
| trend_filter | 100 | 45.0 | 48.5 | $-103.85 | -10.4% | $896.15 | -1.0 | Thu 4:45 AM | too few trades (100/200) |
| value_ev5 | 143 | 39.9 | 41.2 | $-118.07 | -8.3% | $881.93 | -0.9 | Wed 5:30 PM | too few trades (143/200) |
| coinflip | 299 | 49.5 | 51.5 | $-219.98 | -7.4% | $780.02 | -1.3 | done | can't tell from luck |
| momentum_15m_0.10pct | 179 | 41.9 | 49.3 | $-317.58 | -17.7% | $682.42 | -2.4 | Wed 12:15 PM | too few trades (179/200) |
| momentum_60m_0.30pct | 135 | 37.8 | 48.4 | $-322.36 | -23.9% | $677.64 | -2.7 | Wed 7:15 PM | too few trades (135/200) |
| always_up | 299 | 44.1 | 50.1 | $-451.94 | -15.1% | $548.06 | -2.6 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 406 | 46.8 | 49.8 | $-192.38 |
| ETH | 452 | 46.5 | 48.5 | $-277.23 |
| SOL | 521 | 48.9 | 48.2 | $-280.28 |
| XRP | 536 | 50.0 | 48.2 | $-237.75 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
