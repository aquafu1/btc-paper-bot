# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 11, 8:45 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 71 windows, 1757 settled trades, 58 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_5m_0.00pct | 276 | 56.5 | 51.0 | $+212.04 | +7.7% | $1212.04 | +1.3 | done | can't tell from luck |
| reversal_60m_0.30pct | 121 | 59.5 | 52.2 | $+143.07 | +11.8% | $1143.07 | +1.3 | Wed 8:00 PM | too few trades (121/200) |
| reversal_15m_0.10pct | 164 | 55.5 | 51.7 | $+89.55 | +5.5% | $1089.55 | +0.7 | Wed 12:30 PM | too few trades (164/200) |
| value_ev10 | 94 | 43.6 | 39.4 | $+42.23 | +4.5% | $1042.23 | +0.4 | Thu 4:00 AM | too few trades (94/200) |
| value_ev20 | 41 | 34.1 | 35.7 | $-33.85 | -8.3% | $966.15 | -0.4 | Sat 3:30 AM | too few trades (41/200) |
| value_ev5 | 131 | 41.2 | 41.1 | $-52.67 | -4.0% | $947.33 | -0.4 | Wed 5:45 PM | too few trades (131/200) |
| trend_filter | 93 | 46.2 | 49.0 | $-79.47 | -8.5% | $920.53 | -0.8 | Thu 4:30 AM | too few trades (93/200) |
| coinflip | 276 | 50.0 | 51.6 | $-169.33 | -6.1% | $830.67 | -1.1 | done | can't tell from luck |
| momentum_15m_0.10pct | 164 | 44.5 | 49.8 | $-206.99 | -12.6% | $793.01 | -1.6 | Wed 12:30 PM | too few trades (164/200) |
| momentum_60m_0.30pct | 121 | 40.5 | 49.2 | $-227.99 | -18.8% | $772.01 | -2.0 | Wed 8:00 PM | too few trades (121/200) |
| always_up | 276 | 42.8 | 50.2 | $-489.85 | -17.7% | $510.15 | -3.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 363 | 47.1 | 49.7 | $-111.59 |
| ETH | 419 | 46.5 | 48.6 | $-218.90 |
| SOL | 481 | 48.6 | 48.2 | $-262.94 |
| XRP | 494 | 50.4 | 48.4 | $-179.81 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
