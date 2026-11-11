# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 11, 1:32 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 42 windows, 1030 settled trades, 54 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_5m_0.00pct | 160 | 57.5 | 52.0 | $+129.39 | +8.1% | $1129.39 | +1.1 | Wed 3:45 AM | too few trades (160/200) |
| reversal_60m_0.30pct | 68 | 57.4 | 49.7 | $+89.14 | +13.1% | $1089.14 | +1.0 | Wed 8:45 PM | too few trades (68/200) |
| value_ev10 | 63 | 46.0 | 38.9 | $+63.82 | +10.1% | $1063.82 | +0.7 | Wed 11:00 PM | too few trades (63/200) |
| momentum_15m_0.10pct | 96 | 53.1 | 51.1 | $+40.81 | +4.3% | $1040.81 | +0.4 | Wed 12:15 PM | too few trades (96/200) |
| value_ev5 | 81 | 43.2 | 40.1 | $+15.55 | +1.9% | $1015.55 | +0.1 | Wed 4:00 PM | too few trades (81/200) |
| coinflip | 160 | 53.1 | 51.5 | $-1.42 | -0.1% | $998.58 | -0.0 | Wed 3:45 AM | too few trades (160/200) |
| value_ev20 | 28 | 35.7 | 35.9 | $-14.27 | -5.1% | $985.73 | -0.2 | Fri 2:45 PM | too few trades (28/200) |
| trend_filter | 50 | 50.0 | 52.2 | $-27.00 | -5.4% | $973.00 | -0.4 | Thu 7:15 AM | too few trades (50/200) |
| reversal_15m_0.10pct | 96 | 46.9 | 50.0 | $-63.00 | -6.6% | $937.00 | -0.6 | Wed 12:15 PM | too few trades (96/200) |
| momentum_60m_0.30pct | 68 | 42.6 | 51.5 | $-118.09 | -17.4% | $881.91 | -1.4 | Wed 8:45 PM | too few trades (68/200) |
| always_up | 160 | 38.8 | 49.4 | $-391.08 | -24.4% | $608.92 | -3.1 | Wed 3:45 AM | too few trades (160/200) |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 210 | 46.7 | 49.2 | $-102.54 |
| ETH | 245 | 45.7 | 47.8 | $-154.47 |
| SOL | 287 | 50.2 | 48.4 | $+22.15 |
| XRP | 288 | 51.4 | 48.3 | $-41.30 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
