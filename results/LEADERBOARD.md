# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 11, 10:45 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 79 windows, 1980 settled trades, 56 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_5m_0.00pct | 308 | 57.5 | 50.9 | $+283.99 | +9.2% | $1283.99 | +1.7 | done | can't tell from luck |
| reversal_60m_0.30pct | 144 | 59.0 | 52.6 | $+137.77 | +9.6% | $1137.77 | +1.2 | Wed 6:00 PM | too few trades (144/200) |
| reversal_15m_0.10pct | 185 | 56.8 | 52.0 | $+122.41 | +6.6% | $1122.41 | +0.9 | Wed 12:15 PM | too few trades (185/200) |
| value_ev10 | 105 | 41.0 | 39.8 | $-30.48 | -2.9% | $969.52 | -0.2 | Thu 4:00 AM | too few trades (105/200) |
| value_ev20 | 43 | 32.6 | 35.9 | $-53.85 | -12.5% | $946.15 | -0.6 | Sat 9:00 AM | too few trades (43/200) |
| trend_filter | 106 | 48.1 | 48.8 | $-54.87 | -5.2% | $945.13 | -0.5 | Thu 3:45 AM | too few trades (106/200) |
| value_ev5 | 144 | 39.6 | 41.3 | $-128.07 | -8.9% | $871.93 | -0.9 | Wed 6:00 PM | too few trades (144/200) |
| coinflip | 308 | 50.3 | 51.6 | $-182.76 | -5.9% | $817.24 | -1.1 | done | can't tell from luck |
| momentum_60m_0.30pct | 144 | 41.0 | 48.7 | $-268.39 | -18.6% | $731.61 | -2.2 | Wed 6:00 PM | too few trades (144/200) |
| momentum_15m_0.10pct | 185 | 43.2 | 49.4 | $-290.04 | -15.7% | $709.96 | -2.1 | Wed 12:15 PM | too few trades (185/200) |
| always_up | 308 | 45.5 | 50.3 | $-397.96 | -12.9% | $602.04 | -2.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 420 | 47.9 | 49.9 | $-133.61 |
| ETH | 476 | 46.8 | 48.7 | $-285.76 |
| SOL | 534 | 49.3 | 48.3 | $-269.00 |
| XRP | 550 | 50.7 | 48.3 | $-173.88 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
