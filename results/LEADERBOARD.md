# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 10, 8:17 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 21 windows, 516 settled trades, 41 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 34 | 55.9 | 48.7 | $+49.32 | +14.5% | $1049.32 | +0.8 | Wed 7:15 PM | too few trades (34/200) |
| coinflip | 76 | 57.9 | 51.7 | $+38.77 | +5.1% | $1038.77 | +0.5 | Wed 3:45 AM | too few trades (76/200) |
| momentum_5m_0.00pct | 76 | 56.6 | 51.7 | $+18.80 | +2.5% | $1018.80 | +0.2 | Wed 3:45 AM | too few trades (76/200) |
| reversal_15m_0.10pct | 43 | 51.2 | 48.8 | $+7.97 | +1.9% | $1007.97 | +0.1 | Wed 1:30 PM | too few trades (43/200) |
| momentum_15m_0.10pct | 43 | 48.8 | 51.0 | $-33.70 | -7.8% | $966.30 | -0.5 | Wed 1:30 PM | too few trades (43/200) |
| value_ev10 | 39 | 38.5 | 38.8 | $-34.64 | -8.9% | $965.36 | -0.5 | Wed 3:45 PM | too few trades (39/200) |
| value_ev20 | 21 | 28.6 | 35.6 | $-50.76 | -24.2% | $949.24 | -0.9 | Thu 12:30 PM | too few trades (21/200) |
| trend_filter | 27 | 44.4 | 53.7 | $-54.09 | -20.0% | $945.91 | -1.1 | Thu 2:30 AM | too few trades (27/200) |
| momentum_60m_0.30pct | 34 | 44.1 | 52.7 | $-60.31 | -17.7% | $939.69 | -1.1 | Wed 7:15 PM | too few trades (34/200) |
| value_ev5 | 47 | 34.0 | 39.6 | $-96.14 | -20.5% | $903.86 | -1.2 | Wed 11:30 AM | too few trades (47/200) |
| always_up | 76 | 39.5 | 48.0 | $-183.51 | -24.1% | $816.49 | -2.1 | Wed 3:45 AM | too few trades (76/200) |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 110 | 48.2 | 48.4 | $-39.73 |
| ETH | 119 | 40.3 | 46.8 | $-274.19 |
| SOL | 144 | 49.3 | 47.7 | $-4.95 |
| XRP | 143 | 49.7 | 47.0 | $-79.44 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
