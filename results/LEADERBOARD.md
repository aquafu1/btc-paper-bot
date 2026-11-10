# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 10, 4:02 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 4 windows, 45 settled trades, 57 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| coinflip | 8 | 75.0 | 53.8 | $+32.11 | +40.1% | $1032.11 | +1.3 | Wed 3:45 AM | too few trades (8/200) |
| momentum_15m_0.10pct | 3 | 66.7 | 51.2 | $+9.50 | +31.7% | $1009.50 | +0.5 | Thu 12:45 AM | too few trades (3/200) |
| momentum_60m_0.30pct | 5 | 60.0 | 50.1 | $+8.44 | +16.9% | $1008.44 | +0.4 | Wed 11:15 AM | too few trades (5/200) |
| always_up | 8 | 50.0 | 51.2 | $-2.21 | -2.8% | $997.79 | -0.1 | Wed 3:45 AM | too few trades (8/200) |
| reversal_15m_0.10pct | 3 | 33.3 | 55.0 | $-12.19 | -40.6% | $987.81 | -0.7 | Thu 12:45 AM | too few trades (3/200) |
| trend_filter | 3 | 33.3 | 50.8 | $-12.19 | -40.6% | $987.81 | -0.7 | Thu 12:45 AM | too few trades (3/200) |
| reversal_60m_0.30pct | 5 | 40.0 | 54.6 | $-14.45 | -28.9% | $985.55 | -0.7 | Wed 11:15 AM | too few trades (5/200) |
| value_ev5 | 2 | 0.0 | 50.5 | $-20.00 | -100.0% | $980.00 | - | Thu 5:15 PM | too few trades (2/200) |
| momentum_5m_0.00pct | 8 | 25.0 | 52.4 | $-42.83 | -53.5% | $957.17 | -1.8 | Wed 3:45 AM | too few trades (8/200) |
| value_ev10 | 0 | - | - | - | - | - | - | - | no trades yet |
| value_ev20 | 0 | - | - | - | - | - | - | - | no trades yet |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 14 | 35.7 | 51.0 | $-42.63 |
| ETH | 11 | 45.5 | 52.0 | $-16.70 |
| SOL | 10 | 50.0 | 53.3 | $-5.98 |
| XRP | 10 | 60.0 | 53.4 | $+11.50 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
