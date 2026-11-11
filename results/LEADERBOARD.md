# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 11, 10:20 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 77 windows, 1939 settled trades, 41 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_5m_0.00pct | 302 | 57.0 | 50.9 | $+252.03 | +8.3% | $1252.03 | +1.5 | done | can't tell from luck |
| reversal_60m_0.30pct | 138 | 61.6 | 52.7 | $+197.77 | +14.3% | $1197.77 | +1.8 | Wed 7:00 PM | too few trades (138/200) |
| reversal_15m_0.10pct | 182 | 57.7 | 52.1 | $+152.41 | +8.4% | $1152.41 | +1.2 | Wed 12:15 PM | too few trades (182/200) |
| value_ev10 | 105 | 41.0 | 39.8 | $-30.48 | -2.9% | $969.52 | -0.2 | Thu 3:30 AM | too few trades (105/200) |
| value_ev20 | 43 | 32.6 | 35.9 | $-53.85 | -12.5% | $946.15 | -0.6 | Sat 7:45 AM | too few trades (43/200) |
| trend_filter | 101 | 45.5 | 48.6 | $-96.84 | -9.6% | $903.16 | -0.9 | Thu 5:00 AM | too few trades (101/200) |
| value_ev5 | 144 | 39.6 | 41.3 | $-128.07 | -8.9% | $871.93 | -0.9 | Wed 5:45 PM | too few trades (144/200) |
| coinflip | 302 | 49.7 | 51.5 | $-214.72 | -7.1% | $785.28 | -1.3 | done | can't tell from luck |
| momentum_15m_0.10pct | 182 | 42.3 | 49.3 | $-313.18 | -17.2% | $686.82 | -2.3 | Wed 12:15 PM | too few trades (182/200) |
| momentum_60m_0.30pct | 138 | 38.4 | 48.5 | $-317.97 | -23.0% | $682.03 | -2.7 | Wed 7:00 PM | too few trades (138/200) |
| always_up | 302 | 44.4 | 50.2 | $-447.54 | -14.8% | $552.46 | -2.6 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 406 | 46.8 | 49.8 | $-192.38 |
| ETH | 461 | 46.4 | 48.5 | $-294.24 |
| SOL | 528 | 48.9 | 48.2 | $-298.11 |
| XRP | 544 | 50.4 | 48.3 | $-215.71 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
