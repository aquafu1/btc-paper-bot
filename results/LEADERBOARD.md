# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 11, 3:30 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 50 windows, 1263 settled trades, 59 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 87 | 62.1 | 52.0 | $+142.30 | +16.4% | $1142.30 | +1.6 | Wed 7:00 PM | too few trades (87/200) |
| value_ev10 | 75 | 42.7 | 38.5 | $+26.16 | +3.5% | $1026.16 | +0.2 | Wed 11:15 PM | too few trades (75/200) |
| reversal_15m_0.10pct | 118 | 54.2 | 51.9 | $+20.56 | +1.7% | $1020.56 | +0.2 | Wed 11:45 AM | too few trades (118/200) |
| momentum_5m_0.00pct | 192 | 52.6 | 50.2 | $+7.57 | +0.4% | $1007.57 | +0.1 | Wed 3:45 AM | too few trades (192/200) |
| value_ev20 | 35 | 34.3 | 35.0 | $-24.23 | -6.9% | $975.77 | -0.3 | Fri 12:00 PM | too few trades (35/200) |
| value_ev5 | 98 | 38.8 | 39.8 | $-72.11 | -7.4% | $927.89 | -0.6 | Wed 3:45 PM | too few trades (98/200) |
| momentum_15m_0.10pct | 118 | 45.8 | 48.9 | $-110.10 | -9.3% | $889.90 | -1.0 | Wed 11:45 AM | too few trades (118/200) |
| trend_filter | 69 | 42.0 | 47.9 | $-111.81 | -16.2% | $888.19 | -1.3 | Thu 2:15 AM | too few trades (69/200) |
| coinflip | 192 | 50.0 | 51.3 | $-134.20 | -7.0% | $865.80 | -1.0 | Wed 3:45 AM | too few trades (192/200) |
| momentum_60m_0.30pct | 87 | 37.9 | 48.6 | $-202.90 | -23.3% | $797.10 | -2.1 | Wed 7:00 PM | too few trades (87/200) |
| always_up | 192 | 40.1 | 49.7 | $-453.33 | -23.6% | $546.67 | -3.4 | Wed 3:45 AM | too few trades (192/200) |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 258 | 46.1 | 48.8 | $-111.89 |
| ETH | 302 | 44.0 | 47.5 | $-283.04 |
| SOL | 352 | 46.6 | 47.4 | $-317.14 |
| XRP | 351 | 49.6 | 47.6 | $-200.02 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
