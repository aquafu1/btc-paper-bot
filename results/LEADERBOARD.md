# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 10, 8:32 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 22 windows, 536 settled trades, 47 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_5m_0.00pct | 80 | 58.8 | 51.6 | $+60.83 | +7.6% | $1060.83 | +0.7 | Wed 3:45 AM | too few trades (80/200) |
| reversal_60m_0.30pct | 34 | 55.9 | 48.7 | $+49.32 | +14.5% | $1049.32 | +0.8 | Wed 8:45 PM | too few trades (34/200) |
| coinflip | 80 | 57.5 | 51.6 | $+42.59 | +5.3% | $1042.59 | +0.5 | Wed 3:45 AM | too few trades (80/200) |
| momentum_15m_0.10pct | 47 | 53.2 | 50.8 | $+8.33 | +1.8% | $1008.33 | +0.1 | Wed 12:45 PM | too few trades (47/200) |
| reversal_15m_0.10pct | 47 | 46.8 | 49.3 | $-32.03 | -6.8% | $967.97 | -0.4 | Wed 12:45 PM | too few trades (47/200) |
| value_ev10 | 39 | 38.5 | 38.8 | $-34.64 | -8.9% | $965.36 | -0.5 | Wed 5:00 PM | too few trades (39/200) |
| value_ev20 | 21 | 28.6 | 35.6 | $-50.76 | -24.2% | $949.24 | -0.9 | Thu 3:00 PM | too few trades (21/200) |
| trend_filter | 27 | 44.4 | 53.7 | $-54.09 | -20.0% | $945.91 | -1.1 | Thu 4:30 AM | too few trades (27/200) |
| momentum_60m_0.30pct | 34 | 44.1 | 52.7 | $-60.31 | -17.7% | $939.69 | -1.1 | Wed 8:45 PM | too few trades (34/200) |
| value_ev5 | 47 | 34.0 | 39.6 | $-96.14 | -20.5% | $903.86 | -1.2 | Wed 12:45 PM | too few trades (47/200) |
| always_up | 80 | 37.5 | 48.3 | $-223.51 | -27.9% | $776.49 | -2.6 | Wed 3:45 AM | too few trades (80/200) |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 115 | 47.8 | 48.6 | $-51.13 |
| ETH | 124 | 41.1 | 46.8 | $-252.34 |
| SOL | 149 | 49.7 | 47.8 | $+4.66 |
| XRP | 148 | 49.3 | 47.2 | $-91.62 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
