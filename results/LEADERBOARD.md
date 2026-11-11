# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 11, 11:45 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 83 windows, 2094 settled trades, 63 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_5m_0.00pct | 324 | 57.4 | 50.9 | $+313.85 | +9.7% | $1313.85 | +1.8 | done | can't tell from luck |
| reversal_60m_0.30pct | 151 | 58.9 | 52.8 | $+139.60 | +9.2% | $1139.60 | +1.2 | Wed 6:15 PM | too few trades (151/200) |
| reversal_15m_0.10pct | 198 | 56.6 | 52.1 | $+129.52 | +6.5% | $1129.52 | +0.9 | Wed 11:45 AM | too few trades (198/200) |
| value_ev10 | 114 | 43.0 | 40.1 | $+16.88 | +1.5% | $1016.88 | +0.1 | Thu 3:00 AM | too few trades (114/200) |
| trend_filter | 113 | 48.7 | 48.7 | $-33.05 | -2.9% | $966.95 | -0.3 | Thu 3:15 AM | too few trades (113/200) |
| value_ev20 | 43 | 32.6 | 35.9 | $-53.85 | -12.5% | $946.15 | -0.6 | Sat 1:30 PM | too few trades (43/200) |
| value_ev5 | 154 | 41.6 | 41.5 | $-68.55 | -4.5% | $931.45 | -0.5 | Wed 5:45 PM | too few trades (154/200) |
| coinflip | 324 | 50.3 | 51.5 | $-176.92 | -5.5% | $823.08 | -1.0 | done | can't tell from luck |
| momentum_60m_0.30pct | 151 | 41.1 | 48.6 | $-269.63 | -17.9% | $730.37 | -2.2 | Wed 6:15 PM | too few trades (151/200) |
| momentum_15m_0.10pct | 198 | 43.4 | 49.4 | $-290.02 | -14.6% | $709.98 | -2.1 | Wed 11:45 AM | too few trades (198/200) |
| always_up | 324 | 46.6 | 50.1 | $-318.61 | -9.8% | $681.39 | -1.8 | done | can't tell from luck |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 451 | 48.3 | 49.7 | $-79.85 |
| ETH | 507 | 47.7 | 48.6 | $-158.73 |
| SOL | 560 | 50.4 | 48.3 | $-117.94 |
| XRP | 576 | 50.2 | 48.5 | $-254.25 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
