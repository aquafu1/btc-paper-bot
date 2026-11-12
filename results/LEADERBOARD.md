# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 12, 8:30 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 156 windows, 3953 settled trades, 60 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 285 | 58.9 | 53.1 | $+237.57 | +8.3% | $1237.57 | +1.5 | done | can't tell from luck |
| reversal_15m_0.10pct | 381 | 56.7 | 52.4 | $+209.98 | +5.5% | $1209.98 | +1.1 | done | can't tell from luck |
| momentum_5m_0.00pct | 616 | 52.4 | 51.3 | $-129.15 | -2.1% | $870.85 | -0.5 | done | can't tell from luck |
| value_ev20 | 74 | 32.4 | 37.2 | $-143.54 | -19.4% | $856.46 | -1.4 | Sun 6:15 AM | too few trades (74/200) |
| value_ev10 | 201 | 36.8 | 40.8 | $-295.12 | -14.7% | $704.88 | -1.8 | done | can't tell from luck |
| coinflip | 616 | 50.8 | 50.9 | $-301.19 | -4.9% | $698.81 | -1.3 | done | can't tell from luck |
| trend_filter | 202 | 42.1 | 49.2 | $-358.28 | -17.7% | $641.72 | -2.5 | done | losing for real |
| value_ev5 | 296 | 38.2 | 42.5 | $-430.38 | -14.5% | $569.62 | -2.3 | done | losing for real |
| momentum_60m_0.30pct | 285 | 41.1 | 49.3 | $-554.69 | -19.5% | $445.31 | -3.3 | done | losing for real |
| momentum_15m_0.10pct | 381 | 43.3 | 50.0 | $-624.92 | -16.4% | $375.08 | -3.3 | done | losing for real |
| always_up | 616 | 45.8 | 50.1 | $-809.00 | -13.1% | $191.00 | -3.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 854 | 46.0 | 49.7 | $-885.51 |
| ETH | 978 | 45.5 | 48.9 | $-1107.47 |
| SOL | 1040 | 48.0 | 48.9 | $-841.65 |
| XRP | 1081 | 50.2 | 49.1 | $-364.09 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
