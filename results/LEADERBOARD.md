# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 11, 7:35 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 66 windows, 1652 settled trades, 28 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 116 | 59.5 | 52.1 | $+139.73 | +12.0% | $1139.73 | +1.3 | Wed 7:30 PM | too few trades (116/200) |
| reversal_15m_0.10pct | 152 | 55.9 | 51.6 | $+92.50 | +6.1% | $1092.50 | +0.8 | Wed 12:45 PM | too few trades (152/200) |
| momentum_5m_0.00pct | 259 | 53.7 | 50.9 | $+61.32 | +2.4% | $1061.32 | +0.4 | done | can't tell from luck |
| value_ev10 | 88 | 43.2 | 39.1 | $+35.25 | +4.0% | $1035.25 | +0.3 | Thu 4:15 AM | too few trades (88/200) |
| value_ev20 | 39 | 35.9 | 35.5 | $-13.85 | -3.6% | $986.15 | -0.2 | Sat 2:45 AM | too few trades (39/200) |
| value_ev5 | 122 | 41.0 | 40.9 | $-51.98 | -4.3% | $948.02 | -0.4 | Wed 6:00 PM | too few trades (122/200) |
| trend_filter | 90 | 44.4 | 49.1 | $-112.79 | -12.5% | $887.21 | -1.2 | Thu 3:30 AM | too few trades (90/200) |
| coinflip | 259 | 49.8 | 51.6 | $-167.49 | -6.5% | $832.51 | -1.1 | done | can't tell from luck |
| momentum_15m_0.10pct | 152 | 44.1 | 49.7 | $-205.56 | -13.5% | $794.44 | -1.7 | Wed 12:45 PM | too few trades (152/200) |
| momentum_60m_0.30pct | 116 | 40.5 | 49.3 | $-218.98 | -18.9% | $781.02 | -2.0 | Wed 7:30 PM | too few trades (116/200) |
| always_up | 259 | 43.6 | 50.0 | $-406.46 | -15.7% | $593.54 | -2.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 342 | 46.8 | 49.5 | $-121.79 |
| ETH | 391 | 45.3 | 48.3 | $-294.57 |
| SOL | 451 | 48.6 | 48.1 | $-252.46 |
| XRP | 468 | 50.2 | 48.3 | $-179.50 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
