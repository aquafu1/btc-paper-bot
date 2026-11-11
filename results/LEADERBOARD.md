# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 11, 4:45 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 55 windows, 1394 settled trades, 55 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 96 | 63.5 | 51.9 | $+190.72 | +19.9% | $1190.72 | +2.0 | Wed 7:00 PM | too few trades (96/200) |
| reversal_15m_0.10pct | 132 | 58.3 | 51.7 | $+137.96 | +10.5% | $1137.96 | +1.2 | Wed 11:30 AM | too few trades (132/200) |
| value_ev10 | 80 | 45.0 | 38.7 | $+71.79 | +9.0% | $1071.79 | +0.6 | Thu 12:30 AM | too few trades (80/200) |
| momentum_5m_0.00pct | 212 | 53.3 | 50.5 | $+40.51 | +1.9% | $1040.51 | +0.3 | done | can't tell from luck |
| value_ev20 | 38 | 36.8 | 35.4 | $-3.85 | -1.0% | $996.15 | -0.0 | Fri 1:00 PM | too few trades (38/200) |
| value_ev5 | 109 | 41.3 | 40.2 | $-22.45 | -2.1% | $977.55 | -0.2 | Wed 3:45 PM | too few trades (109/200) |
| coinflip | 212 | 50.9 | 51.5 | $-102.25 | -4.8% | $897.75 | -0.7 | done | can't tell from luck |
| trend_filter | 75 | 42.7 | 48.5 | $-115.82 | -15.4% | $884.18 | -1.3 | Thu 2:45 AM | too few trades (75/200) |
| momentum_15m_0.10pct | 132 | 41.7 | 49.3 | $-233.67 | -17.7% | $766.33 | -2.0 | Wed 11:30 AM | too few trades (132/200) |
| momentum_60m_0.30pct | 96 | 36.5 | 48.9 | $-253.35 | -26.4% | $746.65 | -2.6 | Wed 7:00 PM | too few trades (96/200) |
| always_up | 212 | 42.0 | 49.6 | $-399.36 | -18.8% | $600.64 | -2.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 286 | 46.9 | 48.9 | $-54.24 |
| ETH | 336 | 44.6 | 47.9 | $-284.00 |
| SOL | 387 | 48.3 | 47.7 | $-201.56 |
| XRP | 385 | 50.4 | 47.8 | $-149.97 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
