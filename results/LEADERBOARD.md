# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 11, 8:30 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 70 windows, 1730 settled trades, 59 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_5m_0.00pct | 272 | 55.9 | 51.0 | $+170.33 | +6.3% | $1170.33 | +1.1 | done | can't tell from luck |
| reversal_60m_0.30pct | 120 | 60.0 | 52.1 | $+153.07 | +12.8% | $1153.07 | +1.4 | Wed 7:45 PM | too few trades (120/200) |
| reversal_15m_0.10pct | 160 | 56.9 | 51.6 | $+129.55 | +8.1% | $1129.55 | +1.0 | Wed 12:30 PM | too few trades (160/200) |
| value_ev10 | 93 | 44.1 | 39.3 | $+52.23 | +5.6% | $1052.23 | +0.4 | Thu 4:00 AM | too few trades (93/200) |
| value_ev20 | 41 | 34.1 | 35.7 | $-33.85 | -8.3% | $966.15 | -0.4 | Sat 2:15 AM | too few trades (41/200) |
| value_ev5 | 129 | 41.1 | 41.0 | $-55.00 | -4.3% | $945.00 | -0.4 | Wed 5:45 PM | too few trades (129/200) |
| trend_filter | 91 | 45.1 | 49.1 | $-105.18 | -11.6% | $894.82 | -1.1 | Thu 4:45 AM | too few trades (91/200) |
| coinflip | 272 | 50.4 | 51.5 | $-148.40 | -5.5% | $851.60 | -0.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 120 | 40.0 | 49.2 | $-241.37 | -20.1% | $758.63 | -2.2 | Wed 7:45 PM | too few trades (120/200) |
| momentum_15m_0.10pct | 160 | 43.1 | 49.8 | $-248.70 | -15.5% | $751.30 | -2.0 | Wed 12:30 PM | too few trades (160/200) |
| always_up | 272 | 43.4 | 50.1 | $-449.85 | -16.5% | $550.15 | -2.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 355 | 47.0 | 49.7 | $-125.12 |
| ETH | 412 | 46.4 | 48.5 | $-238.21 |
| SOL | 474 | 48.9 | 48.1 | $-226.83 |
| XRP | 489 | 50.3 | 48.3 | $-186.99 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
