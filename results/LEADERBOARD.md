# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 10, 3:45 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 3 windows, 25 settled trades, 53 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 3 | 100.0 | 51.3 | $+28.44 | +94.8% | $1028.44 | +13.1 | Wed 8:00 AM | too few trades (3/200) |
| always_up | 4 | 75.0 | 51.6 | $+18.44 | +46.1% | $1018.44 | +0.9 | Wed 3:45 AM | too few trades (4/200) |
| momentum_15m_0.10pct | 3 | 66.7 | 51.2 | $+9.50 | +31.7% | $1009.50 | +0.5 | Wed 8:00 AM | too few trades (3/200) |
| trend_filter | 1 | 100.0 | 56.1 | $+7.81 | +78.1% | $1007.81 | - | Thu 5:15 PM | too few trades (1/200) |
| coinflip | 4 | 50.0 | 53.9 | $-2.48 | -6.2% | $997.52 | -0.1 | Wed 3:45 AM | too few trades (4/200) |
| reversal_15m_0.10pct | 3 | 33.3 | 55.0 | $-12.19 | -40.6% | $987.81 | -0.7 | Wed 8:00 AM | too few trades (3/200) |
| momentum_5m_0.00pct | 4 | 25.0 | 54.2 | $-22.19 | -55.5% | $977.81 | -1.2 | Wed 3:45 AM | too few trades (4/200) |
| reversal_60m_0.30pct | 3 | 0.0 | 53.5 | $-30.00 | -100.0% | $970.00 | - | Wed 8:00 AM | too few trades (3/200) |
| value_ev5 | 0 | - | - | - | - | - | - | - | no trades yet |
| value_ev10 | 0 | - | - | - | - | - | - | - | no trades yet |
| value_ev20 | 0 | - | - | - | - | - | - | - | no trades yet |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7 | 42.9 | 52.6 | $-7.25 |
| ETH | 5 | 60.0 | 52.4 | $+6.81 |
| SOL | 7 | 57.1 | 53.2 | $+4.34 |
| XRP | 6 | 50.0 | 54.2 | $-6.56 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
