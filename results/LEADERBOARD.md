# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 11, 9:15 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 73 windows, 1815 settled trades, 54 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_5m_0.00pct | 284 | 56.3 | 51.0 | $+196.29 | +6.9% | $1196.29 | +1.2 | done | can't tell from luck |
| reversal_60m_0.30pct | 125 | 60.8 | 52.6 | $+160.78 | +12.9% | $1160.78 | +1.5 | Wed 7:45 PM | too few trades (125/200) |
| reversal_15m_0.10pct | 171 | 56.1 | 52.0 | $+100.36 | +5.9% | $1100.36 | +0.8 | Wed 12:15 PM | too few trades (171/200) |
| value_ev10 | 98 | 43.9 | 39.5 | $+39.52 | +4.0% | $1039.52 | +0.3 | Thu 3:30 AM | too few trades (98/200) |
| value_ev20 | 41 | 34.1 | 35.7 | $-33.85 | -8.3% | $966.15 | -0.4 | Sat 6:00 AM | too few trades (41/200) |
| value_ev5 | 137 | 41.6 | 41.1 | $-58.07 | -4.2% | $941.93 | -0.4 | Wed 5:15 PM | too few trades (137/200) |
| trend_filter | 95 | 45.3 | 48.7 | $-99.47 | -10.5% | $900.53 | -1.0 | Thu 4:45 AM | too few trades (95/200) |
| coinflip | 284 | 49.6 | 51.5 | $-201.64 | -7.1% | $798.36 | -1.2 | done | can't tell from luck |
| momentum_15m_0.10pct | 171 | 43.9 | 49.4 | $-237.58 | -13.9% | $762.42 | -1.8 | Wed 12:15 PM | too few trades (171/200) |
| momentum_60m_0.30pct | 125 | 39.2 | 48.4 | $-267.99 | -21.4% | $732.01 | -2.4 | Wed 7:45 PM | too few trades (125/200) |
| always_up | 284 | 43.7 | 50.4 | $-472.74 | -16.6% | $527.26 | -2.9 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 379 | 47.8 | 49.8 | $-97.01 |
| ETH | 432 | 46.3 | 48.6 | $-268.84 |
| SOL | 497 | 48.9 | 48.1 | $-280.33 |
| XRP | 507 | 50.1 | 48.2 | $-228.20 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
