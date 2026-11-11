# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 11, 5:00 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 56 windows, 1425 settled trades, 42 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 99 | 61.6 | 51.9 | $+160.72 | +16.2% | $1160.72 | +1.7 | Wed 6:45 PM | too few trades (99/200) |
| reversal_15m_0.10pct | 136 | 57.4 | 51.7 | $+117.26 | +8.6% | $1117.26 | +1.0 | Wed 11:15 AM | too few trades (136/200) |
| value_ev10 | 80 | 45.0 | 38.7 | $+71.79 | +9.0% | $1071.79 | +0.6 | Thu 1:00 AM | too few trades (80/200) |
| momentum_5m_0.00pct | 216 | 53.7 | 50.5 | $+56.90 | +2.6% | $1056.90 | +0.4 | done | can't tell from luck |
| value_ev20 | 38 | 36.8 | 35.4 | $-3.85 | -1.0% | $996.15 | -0.0 | Fri 2:30 PM | too few trades (38/200) |
| value_ev5 | 110 | 41.8 | 40.2 | $-10.40 | -0.9% | $989.60 | -0.1 | Wed 4:00 PM | too few trades (110/200) |
| trend_filter | 79 | 44.3 | 48.8 | $-99.43 | -12.6% | $900.57 | -1.1 | Thu 1:30 AM | too few trades (79/200) |
| coinflip | 216 | 50.9 | 51.5 | $-103.47 | -4.8% | $896.53 | -0.7 | done | can't tell from luck |
| momentum_15m_0.10pct | 136 | 42.6 | 49.4 | $-217.28 | -16.0% | $782.72 | -1.8 | Wed 11:15 AM | too few trades (136/200) |
| momentum_60m_0.30pct | 99 | 38.4 | 49.0 | $-226.95 | -22.9% | $773.05 | -2.2 | Wed 6:45 PM | too few trades (99/200) |
| always_up | 216 | 42.6 | 49.6 | $-382.97 | -17.7% | $617.03 | -2.6 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 294 | 47.6 | 49.0 | $-33.83 |
| ETH | 342 | 44.2 | 47.9 | $-324.70 |
| SOL | 395 | 48.6 | 47.8 | $-193.51 |
| XRP | 394 | 51.0 | 47.8 | $-85.64 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
