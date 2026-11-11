# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 11, 10:15 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 77 windows, 1924 settled trades, 56 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_5m_0.00pct | 300 | 57.0 | 50.9 | $+255.02 | +8.5% | $1255.02 | +1.5 | done | can't tell from luck |
| reversal_60m_0.30pct | 136 | 62.5 | 52.8 | $+217.77 | +16.0% | $1217.77 | +2.0 | Wed 7:00 PM | too few trades (136/200) |
| reversal_15m_0.10pct | 180 | 58.3 | 52.1 | $+172.41 | +9.6% | $1172.41 | +1.3 | Wed 12:15 PM | too few trades (180/200) |
| value_ev10 | 105 | 41.0 | 39.8 | $-30.48 | -2.9% | $969.52 | -0.2 | Thu 3:00 AM | too few trades (105/200) |
| value_ev20 | 43 | 32.6 | 35.9 | $-53.85 | -12.5% | $946.15 | -0.6 | Sat 6:30 AM | too few trades (43/200) |
| trend_filter | 100 | 45.0 | 48.5 | $-103.85 | -10.4% | $896.15 | -1.0 | Thu 4:45 AM | too few trades (100/200) |
| value_ev5 | 144 | 39.6 | 41.3 | $-128.07 | -8.9% | $871.93 | -0.9 | Wed 5:30 PM | too few trades (144/200) |
| coinflip | 300 | 49.7 | 51.5 | $-211.73 | -7.1% | $788.27 | -1.3 | done | can't tell from luck |
| momentum_15m_0.10pct | 180 | 41.7 | 49.3 | $-327.58 | -18.2% | $672.42 | -2.4 | Wed 12:15 PM | too few trades (180/200) |
| momentum_60m_0.30pct | 136 | 37.5 | 48.4 | $-332.36 | -24.4% | $667.64 | -2.8 | Wed 7:00 PM | too few trades (136/200) |
| always_up | 300 | 44.0 | 50.1 | $-461.94 | -15.4% | $538.06 | -2.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 406 | 46.8 | 49.8 | $-192.38 |
| ETH | 461 | 46.4 | 48.5 | $-294.24 |
| SOL | 521 | 48.9 | 48.2 | $-280.28 |
| XRP | 536 | 50.0 | 48.2 | $-237.75 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
