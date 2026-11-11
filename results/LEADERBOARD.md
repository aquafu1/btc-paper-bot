# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 11, 6:45 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 63 windows, 1572 settled trades, 39 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 113 | 60.2 | 52.1 | $+151.36 | +13.4% | $1151.36 | +1.5 | Wed 6:15 PM | too few trades (113/200) |
| reversal_15m_0.10pct | 146 | 56.2 | 51.9 | $+90.86 | +6.2% | $1090.86 | +0.8 | Wed 12:15 PM | too few trades (146/200) |
| momentum_5m_0.00pct | 244 | 54.1 | 50.8 | $+77.10 | +3.2% | $1077.10 | +0.5 | done | can't tell from luck |
| value_ev10 | 83 | 43.4 | 38.9 | $+41.79 | +5.0% | $1041.79 | +0.4 | Thu 4:00 AM | too few trades (83/200) |
| value_ev20 | 38 | 36.8 | 35.4 | $-3.85 | -1.0% | $996.15 | -0.0 | Fri 11:45 PM | too few trades (38/200) |
| value_ev5 | 115 | 40.9 | 40.6 | $-42.45 | -3.7% | $957.55 | -0.3 | Wed 6:00 PM | too few trades (115/200) |
| trend_filter | 86 | 44.2 | 49.1 | $-112.25 | -13.1% | $887.75 | -1.2 | Thu 2:45 AM | too few trades (86/200) |
| coinflip | 244 | 50.8 | 51.6 | $-119.44 | -4.9% | $880.56 | -0.8 | done | can't tell from luck |
| momentum_15m_0.10pct | 146 | 43.8 | 49.4 | $-193.92 | -13.3% | $806.08 | -1.6 | Wed 12:15 PM | too few trades (146/200) |
| momentum_60m_0.30pct | 113 | 39.8 | 49.2 | $-228.44 | -20.2% | $771.56 | -2.1 | Wed 6:15 PM | too few trades (113/200) |
| always_up | 244 | 41.8 | 49.9 | $-473.75 | -19.4% | $526.25 | -3.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 324 | 47.2 | 49.4 | $-91.67 |
| ETH | 380 | 44.5 | 48.3 | $-356.19 |
| SOL | 427 | 48.5 | 48.1 | $-225.09 |
| XRP | 441 | 50.6 | 48.2 | $-140.05 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
