# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 11, 5:15 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 57 windows, 1449 settled trades, 43 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 103 | 62.1 | 52.0 | $+173.92 | +16.9% | $1173.92 | +1.8 | Wed 6:00 PM | too few trades (103/200) |
| reversal_15m_0.10pct | 137 | 57.7 | 51.7 | $+126.69 | +9.2% | $1126.69 | +1.1 | Wed 11:30 AM | too few trades (137/200) |
| momentum_5m_0.00pct | 220 | 54.1 | 50.6 | $+70.11 | +3.2% | $1070.11 | +0.5 | done | can't tell from luck |
| value_ev10 | 81 | 44.4 | 38.7 | $+61.79 | +7.6% | $1061.79 | +0.6 | Thu 1:15 AM | too few trades (81/200) |
| value_ev20 | 38 | 36.8 | 35.4 | $-3.85 | -1.0% | $996.15 | -0.0 | Fri 3:45 PM | too few trades (38/200) |
| value_ev5 | 111 | 41.4 | 40.3 | $-20.40 | -1.8% | $979.60 | -0.2 | Wed 4:15 PM | too few trades (111/200) |
| trend_filter | 79 | 44.3 | 48.8 | $-99.43 | -12.6% | $900.57 | -1.1 | Thu 2:15 AM | too few trades (79/200) |
| coinflip | 220 | 50.5 | 51.5 | $-125.86 | -5.7% | $874.14 | -0.9 | done | can't tell from luck |
| momentum_15m_0.10pct | 137 | 42.3 | 49.5 | $-227.28 | -16.6% | $772.72 | -1.9 | Wed 11:30 AM | too few trades (137/200) |
| momentum_60m_0.30pct | 103 | 37.9 | 49.0 | $-247.65 | -24.0% | $752.35 | -2.4 | Wed 6:00 PM | too few trades (103/200) |
| always_up | 220 | 42.3 | 49.6 | $-403.67 | -18.3% | $596.33 | -2.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 299 | 47.5 | 49.1 | $-45.23 |
| ETH | 347 | 44.4 | 48.0 | $-321.87 |
| SOL | 402 | 48.3 | 47.8 | $-231.18 |
| XRP | 401 | 50.9 | 47.9 | $-97.35 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
