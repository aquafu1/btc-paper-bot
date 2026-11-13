# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 13, 3:35 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 270 windows, 7090 settled trades, 35 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 697 | 54.7 | 52.3 | $+41.64 | +0.6% | $1041.64 | +0.2 | done | can't tell from luck |
| value_ev20 | 127 | 35.4 | 37.0 | $-111.59 | -8.8% | $888.41 | -0.8 | Sun 9:15 AM | too few trades (127/200) |
| reversal_60m_0.30pct | 565 | 52.6 | 52.2 | $-196.75 | -3.5% | $803.25 | -0.9 | done | can't tell from luck |
| value_ev10 | 339 | 37.8 | 40.8 | $-372.60 | -11.0% | $627.40 | -1.7 | done | can't tell from luck |
| trend_filter | 371 | 46.9 | 50.2 | $-409.54 | -11.0% | $590.46 | -2.2 | done | losing for real |
| value_ev5 | 501 | 39.9 | 42.4 | $-496.63 | -9.9% | $503.37 | -2.0 | done | can't tell from luck |
| momentum_60m_0.30pct | 565 | 47.4 | 49.7 | $-535.37 | -9.5% | $464.63 | -2.3 | done | losing for real |
| momentum_5m_0.00pct | 1076 | 50.1 | 51.4 | $-722.44 | -6.7% | $277.56 | -2.3 | done | losing for real |
| coinflip | 1076 | 49.5 | 50.9 | $-748.06 | -7.0% | $251.94 | -2.3 | done | losing for real |
| momentum_15m_0.10pct | 697 | 45.3 | 49.7 | $-886.43 | -12.7% | $113.57 | -3.4 | done | losing for real |
| always_up | 1076 | 47.2 | 50.2 | $-1092.65 | -10.2% | $-92.65 | -3.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1579 | 46.7 | 49.6 | $-1592.95 |
| ETH | 1769 | 46.9 | 49.0 | $-1738.37 |
| SOL | 1837 | 48.3 | 49.3 | $-1373.75 |
| XRP | 1905 | 49.1 | 49.1 | $-825.36 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
