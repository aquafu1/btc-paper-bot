# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 13, 8:05 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 240 windows, 6246 settled trades, 69 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 615 | 56.3 | 52.2 | $+241.82 | +3.9% | $1241.82 | +1.0 | done | can't tell from luck |
| reversal_60m_0.30pct | 488 | 54.3 | 52.3 | $+7.74 | +0.2% | $1007.74 | +0.0 | done | can't tell from luck |
| value_ev20 | 113 | 34.5 | 36.6 | $-110.27 | -9.8% | $889.73 | -0.8 | Sun 9:30 AM | too few trades (113/200) |
| value_ev10 | 302 | 38.1 | 40.8 | $-313.26 | -10.4% | $686.74 | -1.5 | done | can't tell from luck |
| value_ev5 | 441 | 39.7 | 42.4 | $-460.33 | -10.4% | $539.67 | -1.9 | done | can't tell from luck |
| trend_filter | 328 | 45.1 | 50.3 | $-460.59 | -14.0% | $539.41 | -2.6 | done | losing for real |
| momentum_60m_0.30pct | 488 | 45.7 | 49.7 | $-597.93 | -12.3% | $402.07 | -2.8 | done | losing for real |
| coinflip | 952 | 49.5 | 50.9 | $-672.65 | -7.1% | $327.35 | -2.2 | done | losing for real |
| momentum_5m_0.00pct | 952 | 49.8 | 51.5 | $-704.54 | -7.4% | $295.46 | -2.4 | done | losing for real |
| always_up | 952 | 47.8 | 50.5 | $-917.85 | -9.6% | $82.15 | -3.1 | done | losing for real |
| momentum_15m_0.10pct | 615 | 43.7 | 49.9 | $-972.17 | -15.8% | $27.83 | -4.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1396 | 46.5 | 49.7 | $-1426.84 |
| ETH | 1558 | 46.7 | 49.0 | $-1571.32 |
| SOL | 1611 | 48.4 | 49.4 | $-1199.69 |
| XRP | 1681 | 49.1 | 49.2 | $-762.17 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
